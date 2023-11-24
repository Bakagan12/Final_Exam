from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('albums/', views.albums, name="albums"),
    path('aboutUs/', views.aboutus, name="aboutUs"),
    path('contactUs/', views.contactus, name="contactUs"),
    path('services/', views.service, name="services"),
    path('photos/<int:id>', views.photos, name="photos"),
    path('register', views.register_request, name="register"),
    path ("login", views.login_request, name="login"),
    path ("logout", views.logout_request, name="logout"),

]

