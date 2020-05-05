# -*- coding:utf-8 -*-
"""
@File       :   urls.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/3 11:49     Breeze      0.0.1       None     
"""
from django.urls import path
from managements.views.manage_view import ProjectView

urlpatterns = [
    path('project', ProjectView.as_view()),
]
