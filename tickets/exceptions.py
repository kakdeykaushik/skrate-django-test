from rest_framework.exceptions import APIException


def http_401_unauthorized(message="Unauthorized"):
    ex = APIException(code=401, detail=message)
    return ex


def http_404_not_found(message="Not Found."):
    ex = APIException(code=404, detail=message)
    return ex


def http_409_conflict(message="Conflict"):
    ex = APIException(code=409, detail=message)
    return ex


def http_500_internal_server_error(message="Internal Server Error."):
    ex = APIException(code=500, detail=message)
    return ex
