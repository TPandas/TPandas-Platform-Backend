# -*- coding:utf-8 -*-
"""
@File       :   user_model.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/3 15:48     Breeze      0.0.1       None     
"""
from django.db import models
import django.utils.timezone as timezone


class UserModel(models.Model):
    id_ = models.IntegerField(auto_created=True, primary_key=True, name='id')
    account = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='用户账号')
    user_name = models.CharField(max_length=40, verbose_name='用户名称')
    password = models.CharField(max_length=32, verbose_name='用户密码')
    group_id = models.IntegerField(max_length=4, verbose_name='分组ID')
    user_status = models.IntegerField(max_length=2, verbose_name='0：禁用，1：启用')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='更新时间')


class GroupModel(models.Model):
    id_ = models.IntegerField(auto_created=True, primary_key=True, name='id', db_index=True)
    group_name = models.CharField(max_length=20, unique=True, verbose_name='分组名称')
    desc = models.TextField(null=True, verbose_name='分组说明')
    group_status = models.IntegerField(max_length=2, verbose_name='分组状态(0：禁用，1：启用)')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='更新时间')


class AuthorityModel(models.Model):
    id_ = models.IntegerField(auto_created=True, primary_key=True, name='id', db_index=True)
    authority_name = models.CharField(max_length=20, unique=True, verbose_name='权限名称')
    authority_path = models.CharField(max_length=255, verbose_name='权限路径')
    authority_status = models.IntegerField(max_length=2, verbose_name='权限状态(0：禁用，1：启用)')
    desc = models.TextField(null=True, verbose_name='权限说明')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='更新时间')


class GroupAuthorityModel(models.Model):
    id_ = models.IntegerField(auto_created=True, primary_key=True, name='id', db_index=True)
    group_id = models.IntegerField(db_index=True, verbose_name='分组ID')
    authority_id = models.IntegerField(db_index=True, verbose_name='权限ID')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='更新时间')
