from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('xxxx/', views.addTodo, name='addtodo'),
    path('complete/<todo_id>', views.completeTodo, name='completeTodo'),
    path('delete/<todo_id>', views.deleteTodo, name='deleteTodo'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('weather/', views.weather, name='weather'),
]