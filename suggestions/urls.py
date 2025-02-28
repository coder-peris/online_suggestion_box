from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_form, name='submit')
]
