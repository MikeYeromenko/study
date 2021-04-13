from django.http import HttpResponse
from django.shortcuts import render

from celery_study.tasks import send_email


def index(request):
    result = 'successfully sent' if send_email.delay('some text...').result else 'failed'
    return HttpResponse(result)


def create_user(request):
    pass
