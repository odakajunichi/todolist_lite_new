from django.contrib import admin

# Register your models here.
from .models import Post

#レコード表示機能
class PostAdmin(admin.ModelAdmin):
    list_display = ('message','created_date',)
    list_display_links = ('message','created_date',)

admin.site.register(Post,PostAdmin)