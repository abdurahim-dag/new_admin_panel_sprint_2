from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from movies.models import FilmWork

"""
если значение page будет «абракадабра», то сервис вернёт ошибку валидации.
Передача параметра показывает, каким образом он передаётся — query, path или body:
если указан body, то параметр можно передать при использовании HTTP-методов POST, PUT, PATCH
"""

class MoviesListApi(BaseListView):
    model = FilmWork
    http_method_names = ['get']  # Список методов, которые реализует обработчик

    def get_queryset(self):
        return # Сформированный QuerySet

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'results': list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
