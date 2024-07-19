from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'metadata': {
                'page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'total_results': self.page.paginator.count
            },
            'items': data
        })
