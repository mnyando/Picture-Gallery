from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Photos, Location

# Create your views here.
def index(request):
    photos = Photos.todays_album()
    locations = Location.objects.all()
    return render(request, 'index.html', {"photos": photos,"locations": locations})

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        return render(request, 'search.html')

def photos(request,photos_id):
    try:
        photos = Photos.objects.get(id = photos_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"photo.html", {"photos":photos})   

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    album = Photos.objects.filter(location = selected_location.id)
    return render(request, 'location.html', {"location":selected_location,"locations":locations,"album":album})
