from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Photos, Location

# Create your views here.
def index(request):
    photos = Photos.todays_album()
    return render(request, 'index.html', {"photos": photos})

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        return render(request, 'search.html')
