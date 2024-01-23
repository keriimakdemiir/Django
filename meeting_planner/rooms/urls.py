
from django.urls import path
from rooms.views import room_list, detail

urlpatterns = [
    # http://127.0.0.1:8000/rooms/list
    path('list', room_list, name='rooms'),

    # http://127.0.0.1:8000/rooms/detail/1
    path('detail/<int:id>', detail, name='detail'),
]