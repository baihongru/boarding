from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# TODO：修改为自定义的职位类别
JOB_TYPE = [
    (0, '技术类'),
    (1, '产品运营类'),
    (2, '设计类'),
]

# TODO：修改为自定义的工作地点
CITIES = [
    (0 , '北京'),
    (1 , '上海'),
    (2 , '深圳'),
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JOB_TYPE, verbose_name='职位类别')
    job_name = models.CharField(blank=False, max_length=250, verbose_name='职位名称')
    job_city = models.SmallIntegerField(blank=False, choices=CITIES, verbose_name='工作地点')
    job_responsibility = models.TextField(max_length=1024, verbose_name='职位职责')
    job_requirement = models.TextField(blank=False, max_length=1024, verbose_name='职位要求')
    # 外键引用字段的默认值应该是引用的字段（默认是pk），而不是模型实例，因此在模型管理类中设置默认值
    # <https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#default>
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='创建人')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='修改日期')

    # 使用str()调用对象时返回一个人类可读的对象表示，例如在admin中
    # <https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#str>
    def __str__(self):
        return self.job_name

