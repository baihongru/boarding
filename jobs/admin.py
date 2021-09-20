from django.contrib import admin

from .models import Job

# Register your models here.

# 模型管理类
# <https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/#modeladmin-objects>
# <https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/#modeladmin-options>
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')
    exclude = ('creator', 'created_date', 'modified_date')

    # TODO：增加过滤器，时间、职位类型、职位地点

    # TODO：需要校验request中的用户是否存在于用户表中
    def save_model(self, request, obj, form, change) -> None:
        obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)