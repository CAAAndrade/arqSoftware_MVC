class HttpBadRequest(Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.name = "Bad Request"
        self.status_code = 400
        self.message = message