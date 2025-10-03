from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('videos/', views.VideoListView.as_view(), name='video_list'),
    path('music/', views.MusicListView.as_view(), name='music_list'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),

    # Newsletter
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('newsletter/subscribe/ajax/', views.newsletter_subscribe_ajax, name='newsletter_subscribe_ajax'),

    # Policy pages
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('contact/', views.contact, name='contact'),
]
