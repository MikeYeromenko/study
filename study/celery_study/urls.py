from django.urls import path

from celery_study import views

urlpatterns = [
    path('', views.index, name='index'),
]
