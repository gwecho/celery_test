from celery_tests import app

@app.task
def hello():
    return 'hello, world' 
