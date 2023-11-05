from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('albums', views.albums, name="albums"),
    path('albums/<int:id>', views.photos, name="album-photos"),  # Use a unique name
]
