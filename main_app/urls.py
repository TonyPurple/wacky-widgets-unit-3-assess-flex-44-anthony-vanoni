from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('widgets/', views.create, name="create"),
  path('widgets/<int:widget_id>/', views.delete, name="delete"),
]