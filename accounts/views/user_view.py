# -*- coding:utf-8 -*-
"""
@File       :   user_view.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/3 11:55     Breeze      0.0.1       None     
"""
from rest_framework.views import APIView
from django.http import JsonResponse


class RegUserView(APIView):
    def post(self, request):
        result = {'code': 0, 'msg': 'OK'}
        return JsonResponse(result)
