from django.urls import path

from . import views

app_name = 'opsc'
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('forms.html', views.forms, name='forms'),
    path('tables.html', views.tables, name='tables'),
    path('table2html', views.table2, name='table2'),
    path('bootstrap-elements.html', views.bootstrap_elements, name='bootstrap_elements'),
    path('bootstrap-grid.html', views.bootstrap_grid, name='bootstrap_grid'),
    # path('add<str:str_id>', views.add_host, name='add_host'),
    path('query_host/<str:query_str>/', views.query_host, name='query_host'),
]
