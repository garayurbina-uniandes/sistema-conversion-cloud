# Ejecución en AWS Entrega 5 Despliegue en PaaS

# Ejecución en AWS Entrega 4 Auto Scaling Background

## Asegurarse que los grupos de autoscaling tengan al menos una instancia aprovisionada, tanto el grupo del worker como el grupo de la capa web

El despliegue de los servicios se realiza automáticamente dentro de los grupos de auto-scaling

# Ejecución en AWS Entrega 3 Auto Scaling Web

## Asegurarse que la instancia Worker esté en ejecución y que el grupo de autoscaling tenga al menos una instancia aprovisionada

## Ejecución de API
Por defecto el script de arranque configurado en el grupo de autoscaling aprovisionará las instancias web con las dependencias necesarias y el código de la aplicación

## Montar Sistema de archivos S3 en Worker
En la instancia del worker, ejecutar el siguiente comando

```bash
mkdir /mnt/nfs_clientshare
sudo s3fs sistema-conversion-cloud-grupo-16 /mnt/nfs_clientshare -o iam_role=LabRole -o allow_other -o complement_stat,nonempty
chmod -R 777 /mnt/nfs_clientshare/files
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

Para probar que nuestra aplicación web se está ejecutando correctamente podemos ingresar a la URL 

http://Grupo-conversion-1-2079320198.us-east-1.elb.amazonaws.com:8000/ping

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
