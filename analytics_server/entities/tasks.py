from celery import shared_task
from django_celery_beat.models import PeriodicTask
from entities import models
from entities.producer import Publisher


@shared_task
def data_migrate(task_name, model_name, exchange_name, queue_name, routing_key):
    try:
        task_obj = PeriodicTask.objects.get(name = task_name)
        model_cls = getattr(models, model_name)
        if task_obj.last_run_at is None:
            objs = model_cls.objects.all().values_list()
        else:
            objs = model_cls.objects.filter(modified__gte = task_obj.last_run_at).values_list()
        objs = list(objs)
        if objs:
            publisher_obj = Publisher(exchange_name, "topic", queue_name, routing_key)
            publisher_obj.publish(objs)
            print("Data Pushed To Queue")

    except AttributeError:
        pass