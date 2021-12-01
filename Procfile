web: gunicorn app:app
worker: celery -A flaskr.tareas.tareas worker -l info -P threads