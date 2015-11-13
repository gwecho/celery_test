# celery_test
celery guide test

##start worker 
celery -A celery_tests worker -l info
celery -A celery_tests worker -l info -Q operation
celery -A celery_tests worker -l info -Q celery_default
celery -A celery_tests worker -l info -Q celery_default,operation

##sponsor app for test
python app/add.py
python app/hello.py


