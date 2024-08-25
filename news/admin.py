from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title","author","list_category","body","created"]




admin.site.register(models.Category)