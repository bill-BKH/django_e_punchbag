from django.shortcuts import render
from .models import Todo

# Create your views here.

def add(request):
    if request.method == 'POST':
        Text = request.POST.get('text')


        X = Todo(text = Text)
        

def show(request):
    task = Todo.objects.all()
    return render(request, 'todo/show.html', {'task': task})