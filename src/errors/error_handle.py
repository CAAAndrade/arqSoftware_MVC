from src.views.http_types.http_response import HttpResponse
from src.errors.errors_type.http_bad_request import HttpBadRequest
from src.errors.errors_type.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.errors_type.http_not_found import HttpNotFound


def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequest, HttpUnprocessableEntity, HttpNotFound)):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )
    
    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Internal Server Error", "detail": str(error)}]},
    )
