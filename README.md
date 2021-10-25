# Proyecto-Grupo16-202120

## Cargar requerimientos del proyecto

pip install -r requirements.txt

## Ejecución de cola de mensajería

Se requiere tener instalado redis y celery en la máquina virtual

```python
pip install redis
pip install celery
```

En la raíz del proyecto ejecutar el comando


```python
celery -A flaskr.tareas.tareas worker -l info -P solo
```

## Ejecución de app web

Para subir el servidor web de gunicorn ejecutar el siguiente comando

```python
gunicorn -w 4 --bind 0.0.0.0:8000 wsgi:app
```

## Probar aplicación

La app estará disponible para recibir peticiones en el puerto 8000
