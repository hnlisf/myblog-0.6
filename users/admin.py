#!/root/myenv1/bin python3.5
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
