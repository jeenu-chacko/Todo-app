from django.urls import path 
from . import views

urlpatterns = [
    path('', views.show_todo , name="show_notes"), 
    path('add/',views.AddTodo, name="todoform"),
    path('edit/<int:todo_id>',views.EditTodo, name="editform"),
    path('delete/<int:todo_id>',views.Delete, name="delete"),    
]
