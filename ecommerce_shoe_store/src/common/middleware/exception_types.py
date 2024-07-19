from rest_framework import status


class HandledException(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(self.message)


class NotFoundException(HandledException):

    def __init__(self, code=status.HTTP_404_NOT_FOUND, message='Resource Not Found'):
        super().__init__(code=code, message=message)


class MethodNotImplementedException(HandledException):
    def __init__(self, code=status.HTTP_405_METHOD_NOT_ALLOWED, message='Method Not Allowed'):
        super().__init__(code=code, message=message)


class BadRequestException(HandledException):
    def __init__(self, code=status.HTTP_400_BAD_REQUEST, message='Bad Request'):
        super().__init__(code=code, message=message)


class InvalidSerializationException(HandledException):
    def __init__(self, code=status.HTTP_400_BAD_REQUEST, message='Invalid Serialization'):
        super().__init__(code=code, message=message)


class ConflictException(HandledException):
    def __init__(self, code=status.HTTP_409_CONFLICT, message='Unexpected Conflict Occurred'):
        super().__init__(code=code, message=message)
