from django.contrib import admin

# Register your models here.
from django.contrib import admin
from accounts.models.login_model import UserProfile


class UserInfo(admin.ModelAdmin):
    search_fields = ('nick_name', 'username', 'phone')
    list_display = ('id', 'username', 'nick_name', 'phone')
    list_display_links = ('id', 'username')
    list_per_page = 20
    ordering = ('id',)
    list_filter = ('username',)
    fieldsets = ([
                     '用户信息', {
            'fields': ('username', 'password', 'phone', 'nick_name')
        }],)


admin.site.register(UserProfile, UserInfo)
