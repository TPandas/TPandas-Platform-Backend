# -*- coding:utf-8 -*-
"""
@File       :   urls.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/3 11:49     Breeze      0.0.1       None     
"""
from django.urls import path, re_path

from managements.views import manage_view
from tpandas_backend.urls import router

# router.register(r'project', manage_view.ProjectView, basename='project')
# router.register(r'project_details', manage_view.ProjectDetailsView, basename='project_details')

urlpatterns = [
    path('project', manage_view.ProjectView.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'project_details/(?P<pk>\d+)/$', manage_view.ProjectDetailsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
