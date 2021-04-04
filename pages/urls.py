# pages url patterns goes here
from django.urls import path
from .views import PagesView, BlogListView, BlogCreateView,\
    BlogUpdateView, BlogDeleteView

app_name = 'pages'

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('pages/<int:pk>/', PagesView.as_view(), name="detail"),
    path('pages/new/', BlogCreateView.as_view(), name='post_new'),
    path('pages/update/<int:pk>/', BlogUpdateView.as_view(), name='update_form'),
    path('pages/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_form'),
]