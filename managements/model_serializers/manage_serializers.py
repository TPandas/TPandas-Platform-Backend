# -*- coding:utf-8 -*-
"""
@File       :   manage_serializers.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/4 18:38     Breeze      0.0.1       None     
"""
from abc import ABC

from rest_framework import serializers
from managements.models.manage_model import ProjectModel


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'

    write_only_fields = ('name', 'status', 'desc', 'start_time', 'end_time', 'leader', 'create_auth', 'update_auth')
