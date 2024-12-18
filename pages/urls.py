from django.urls import path
from .views import home
# ahhah
urlpatterns = [
      path("", home, name="root"),
      path("home/", home, name="home"),
]