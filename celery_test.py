from celery import Celery

app = Celery('celery_tests', broker='amqp://testcelery:celery!!!!@127.0.0.1:5670//')
app.config_from_object('config')

