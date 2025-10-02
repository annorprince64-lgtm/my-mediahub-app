from django.contrib import admin
from .models import Category, Video, Music, Article, Picture, NewsletterSubscriber


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'is_published']
    list_filter = ['category', 'created_at', 'is_published']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Media Files', {
            'fields': ('video_file', 'thumbnail')
        }),
        ('Publication', {
            'fields': ('is_published', 'created_at', 'updated_at')
        }),
    )


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'category', 'created_at', 'is_published']
    list_filter = ['category', 'created_at', 'is_published']
    search_fields = ['title', 'artist', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'artist', 'description', 'category')
        }),
        ('Media Files', {
            'fields': ('audio_file', 'cover_image')
        }),
        ('Publication', {
            'fields': ('is_published', 'created_at')
        }),
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'is_published']
    list_filter = ['category', 'created_at', 'is_published']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'category')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Publication', {
            'fields': ('is_published', 'created_at', 'updated_at')
        }),
    )


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'is_published']
    list_filter = ['category', 'created_at', 'is_published']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Publication', {
            'fields': ('is_published', 'created_at')
        }),
    )


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']
    readonly_fields = ['subscribed_at']
    list_per_page = 20

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-subscribed_at')


# Customize admin site
admin.site.site_header = "Media Site Administration"
admin.site.site_title = "Media Site Admin"
admin.site.index_title = "Welcome to Media Site Admin Panel"