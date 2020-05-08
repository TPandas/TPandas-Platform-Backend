# -*- coding:utf-8 -*-
"""
@File       :   urls.py
@Contact    :   breeze.yang@tom.com
@Project    :   tpandas_backend

@Modify Time        @Author     @Version    @Desc
-----------------   ---------   ---------   ---------------------
2020/5/3 11:49     Breeze      0.0.1       None
"""
from django.conf.urls import url
from accounts.views import user_view
urlpatterns = [
    url("login/$", user_view.LoginView.as_view()),
]
