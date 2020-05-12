# celery_demo
celery异步任务和定时任务实现

### 启动worker
* celery -A celery_demo worker -l info

### #启动beta 调度器使用数据库
* celery -A celery_demo beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler