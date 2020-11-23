# Despliegue de sistemas predictivos
> Diplodatos 2019-2020
En este repositorio se incluye material para:
-Desplegar un servicio de análisis de sentimiento en contenedores Docker: API, redis, Módulo de Machine Learning.
-Desplegar de servicio de monitoreo: Graylog, grafana, elasticsearch, mongodb.
-Realizar tests funcionales, unitarios y de integración.
-Realizar stress test con Locust


## Sisema predictivo
El sistema predictivo está compuesto por una API que recibe como requests textos para ser analizados. Se comunica con un módulo de Machine Learning a través de una cola de mensajes implementada con Redis. Se orquestan los contenedores con docker-compose.
Asset 1: arquitectura

Instalar y ejecutar. Se accede a la interfaz web a través del puerto 80.
```
$ docker-compose up --build -d
```

Para detener los servicios:

```
$ docker-compose down
```

Para escalar un servicio:
```
docker-compose scale <módulo>=<workers>
```

## Tests
Se incluyen tests funcionales unitarios y de integración. Además, se disponibiliza Locust como herramienta de simulación de requests para ejecutar Stress tests.

Test funcionales
- Correr los tests en un container en con Python 3.5. Montar un volumen para ver los cambios dinámicamente

```
docker run -v ${pwd}:/src -it --net=host -w /src python:3.5 bash
pip install -r requirements.txt
nosetests [<package_name>]
```

Stress test.
- Instalar Locust. Correr con locust el locustfile.py. El shell informa el puerto del localhost desde el que se accede a la interfaz web. Loguearse con admin/admin.

```
pip install locust
locust -f stress_test/locustfile.py
```
Asset 3: charts de locust

## Sistema de monitoreo
Para el monitoreo del rendimiento del servicio, se utilizan Graylog y Grafana para hacer uso de sus herramientas de filtrado de requests, dashboards, alertas y demás; con mongodb y elasticsearch como bases de datos para autenticación y logging.
Asset 2: arquitectura de monitoreo

-Instalar y ejecutar. 

```
docker-compose -f docker-compose.yml.monitor up -d
```

-Acceder a Graylog: se accede a la interfaz web a través del puerto 9000. Para monitorear los mensajes es necesario declarar un input UDP GELF desde el menú de herramientas. Los resultados del análsis de sentimiento estan parseados en JSON, por lo que pueden aplicarse filtros al sentimiento y su score. Login: admin/admin
-Acceder a Grafana: se accede a la interfaz web a través del puerto 3000. Desde el menú de creación de dashboards se pueden configurar paneles de monitoreo con sus alarmas. Login: admin/admin.

Asset 4: dashboard grafana

