from django.http import JsonResponse
from rest_framework import status

from common.middleware.exception_types import HandledException


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):

        if isinstance(exception, HandledException):
            response_data = {'error': str(exception.message)}
            response = JsonResponse(data=response_data, status=exception.code,
                                    content_type='application/json')

        else:
            response = JsonResponse({'error': str(exception)},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                    content_type='application/json')
            print(exception)

        return response
