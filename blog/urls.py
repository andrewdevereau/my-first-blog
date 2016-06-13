# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:00:11 2016

@author: Andrew Devereau
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]