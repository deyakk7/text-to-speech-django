from django.contrib import admin

from .models import Storage, Language

class StorageAdmin(admin.ModelAdmin):
    list_display = ('title', 'lang', 'slug')
    list_filter = ('lang',)
    readonly_fields = ('text', 'lang', 'title_small', 'created_at', 'slug', 'audio')

admin.site.register(Storage, StorageAdmin)


admin.site.register(Language)