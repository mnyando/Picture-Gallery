from django.contrib import admin
from .models import Tag, Photos, Location, Category

# Register your models here.
admin.site.register(Photos)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Tag)

