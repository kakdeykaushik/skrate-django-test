from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from .exceptions import http_409_conflict, http_500_internal_server_error


User = get_user_model()


@api_view(["POST"])
def create_user(request):
    try:
        username = request.POST.get("username")
        role = request.POST.get("role")

        new_user = User(username=username, role=role)
        new_user.save()

        token = Token.objects.create(user=new_user)
        return Response({"token": token.key})

    except ValidationError as e:
        print(str(e))
        raise http_409_conflict(message=e.message)

    except Exception as e:
        print(str(e))
        raise http_500_internal_server_error
