#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@File       :   pagination.py
@Contact    :   breeze.yang.tech@linkkt.one
@Project    :   TPandas-Platform-Backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/13 16:15     Breeze      0.0.1       None     
"""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
import math


class TpCustomPagination(PageNumberPagination):
    """
    数据分页
    """
    # page_size = 100

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        page_size = api_settings.PAGE_SIZE or self.page_size
        total_page = math.ceil(count / page_size)
        return Response({
            'code': data['code'],
            'msg': data['msg'],
            'count': count,
            'total_page': total_page,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data['data']
        })
