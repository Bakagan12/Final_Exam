from django.shortcuts import render

# Create your views here.

def gallery(request):
    # Assuming you have a list of image filenames in the static/images directory
    return render(request, 'gallery.html',)
