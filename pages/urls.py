from django.urls import path
from .views import home, about
# ahhah
urlpatterns = [
      path("", home, name="root"),
      path("home/", home, name="home"),
      path("about/", about, name="about"),
]