from django.contrib import admin
from .models import Tag, Photos, Location, Category

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal =('tag',)

admin.site.register(Photos, PhotoAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Tag)

