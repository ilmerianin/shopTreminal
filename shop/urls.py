#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 01:11:54 2022

@author: wasilii
"""

from . import views
from django.urls import include, re_path
from django.views.generic.base import RedirectView 

urlpatterns = [

    re_path(r'config', views.configS, name='config'), 
    re_path(r'^items/$', views.itemListView.as_view(), name = 'items'),
    re_path(r'^item_list/(?P<pk>\d+)$', views.itemDetalView.as_view(), name='item_detail'), #item_detail

    re_path(r'successCheck', views.subMit, name='submitet'),

    re_path(r'create-checkout-session', views.checkoutSess, name='checkoutSess'), 

    re_path(r'', views.indexItem, name='index'),  #
]  
        
       