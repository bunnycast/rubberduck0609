from django.contrib import admin
from .models import Snippet
from rest_framework import authtoken
# Register your models here.


class SnippetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'linenos', 'language', 'style', 'price')


admin.site.register(Snippet, SnippetsAdmin),
admin.register(authtoken)
