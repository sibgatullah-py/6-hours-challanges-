from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add'),
    path('edit/<int:task_id>/', views.edit_task, name='edit')
]
