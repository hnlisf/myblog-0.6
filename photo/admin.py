#!/root/myenv1/bin python3.5
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import MyPhoto

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title','description','photo','photo_author','views']

admin.site.register(MyPhoto)

