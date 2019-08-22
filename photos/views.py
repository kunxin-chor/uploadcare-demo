from django.shortcuts import render, HttpResponse
from .forms import PhotoForm
from .models import Photo


# Create your views here.
def show_photos(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {
        'photos':photos
    })


def add_photo(request):
    if request.method == 'GET':
        form = PhotoForm()
        return render(request, 'add_photo.html',{
            'form' : form
        })
    else:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return HttpResponse("Photo saved")