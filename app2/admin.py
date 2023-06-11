from django.contrib import admin
from .models import Post, Comment, Topic


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_on', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'comment')
    readonly_fields = ('name', 'email', 'comment')


admin.site.register(Comment, CommentAdmin)
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('name', 'email', 'comment')
    fields = ('name', 'email', 'comment', 'approved')



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
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    def display_topics(self, obj):
        return ", ".join([topic.name for topic in obj.topics.all()])

    display_topics.short_description = 'Topics'


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)









