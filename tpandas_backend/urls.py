"""tpandas_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from managements.views.manage_view import ProjectView, ProjectDetailsView

router = routers.DefaultRouter()  # 创建路由对象
# router.register(r'project', ProjectView, basename='project')
# router.register(r'project_details', ProjectDetailsView, basename='project_details')

# 利用辅助函数引入所导入的两个类
schema_view = get_schema_view(
    openapi.Info(
        title="Tpandas API",
        default_version='v1.0',
        description="Tpandas项目接口文档",
        terms_of_service="#",
        contact=openapi.Contact(email="breeze.yang@tom.com"),
        license=openapi.License(name="Tpandas License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 配置django-rest-framework API路由
    path('accounts/', include('accounts.urls')),
    path('managements/', include('managements.urls')),
    path('runners/', include('runners.urls')),
    path('users/', include('accounts.urls')),
    path('api/', include(router.urls)),

    # 配置drf-yasg路由(Swagger)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view().without_ui(cache_timeout=0), name='Tpandas-json'),
    path('swagger', schema_view().with_ui('swagger', cache_timeout=0), name='Tpandas-swagger-ui'),
    path('docs/', schema_view().with_ui('redoc', cache_timeout=0), name='Tpandas-docs'),
]
