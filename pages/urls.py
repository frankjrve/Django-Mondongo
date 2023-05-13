from django.urls import path
from .views import HomePageView, MondongoPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("Mondongo/", MondongoPageView.as_view(), name="Mondongo"), 
]