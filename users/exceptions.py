from rest_framework.exceptions import APIException


def http_409_conflict(message="Conflict"):
    ex = APIException(code=409, detail=message)
    return ex


def http_500_internal_server_error(message="Internal Server Error."):
    ex = APIException(code=500, detail=message)
    return ex
