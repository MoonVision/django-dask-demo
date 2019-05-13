# django-dask-demo

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
