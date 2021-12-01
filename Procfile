web: gunicorn app:app
worker: celery worker -A flaskr.tareas.tareas -l info -P threads