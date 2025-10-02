from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('videos/', views.VideoListView.as_view(), name='video_list'),
    path('music/', views.MusicListView.as_view(), name='music_list'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    # Add these newsletter routes
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('newsletter/subscribe/ajax/', views.newsletter_subscribe_ajax, name='newsletter_subscribe_ajax'),
]