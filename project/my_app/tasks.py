from __future__ import absolute_import, unicode_literals
from celery import shared_task

from datetime import timedelta
from celery.task import periodic_task
from celery.schedules import crontab


@periodic_task(run_every=(timedelta(seconds=5)), name="my_first_task")
def my_first_task():
    print("This is my first task")
    return True


@shared_task
def my_second_task():
    print("This is my second task")
    return True


@shared_task
def my_third_task():
    print("This is my third task")
    return True


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)