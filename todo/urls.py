from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("erase/<int:tarea_id>/", views.erase, name="erase"),
    path("edit/<int:tarea_id>/", views.edit, name="edit"),
]