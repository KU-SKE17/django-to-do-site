from django.http import HttpResponse, HttpResponseNotFound
# Model.DoesNotExist is subclass of ObjectDoesNotExist
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import  reverse
from django.views import generic
from todo.models import Todo
from todo.forms import TodoForm

# function-based views
def index(request):
	"""Return a list of current todo tasks with a form for adding a new todo"""
	todo_list = Todo.objects.filter(done=False)
	form = TodoForm()
	context = {'form': form, 'todo_list': todo_list}
	return render(request, 'todo/todo_list.html', context)

def add_todo(request):
	"""Add a new todo. Should be invoked via POST method."""
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			# should log the action
			form.save()
			messages.success(request, 
				f"Added \"{request.POST['description']}\"" )
			return redirect('todo:index')
	else:  # GET /add/ should be handled by the main index
		return redirect('todo:index')
	return render(request, 'todo/add.html', {'form': form})


def done_todo(request, todo_id: int):
	"""Mark a todo as done, then redirect back to the index page."""
	try:
		todo = Todo.objects.get(id=todo_id)
	except ObjectDoesNotExist:
		return HttpResponseNotFound(f"<h2>Todo number {todo_id} not found</h2>")
	except Exception as e:
		# treat anything else as server-side error
		return HttpResponse(f"<h2>Error - {str(e)}</h2>", status=500)
	todo.done = True
	todo.save()
	messages.success(request, f"Todo {todo.id} marked as done")
	return redirect('todo:index')
