from kombu import Exchange, Queue

##mongo backend config
CELERY_RESULT_BACKEND = 'mongodb://127.0.0.1:27020/'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'database':'celery',
    'taskmeta_collection': 'celery_test_taskmeta_collection',
    'max_pool_size':10,
}

##celery default queue config
CELERY_DEFAULT_QUEUE = 'celery_default'
CELERY_DEFAULT_EXCHANGE = 'celery'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'

