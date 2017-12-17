#!/root/myenv1/bin python3.5
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import register

app_name='users'

urlpatterns=[
    url('^register/$',register,name='register'),
]
