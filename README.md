# Ejecución en AWS Entrega 2

## Asegurarse que las instancias Web Server, Worker y File Server están ejecutándose en AWS Academy Learner Lab

## Conexión a servidor NFS 

Ejecutar el siguiente comando en la instancia Worker y Web Server

```bash
sudo mount 172.31.17.66:/mnt/nfs_share  /mnt/nfs_clientshare
```
172.31.17.66 es actualmente la IP privada del EC2 que utilizamos como File Server

## Ejecución de API
En el Web Server ingresar a la carpeta Proyecto-Grupo16-2021 y ejecutar

```bash
source venv/bin/activate
gunicorn -w 4 --bind 0.0.0.0:8000 wsgi:app
```

## Ejecutar Celery
En la instancia del worker, ingresar a la carpeta Proyecto-Grupo16-2021/flaskr y ejecutar

```bash
source venv/bin/activate
```
Posteriormente regresar a la carpeta raíz del repositorio y ejecutar

```bash
celery -A flaskr.tareas.tareas worker -l info
```

## Pruebas de humo

Consultar dirección DNS ipv4 pública en la instancia del web server y realizar petición GET a la URL http://{{conversion-host}}/ping

Como respuesta deberíamos obtener

```bash
"Pong"
```

# Ejecución en máquina on-premise

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
