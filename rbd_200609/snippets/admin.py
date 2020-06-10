from django.contrib import admin
from .models import Snippet

# Register your models here.


class SnippetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'linenos', 'language', 'style')


admin.site.register(Snippet, SnippetsAdmin)
