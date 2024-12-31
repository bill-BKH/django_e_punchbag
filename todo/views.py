from django.shortcuts import render
from .models import Todo

# Create your views here.

def add(request):
    if request.method == 'POST':
        Text = request.POST.get('text')


        X = Todo(text = Text)
        

def show(request):
    if request.method == 'POST':
        text = request.POST.get('todo_text')
        date = request.POST.get('todo_date')
    return render(request, 'todo/show.html')
