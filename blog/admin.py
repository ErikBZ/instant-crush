from django.contrib import admin

from .models import Blog


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "pub_date"]
    class Meta:
        model = Blog

# Register your models here.
admin.site.register(Blog, BlogModelAdmin)
