from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from tube.models import Video, VideoForm

# Create your views here.
@login_required
def index(request):
    videos = Video.objects.all()
    return render(request, 'index.html', {'videos':videos})

def video(request, name):
    try:
        video = Video.objects.get(name=name)
    except:
        try:
            video = Video.objects.get(hidden=name)
        except:
            return HttpResponse("<html><body>No video found :(</body></html>")
    return render(request, 'video.html', {'video':video})

def upload(request):
    pass
