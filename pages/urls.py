# pages url patterns goes here
from django.urls import path
from .views import HomePageView, AboutPage

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPage.as_view(), name="about"),
]