from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import ArtForm 
from .models import Art
AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.
def create_art(request):
     
    form = ArtForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        album = form.save(commit=False)
         
        album.picture = request.FILES['picture']
        file_type = album.picture.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'album': album,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'create_album.html', context)
        album.save()
         
        return render(request, 'arts/detail.html', {'album': album})
    context = {
        "form": form,
    }
    return render(request, 'create_album.html', context)

def art_view(request):
	 
    albums = Art.objects.filter()
    context  = {'albums': albums}
    return render(request, 'arts/index.html', context)

def detail_art(request,id):
    obj = Art.objects.get(id=id)
    context = {'album'  : obj}
    return render(request, "arts/detail.html",context)
