from functools import wraps
from rest_framework.authtoken.models import Token
from .exceptions import http_401_unauthorized


def is_authenticated_custom(view):
    try:

        @wraps(view)
        def _view(request, *args, **kwargs):
            print(request.headers)
            token = request.headers["Authorization"].split()[-1]
            if Token.objects.get(key=token):
                return view(request, *args, **kwargs)

            raise http_401_unauthorized()

        return _view

    except Exception as e:
        raise e


def is_admin(view):
    try:

        @wraps(view)
        def _view(request, *args, **kwargs):

            token = request.headers["Authorization"].split()[-1]
            user = Token.objects.get(key=token).user

            if user.role != 1:
                raise http_401_unauthorized()

            return view(request, *args, **kwargs)

        return _view

    except Exception as e:
        raise e
