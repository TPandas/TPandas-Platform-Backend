#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models.login_model import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
