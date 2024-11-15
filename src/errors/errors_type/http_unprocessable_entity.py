class HttpUnprocessableEntity(Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.name = "Unprocessable Entity"
        self.status_code = 422
        self.message = message