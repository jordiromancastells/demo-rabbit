
# Demo Servidor RabbitMQ

Introducción al servidor RabbitMQ

# Requisitos

1. Asumo que has leido la documentación básica de RabbitMQ https://www.rabbitmq.com/getstarted.html 

2. Se necesita python3 y la libreria Pika para poder ejecutar los ejemplos. Para instalar Pika:
```
pip3 install pika
```

4. El servidor de rabbitMQ esta dockerizado.

5. Si necesitas instalar docker o docker-compose: https://gitlab.com/snippets/1722766 o google ;)


# Servidor de RabbitMQ


## Arrancar el servidor de rabbitMQ

```
docker-compose up --build
```

En el servidor de rabbit está activado el plugin *rabbitmq_management*, proporciona una interfaz web para ver que sucede en el servidor

## Para acceder a la interfaz web

```
http://localhost:15672/
```

* usuario: jordi
* password: jordi

Estos datos estan definidos en el fichero **docker-compose.yml**, siempre los puedes cambiar.

## Para acceder a la consola: **rabbitmqctl**

En este caso, el servidor de rabbit está dockerizado, sino has cambiado el nombre del servicio en el docker-compose.yml puedes acceder mediante:

```
docker exec -it rabbitmq_rabbit-server_1 bash
```

En caso contrario, busca el identificador del contenedor, y substituye el nombre por el hash

Una vez dentro del contedor ya puedes invocar al comando rabbitmqctl

Doc oficual de rabbitmqctl: https://www.rabbitmq.com/rabbitmqctl.8.html

Para salir del contenedor, Ctrl+D o exit

# Clientes de rabbit en python3

Tutoriales de la web oficial (https://www.rabbitmq.com/getstarted.html) usando la libreria Pika. No estan dockerizados, para ejecutarlos, abre una terminal y lanza el script.

1. Son los ejemplos oficiales pero con algun pequeño cambio

2. Siempre arrancar el script consumidor o worker antes que el productor.


## Tutorial 1

Ejemplo oficial: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

**Objetivo:**

Poder enviar enviar información desde el productor al consumidor.

![](https://www.rabbitmq.com/img/tutorials/python-one-overall.png "Ejemplo 1")

### Ejecutar el ejemplo:
1. Situarse en el directorio *tutorial1*

2. Ejecutar el script consumidor:
```
python3 consumer.py
```

3. Ejecutar el script productor:
```
python3 producer.py
```

**Conclusión:**

Se ha podido enviar un mensaje, en este caso una cadena de texto desde el productor al consumidor. En el mundo real podria ser un conjunto de datos serializado, una imagen o cualquier cosa que necesites.

## Tutorial 2

Ejemplo oficial: https://www.rabbitmq.com/tutorials/tutorial-two-python.html

**Objetivo:**

Poder enviar una gran cantidad de mensajes desde el productor y con varios workers (consumidores) poder recibirlos.

![](https://www.rabbitmq.com/img/tutorials/python-two.png "Ejemplo 2")

### Ejecutar el ejemplo:

1. Situarse en el directorio *tutorial2*
2. En un terminal ejecutar el sctipt consumidor:
```
python3 worker.py
```
3. En otro terminal ejecutar otra vez el script consumidor como indica el punto 2

4. En otro terminal ejecutar el script productor
```
python3 producer.py
```

**Conclusión:**

El productor envia una gran cantidad de mensajes, y vemos como los mensajes son consumidos por los workers de forma repartida. 

Si se lanzan mas workers, cada worker tendrá que procesar menor cantidad de mensajes.

## Tutorial 3

Ejemplo oficial: https://www.rabbitmq.com/tutorials/tutorial-three-python.html

**Objetivo:**

Poder enviar los mismos mensajes desde un productor a varios consumidores.

![](https://www.rabbitmq.com/img/tutorials/python-three.png "Ejemplo 3")

### Ejecutar el ejemplo:

1. Situarse en el directorio *tutorial3*
2. Abrir varios terminales y ejecutar el consumdor en cada terminal
```
python3 consumer.py
```
3. En otro terminal ejecutar el productor
```
python3 producer.py
```

**Conclusión:**

El productor envia un mensaje y todos los consumidores reciben el mismo mensaje.