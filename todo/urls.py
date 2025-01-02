from django.urls import path
from . import views
from .views import add,show,delete_task



urlpatterns = [
    path('',views.add),
    path('show/', views.show, name='show'),
    path('delete/<int:todo_id>/',delete_task,name='delete_task')
]
