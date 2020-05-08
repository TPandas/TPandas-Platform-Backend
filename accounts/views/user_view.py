# -*- coding:utf-8 -*-
"""
@File       :   user_view.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/3 11:55     Breeze      0.0.1       None
"""
from django.http import JsonResponse
from rest_framework.views import APIView
from accounts.models.login_model import UserProfile
from utils.jwt_auth import create_token


class LoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        """ 用户登录 """
        user = request.data.get('username')
        obj = UserProfile.objects.filter(username=user).first()
        # 检测用户和密码是否正确，此处可以在数据进行校验。
        if obj:
            # 用户名和密码正确，给用户生成token并返回
            token = create_token({'username': user})
            return JsonResponse({'id': obj.id, 'username': user, 'token': token})
        return JsonResponse({'code': 0, 'msg': '用户名或密码错误'})


class RegUserView(APIView):
    def post(self, request):
        result = {'code': 0, 'msg': 'OK'}
        return JsonResponse(result)
