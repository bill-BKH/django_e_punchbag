from django.urls import path
from . import views


urlpatterns = [
    path('',views.add_todo),
    path('show/', views.show, name='show'),
]
