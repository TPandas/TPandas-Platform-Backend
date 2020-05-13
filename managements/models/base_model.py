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


class BaseTimeModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        abstract = True
        verbose_name = '基础时间字段'
        # 减号代表倒序排列
        ordering = ['-update_time']


class BaseActionUserModel(models.Model):
    update_auth = models.ForeignKey(to='accounts.UserProfile', on_delete=models.CASCADE, verbose_name='修改者')
    create_auth = models.ForeignKey(to='accounts.UserProfile', on_delete=models.CASCADE, verbose_name='创建者')

    class Meta:
        abstract = True
        verbose_name = '操作用户字段'
