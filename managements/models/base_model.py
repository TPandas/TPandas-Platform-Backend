# -*- coding:utf-8 -*-
"""
@File       :   base_model.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/4 22:27     Breeze      0.0.1       None     
"""
from django.db import models


class BaseModel(models.Model):
    create_auth = models.CharField(max_length=20, verbose_name='创建者')
    update_auth = models.CharField(max_length=20, verbose_name='修改者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        abstract = True
        verbose_name = '公共字段'
