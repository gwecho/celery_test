from basic_config import *

##celery queues config
CELERY_QUEUES = (
    Queue('celery_default', routing_key='celery_default'),
    Queue('operation', routing_key='operation'),
) 

##celery routers config
CELERY_ROUTES={
    'tasks.operation.add': {'queue':'operation', 'routing_key':'operation'},
    'tasks.operation.sub': {'queue':'operation', 'routing_key':'operation'},
    'tasks.operation.mul': {'queue':'operation', 'routing_key':'operation'},
    'tasks.operation.div': {'queue':'operation', 'routing_key':'operation'},
}

##tasks
CELERY_IMPORTS = ('tasks.operation', 'tasks.hello', )


