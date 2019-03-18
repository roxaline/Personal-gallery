from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image, Category, Location



# Create your views here.
def index(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'index.html',{"images":images})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
        return render(request, 'search.html', {'message':message})

def display_images_categories(request):    
    images = Image.image_categories()

    return render(request, 'category.html', {"images":images}) 

def display_images_locations(request):    
    images = Image.image_locations()

    return render(request, 'location.html', {"images":images}) 