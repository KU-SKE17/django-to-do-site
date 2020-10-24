from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
	path("", views.index, name="index"),
	path("add/", views.add_todo, name="add"),
	path('<int:todo_id>/done/', views.done_todo, name='done'),
]