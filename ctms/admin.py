from django.contrib import admin
from .models import photographer, categories, photos, BackgroundImage
# Register your models here.
admin.site.register(photographer)
admin.site.register(categories)
admin.site.register(photos)
admin.site.register(BackgroundImage)