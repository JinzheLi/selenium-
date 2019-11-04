# -*- coding: utf-8 -*-
# coding: utf-8
from django.urls import path
from .views import index, users, type

urlpatterns = [
    # 后台首页
    path('', index.index, name='myadmin_index'),
    # 登录
    path('login', index.login, name="myadmin_login"),
    path('dologin', index.dologin, name="myadmin_dologin"),
    path('logout', index.logout, name="myadmin_logout"),
    path('verify', index.verify, name='myadmin_verify'),

    # 用户管理
    path('users/<int:pIndex>/', users.index, name='myadmin_users_index'),
    path('users/add', users.add, name='myadmin_users_add'),
    path('users/insert', users.insert, name='myadmin_users_insert'),
    path('users/del/<int:uid>/', users.delete, name='myadmin_users_del'),
    path('users/edit/<int:uid>/', users.edit, name='myadmin_users_edit'),
    path('users/update/<int:uid>/', users.update, name='myadmin_users_update'),
    path('users/resetpass/<int:uid>/', users.resetpass, name="myadmin_users_resetpass"),
    path('users/doresetpass/<int:uid>/', users.doresetpass, name="myadmin_users_doresetpass"),

    # 网速页面
    path('type/', type.index, name='myadmin_type_index')
]
