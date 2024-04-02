from django.contrib import admin
from .models import *
admin.site.register([BooksOwner])

class OwnerAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email']
    search_fields=['first_name','last_name','email']


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'get_categories')

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'

class CommentAdmin(admin.ModelAdmin):
    list_display=['id','comment_text','user']
    search_fields=['comment_text','user','stars_given']
    
admin.site.register(Owner,OwnerAdmin)
admin.site.register(Books,BookAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
