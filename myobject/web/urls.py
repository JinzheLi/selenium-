from django.urls import path
from .views import index

urlpatterns = [
    # 前台首页
    path('', index.index, name="index"),
]
