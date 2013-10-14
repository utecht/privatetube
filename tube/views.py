from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from tube.models import Video, VideoForm

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        videos = Video.objects.all()
        return render(request, 'index.html', {'videos':videos})
    else:
        return render(request, 'logo.html')

def video(request, name):
    try:
        video = Video.objects.get(name=name)
    except:
        try:
            video = Video.objects.get(hidden=name)
        except:
            return redirect(index)
    print("found video: {}".format(video.vid.url))
    return render(request, 'video.html', {'video':video})

def upload(request):
    pass
