from django.contrib import admin

from .models import Comment, Review, User


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'text', 'score', 'pub_date')
    search_fields = ('pk', 'title', 'author', 'pub_date',)
    list_filter = ('pub_date','score')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'text', 'author', 'pub_date')
    search_fields = ('review', 'author', 'pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User)
