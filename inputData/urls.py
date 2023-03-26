from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('leave_comment/', views.index,name = "leave_comment"),
    path("input/", views.input)
]