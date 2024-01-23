from django.shortcuts import render, get_object_or_404
from meetings.models import Room


# Create your views here.
def room_list(request):
    return render(request=request,
                  template_name='rooms/room_list.html',
                  context={
                      'rooms': Room.objects.all()
                  })


def detail(request, id):
    return render(request=request,
                  template_name='rooms/detail.html',
                  context={
                      'room': get_object_or_404(Room, pk=id)
                  })

