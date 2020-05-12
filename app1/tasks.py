from __future__ import absolute_import, unicode_literals

from datetime import datetime

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul():
    return datetime.now().strftime("%H:%M:%S")

