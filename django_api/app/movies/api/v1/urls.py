from django.urls import include, path
from movies.api.v1 import views

urlpatterns = [
  path('movies', views.MoviesListApi.as_view()),
]
