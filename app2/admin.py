from django.contrib import admin
from . import models
from .models import Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
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


admin.site.register(models.Post, PostAdmin)

