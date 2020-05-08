#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=15, verbose_name="昵称", default="")
    phone = models.CharField(max_length=32, verbose_name="手机号码", null=True)

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name
