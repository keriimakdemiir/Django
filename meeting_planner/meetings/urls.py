
from django.urls import path
from meetings.views import detail, create

urlpatterns = [
    # http://127.0.0.1:8000/meetings/detail/1
    path('detail/<int:id>', detail, name='detail'),

    # http://127.0.0.1:8000/meetings/create
    path('create', create, name='create'),
]