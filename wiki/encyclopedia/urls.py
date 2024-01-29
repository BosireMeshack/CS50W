from django.urls import path

from . import views
# namespace


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="entry")
    
]
