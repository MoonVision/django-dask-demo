# django-dask-demo

Source code that goes along with the article here: https://medium.com/moonvision/using-django-with-dask-for-task-processing-73f4b903bf64. See article for full explanation.

## Setup

pip install -r requirements.txt

## Running

We will run everything from the demo folder. 

Start Django server:
```
python manage.py runserver
```

Start Dask Scheduler:
```
dask-scheduler
```

Start Dask Worker
```
dask-worker --preload daskworkerinit.py 127.0.0.1:8786
```
