from django.shortcuts import render,redirect
from .models import Todo
from django.shortcut import get_object_or_404

# Create your views here.

def add(request):
    if request.method == 'POST':
        Text = request.POST.get('text')


        X = Todo(text = Text)
        

def show(request):
    tasks = Todo.objects.all()
    return render(request,'todo/show.html',{'tasks':tasks})

def delete_task(request,todo_id):
    todo = get_object_or_404(Todo,id=todo_id)
    todo.delete()
    return redirect('show')