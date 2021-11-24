from django.urls import path
from . import views

urlpatterns = [
    path('edit', views.new, name='new'),
    path('', views.index, name = 'index'),
    path('delete/int:id/', views.delete, name ='delete')
]