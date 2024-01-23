from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


def welcome(request):
    return render(request=request,
                  template_name='website/welcome.html',
                  context={
                      'message': 'This data was sent from the views to the template',
                      'num_meetings': Meeting.objects.count(),
                      'meetings': Meeting.objects.all()
                  })


def about(request):
    return HttpResponse('Copyright Tyson Solution')


def date(request):
    return HttpResponse(f'Server Clock: {datetime.now()}')
