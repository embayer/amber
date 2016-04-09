# -*- coding: utf-8 -*-

#  Creation Date: 07.04.2015

from kombu import Exchange, Queue


# local url
# BROKER_URL = "redis://localhost:6379/0"
# boot2docker url
BROKER_URL = "redis://192.168.59.103:6379/0"
# docker-compose url
# BROKER_URL = "redis://broker:6379/0"

CELERY_QUEUES = (
    Queue("default_q", Exchange("default"), routing_key="default"),
    Queue("store_q", Exchange("media"), routing_key="media.store"),
    Queue("fetch_ikea_q", Exchange("media"), routing_key="media.fetch")
)

CELERY_DEFAULT_QUEUE = "default"
CELERY_DEFAULT_EXCHANGE_TYPE = "direct"
CELERY_DEFAULT_ROUTING_KEY = "default"

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT=["json"]
CELERY_TIMEZONE = "Europe/Berlin"
CELERY_ENABLE_UTC = True
# Optional configuration, see the application user guide.
CELERY_TASK_RESULT_EXPIRES = 3600
