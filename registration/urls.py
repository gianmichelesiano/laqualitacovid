from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_form_list, name='simple_form_list'),
    path('registration/new/', views.registration_new, name='registration_new'),
]