from django.http import JsonResponse
from app1 import tasks


# Create your views here.


def index(request, *args, **kwargs):
    res = tasks.add.delay(1, 8)
    # 任务逻辑
    return JsonResponse({'status': 'successful', 'task_id': res.task_id})
