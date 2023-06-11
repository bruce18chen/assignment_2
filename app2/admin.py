from django.contrib import admin
from . import models
from .models import Post, Comment, Topic

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'display_topics',
        'author',
        'status',
        'published',
        'created',
        'updated',
        'slug',
    )
    inlines = [
        CommentInline,
    ]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    def display_topics(self, obj):
        return ", ".join([topic.name for topic in obj.topics.all()])

    display_topics.short_description = 'Topics'


admin.site.register(models.Post, PostAdmin)

admin.site.register(Topic)
