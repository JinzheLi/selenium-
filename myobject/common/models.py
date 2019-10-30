from django.db import models
from datetime import datetime


# Create your models here.
# 用户信息模型
class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id': self.id, 'username': self.username, 'name': self.name, 'password': self.password,
                'address': self.address, 'phone': self.phone, 'email': self.email, 'state': self.state}

    class Meta:
        db_table = "users"  # 更改表名


class Speeddate(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    download = models.CharField(max_length=50)
    upload = models.CharField(max_length=50)
    ping = models.CharField(max_length=50)
    server = models.TextField()
    timestamp = models.CharField(max_length=50)
    bytes_sent = models.CharField(max_length=100)
    bytes_received = models.CharField(max_length=100)
    share = models.CharField(max_length=50)
    client = models.TextField()

    def toDict(self):
        return {'id': self.id, 'download': self.download, 'upload': self.upload, 'ping': self.ping,
                'server': self.server, 'phone': self.timestamp, 'timestamp': self.timestamp,
                'bytes_sent': self.bytes_sent, 'bytes_received': self.bytes_received, 'share': self.share,
                'client': self.client}

    class Meta:
        db_table = "speeddate"  # 更改表名
