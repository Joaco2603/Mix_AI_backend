class CustomError(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code
        self.message = message

    @staticmethod
    def bad_request(message: str):
        return CustomError(400, message)

    @staticmethod
    def unauthorized(message: str):
        return CustomError(401, message)

    @staticmethod
    def forbidden(message: str):
        return CustomError(403, message)

    @staticmethod
    def not_found(message: str):
        return CustomError(404, message)

    @staticmethod
    def internal_server(message: str = 'Internal Server Error'):
        return CustomError(500, message)