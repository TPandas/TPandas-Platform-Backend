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

from managements.models.base_model import BaseModel


class CaseModel(BaseModel):
    """
    测试用例
    """
    id_ = models.AutoField(primary_key=True, db_index=True, name='id', verbose_name='用例ID')
    module_name = models.CharField(max_length=20, verbose_name='模块名称')
    kit_name = models.CharField(max_length=20, verbose_name='套件名称')
    case_name = models.CharField(max_length=20, verbose_name='用例名称')
    case_status = models.IntegerField(verbose_name='用例状态（0：停用，1：启用）')
    # 外键
    project = models.ForeignKey(to='ProjectModel', on_delete=models.CASCADE, verbose_name='所属项目')


class TestDataModel(BaseModel):
    """
    测试数据
    """
    id_ = models.AutoField(primary_key=True, db_index=True, name='id', verbose_name='测试数据ID')
    data_name = models.CharField(max_length=20, verbose_name='数据名称')
    test_data = models.TextField(verbose_name='测试数据')
    data_tag = models.IntegerField(verbose_name='数据标记（0：不处理，1：删除）')
    # 外键
    case = models.ForeignKey(to='CaseModel', on_delete=models.CASCADE, verbose_name='测试用例')
    env = models.ForeignKey(to='EnvModel', on_delete=models.CASCADE, verbose_name='项目环境')


class GlobalsDataModel(BaseModel):
    """
    公共环境参数
    """
    id_ = models.AutoField(primary_key=True, db_index=True, name='id', verbose_name='ID')
    field = models.CharField(max_length=40, verbose_name='Globals name')
    value = models.CharField(max_length=40, verbose_name='Globals value')
    # 外键
    env = models.ForeignKey(to='EnvModel', on_delete=models.CASCADE, verbose_name='项目环境')


class CaseDateModel(BaseModel):
    """
    用例与数据关联表
    """
    id_ = models.AutoField(primary_key=True, db_index=True, name='id', verbose_name='测试用例与测试数据关联表')
    test_case = models.ForeignKey(to='CaseModel', on_delete=models.CASCADE)
    test_data = models.ForeignKey(to='TestDataModel', on_delete=models.CASCADE)


class ByTypeModel(BaseModel):
    """
    页面元素类型
    """
    id_ = models.AutoField(primary_key=True, db_index=True, name='id', verbose_name='定位器类型ID')
    by_locator_type = models.CharField(max_length=40, verbose_name='定位器类型名称')


class PageObjectModel(BaseModel):
    """
    页面元素对象
    """
    id_ = models.AutoField(primary_key=True, db_index=True, name='id', verbose_name='元素ID')
    page_name = models.CharField(max_length=20, verbose_name='页面名称')
    model_name = models.CharField(max_length=20, verbose_name='功能模块名称')
    obj_name = models.CharField(max_length=40, verbose_name='元素名称')
    by_locator = models.CharField(max_length=255, verbose_name='元素定位器内容')
    # 外键
    by_type = models.ForeignKey(to='ByTypeModel', on_delete=models.CASCADE, verbose_name='定位类型')


class ProjectModel(BaseModel):
    """
    测试项目
    """
    id_ = models.AutoField(primary_key=True, db_index=True, name='id', verbose_name='项目ID')
    name = models.CharField(max_length=40, verbose_name='项目名称')
    status = models.IntegerField(verbose_name='项目状态(0：未开始，1：进行中，2：已完成，3：阻塞，4：关闭)')
    desc = models.TextField(verbose_name='项目描述')
    start_time = models.DateTimeField(verbose_name='项目开始时间')
    end_time = models.DateTimeField(verbose_name='项目结束时间')
    leader = models.CharField(max_length=40, verbose_name='项目负责人')


class EnvModel(BaseModel):
    """
    项目环境
    """
    id_ = models.AutoField(primary_key=True, db_index=True, name='id', verbose_name='环境ID')
    name = models.CharField(max_length=30, verbose_name='环境名称')
    desc = models.TextField(verbose_name='环境描述')
