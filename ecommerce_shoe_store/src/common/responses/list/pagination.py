from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'total': self.page.paginator.count
            },
            'items': data
        })
