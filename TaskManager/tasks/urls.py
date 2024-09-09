from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/', views.complete_task, name='complete_task'),
    path('delete/', views.delete_task, name='delete_task'),
]