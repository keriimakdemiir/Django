from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)

    return render(
        request=request,
        template_name='meetings/detail.html',
        context={
            'meeting': meeting
        }
    )


def create(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm()

    return render(request=request,
                  template_name='meetings/create.html',
                  context={
                      'form': form
                  })