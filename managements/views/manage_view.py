# -*- coding:utf-8 -*-
"""
@File       :   manage_view.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/4 18:37     Breeze      0.0.1       None     
"""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from managements.model_serializers.manage_serializers import ProjectSerializer
from managements.models.manage_model import ProjectModel


class ProjectView(viewsets.ModelViewSet):
    """
        list:
            查看所有项目
        create:
            添加新项目
    """
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailsView(viewsets.ModelViewSet):
    """
        retrieve:
            查询项目
        delete:
            删除项目
        update:
            更新项目
    """
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
