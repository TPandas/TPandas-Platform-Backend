# -*- coding:utf-8 -*-
"""
@File       :   manage_view.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/4 18:37     Breeze      0.0.1       None     
"""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from managements.model_serializers.manage_serializers import ProjectSerializer
from managements.models.manage_model import ProjectModel
from loguru import logger


class ProjectView(viewsets.ModelViewSet):
    """
        list:
            查看所有项目
        create:
            添加新项目
    """
    authentication_classes = ()
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        ret = {'code': 0, 'msg': None, 'data': None}
        try:
            page = self.paginate_queryset(self.queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                ret['msg'] = 'success'
                ret['data'] = serializer.data
                return self.get_paginated_response(ret)

        except Exception as ex:
            ret['code'] = -1
            ret['msg'] = '查询失败'
            logger.error(ex.__str__())


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
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
