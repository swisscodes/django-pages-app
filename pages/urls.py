# pages url patterns goes here
from django.urls import path
from .views import PagesView, BlogListView

app_name = 'pages'

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('pages/<int:pk>/', PagesView.as_view(), name="detail"),
]