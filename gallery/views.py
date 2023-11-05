from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, "home.html",{})

def photos(request):
    return render(request, "albums/photos.html",{})

def albums(request):
    image_data = [
        {
            'url': '/static/images/img1.jpg',
            'title': 'Image 1',
        },
        {
            'url': '/static/images/img2.jpg',
            'title': 'Image 2',
        },
        {
            'url': '/static/images/img3.jpg',
            'title': 'Image 3',
        },
        {
            'url': '/static/images/img4.jpg',
            'title': 'Image 4',
        },
        {
            'url': '/static/images/img5.jpg',
            'title': 'Image 5',
        },
        {
            'url': '/static/images/img6.jpg',
            'title': 'Image 6',
        },
        {
            'url': '/static/images/img7.jpg',
            'title': 'Image 7',
        },
        {
            'url': '/static/images/img8.jpg',
            'title': 'Image 8',
        },
        {
            'url': '/static/images/img9.jpeg',
            'title': 'Image 9',
        },
    ]
    context = {
        'photos': image_data,
    }
    
    return render(request, "albums/index.html",context)


# def photos(request, id):
#     albumsResponse = requests.get("https://jsonplaceholder.typicode.com/albums/" + str(id))

#     photosResponse = requests.get("https://jsonplaceholder.typicode.com/photos?albumId=" + str(id))
#     data = photosResponse.json()
#     albumData = albumsResponse.json();

#     context = {
#         'photos': data,
#         'album': albumData
#     }
#     return render(request, "albums/photos.html",context)
def photos(request):
    # Manually create a list of image data with file paths
    image_data = [
        {
            'url': '/static/images/img1.jpg',
            'title': 'Image 1',
        },
        {
            'url': '/static/images/img2.jpg',
            'title': 'Image 2',
        },
        {
            'url': '/static/images/img3.jpg',
            'title': 'Image 3',
        },
        {
            'url': '/static/images/img4.jpg',
            'title': 'Image 4',
        },
        {
            'url': '/static/images/img5.jpg',
            'title': 'Image 5',
        },
        {
            'url': '/static/images/img6.jpg',
            'title': 'Image 6',
        },
        {
            'url': '/static/images/img7.jpg',
            'title': 'Image 7',
        },
        {
            'url': '/static/images/img8.jpg',
            'title': 'Image 8',
        },
        {
            'url': '/static/images/img9.jpeg',
            'title': 'Image 9',
        },
        
    ]
    context = {
        'photos': image_data,
    }
    return render(request, "albums/photos.html", context)
