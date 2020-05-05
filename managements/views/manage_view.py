# -*- coding:utf-8 -*-
"""
@File       :   manage_view.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/4 18:37     Breeze      0.0.1       None     
"""
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from managements.model_serializers.manage_serializers import ProjectSerializer
from managements.models.manage_model import ProjectModel


class ProjectView(APIView):
    def get(self, request):
        project_obj = ProjectModel.objects.all()
        serializer = ProjectSerializer(project_obj, many=True)
        return Response(serializer)

    def post(self, request):
        client_data = request.data
        verified_data = ProjectSerializer(data=client_data, many=False)

        if verified_data.is_valid():
            verified_data.save()
        else:
            return Response(verified_data.errors)
        return Response(verified_data.data)


class ProjectDetailedView(APIView):
    def get(self, request, pid):
        pass

    def post(self, request, pid):
        pass

    def put(self, request, pid):
        pass

    def delete(self, request, pid):
        pass
