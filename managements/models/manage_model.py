# -*- coding:utf-8 -*-
"""
@File       :   manage_model.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/3 17:47     Breeze      0.0.1       None     
"""
from django.db import models
import django.utils.timezone as timezone


class TestCaseModel(models.Model):
    id_ = models.IntegerField(auto_created=True, primary_key=True, db_index=True, name='id', verbose_name='用例ID')
    project_id = models.IntegerField(verbose_name='所属项目ID')
    module_name = models.CharField(max_length=20, verbose_name='模块名称')
    kit_name = models.CharField(max_length=20, verbose_name='套件名称')
    case_name = models.CharField(max_length=20, verbose_name='用例名称')
    case_status = models.IntegerField(max_length=2, verbose_name='用例状态（0：停用，1：启用）')
    create_auth = models.CharField(verbose_name='创建者')
    update_auth = models.CharField(verbose_name='修改者')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='修改时间')


class TestDataModel(models.Model):
    id_ = models.IntegerField(auto_created=True, primary_key=True, db_index=True, name='id', verbose_name='测试数据ID')
    test_case_id = models.IntegerField(verbose_name='测试用例ID')
    data_name = models.CharField(max_length=20, verbose_name='数据名称')
    init_data = models.TextField(verbose_name='初始化数据')
    test_data = models.TextField(verbose_name='测试数据')
    data_tag = models.IntegerField(max_length=2, verbose_name='数据标记（0：不处理，1：删除）')
    create_auth = models.CharField(verbose_name='创建者')
    update_auth = models.CharField(verbose_name='修改者')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='修改时间')


class UiElementModel(models.Model):
    id_ = models.IntegerField(auto_created=True, primary_key=True, db_index=True, name='id', verbose_name='元素ID')
    page_name = models.CharField(max_length=20, verbose_name='页面名称')
    ui_element_name = models.CharField(max_length=40, verbose_name='元素名称')
    ui_element_path = models.CharField(max_length=255, verbose_name='元素路径')
    create_auth = models.CharField(verbose_name='创建者')
    update_auth = models.CharField(verbose_name='修改者')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='修改时间')


class TestProjectModel(models.Model):
    id_ = models.IntegerField(auto_created=True, primary_key=True, db_index=True, name='id', verbose_name='项目ID')
    project_name = models.CharField(max_length=40, verbose_name='项目名称')
    project_status = models.IntegerField(max_length=2, verbose_name='项目状态(0：未开始，1：进行中，2：已完成，3：阻塞，4：关闭)')
    desc = models.TextField(verbose_name='项目描述')
    start_time = models.DateTimeField(verbose_name='项目开始时间')
    end_time = models.DateTimeField(max_length=2, verbose_name='项目结束时间')
    project_leader = models.CharField(max_length=40, verbose_name='项目负责人')
    create_auth = models.CharField(verbose_name='创建者')
    update_auth = models.CharField(verbose_name='修改者')
    create_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='修改时间')
