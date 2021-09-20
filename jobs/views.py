from django.shortcuts import get_object_or_404, render

from jobs.models import Job
from jobs.models import JOB_TYPE, CITIES

# Create your views here.

def rich_obj(obj):
    obj.city_name = CITIES[obj.job_city][1]
    obj.type_name = JOB_TYPE[obj.job_type][1]


# TODO：使用通用视图
def index(request):
    jobs = Job.objects.order_by('job_type')
    context = {'jobs': jobs}

    # TODO：当模型改变时将导致页面崩溃，需要将城市和类别变更为数据库字段，并添加合理的删除策略
    for job in jobs:
        rich_obj(job)
    
    return render(request, 'jobs/index.html', context)


def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    rich_obj(job)
    context = {'job': job}
    return render(request, 'jobs/job.html', context)