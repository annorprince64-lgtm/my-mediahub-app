from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Video, Music, Article, Picture, NewsletterSubscriber
import re


def home(request):
    context = {
        'recent_videos': Video.objects.filter(is_published=True).order_by('-created_at')[:6],
        'recent_music': Music.objects.filter(is_published=True).order_by('-created_at')[:6],
        'recent_articles': Article.objects.filter(is_published=True).order_by('-created_at')[:3],
        'featured_pictures': Picture.objects.filter(is_published=True).order_by('-created_at')[:6],
    }
    return render(request, 'index.html', context)


class VideoListView(ListView):
    model = Video
    template_name = 'content/video_list.html'
    context_object_name = 'videos'

    def get_queryset(self):
        return Video.objects.filter(is_published=True).order_by('-created_at')


class MusicListView(ListView):
    model = Music
    template_name = 'content/music_list.html'
    context_object_name = 'music_list'

    def get_queryset(self):
        return Music.objects.filter(is_published=True).order_by('-created_at')


class ArticleListView(ListView):
    model = Article
    template_name = 'content/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by('-created_at')


class GalleryView(ListView):
    model = Picture
    template_name = 'content/gallery.html'
    context_object_name = 'pictures'

    def get_queryset(self):
        return Picture.objects.filter(is_published=True).order_by('-created_at')


def newsletter_subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()

        # Basic email validation
        if not email:
            messages.error(request, "Please enter an email address.")
            return redirect('home')

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            messages.error(request, "Please enter a valid email address.")
            return redirect('home')

        try:
            # Check if email already exists
            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={'is_active': True}
            )

            if created:
                messages.success(request, "Successfully subscribed to our newsletter!")
            else:
                if subscriber.is_active:
                    messages.info(request, "You're already subscribed to our newsletter.")
                else:
                    subscriber.is_active = True
                    subscriber.save()
                    messages.success(request, "Successfully re-subscribed to our newsletter!")

        except Exception as e:
            messages.error(request, "An error occurred. Please try again.")

        return redirect('home')

    return redirect('home')


# AJAX version for better user experience
def newsletter_subscribe_ajax(request):
    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        email = request.POST.get('email', '').strip()

        # Basic email validation
        if not email:
            return JsonResponse({'success': False, 'message': 'Please enter an email address.'})

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            return JsonResponse({'success': False, 'message': 'Please enter a valid email address.'})

        try:
            # Check if email already exists
            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={'is_active': True}
            )

            if created:
                return JsonResponse({'success': True, 'message': 'Successfully subscribed to our newsletter!'})
            else:
                if subscriber.is_active:
                    return JsonResponse({'success': True, 'message': 'You\'re already subscribed to our newsletter.'})
                else:
                    subscriber.is_active = True
                    subscriber.save()
                    return JsonResponse({'success': True, 'message': 'Successfully re-subscribed to our newsletter!'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An error occurred. Please try again.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})