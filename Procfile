web: gunicorn app:app
worker: celery worker -A flaskr.tareas.tareas worker -l info -P threads