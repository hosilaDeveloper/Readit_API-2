from django.contrib import admin
from .models import About, Author, Tag, Category, HappyClients, Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category')
    list_display_links = ('id', 'title', 'author', 'category')
    search_fields = ('title', 'author')
    filter_horizontal = ('tags',)


admin.site.register(About)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(HappyClients)
admin.site.register(Comment)
