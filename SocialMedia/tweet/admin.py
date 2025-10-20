from django.contrib import admin
from .models import Tweet, Comment
# Register your models here.

class CommentAdmin(admin.TabularInline):
    model = Comment
    extra = 2

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime_created', 'datetime_updated', 'text')
    list_filter = ('user', )
    search_fields = ('user', 'text')
    readonly_fields = ('user', 'datetime_created', 'datetime_updated', 'text', 'image')
    inlines = (CommentAdmin, )

