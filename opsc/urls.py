from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('add<str:str_id>', views.add_host, name='add_host'),
    path('query_host/<str:query_str>/', views.query_host, name='query_host'),
]
