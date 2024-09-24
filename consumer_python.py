import pika
import logging
import time

# Configurar logging (similar a @Slf4j en Java)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de la conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declarar la cola (esto debería estar configurado igual que en tu configuración de Spring)
queue_name = 'cola1'
channel.queue_declare(queue=queue_name, durable = True)

# Función que simula un proceso lento
def make_slow():
    try:
        time.sleep(5)  # Espera 5 segundos
    except Exception as e:
        logger.error(f"Error al dormir el hilo: {e}")

# Función callback que procesa el mensaje
def callback(ch, method, properties, body):
    message = body.decode('utf-8')  # Decodificar el mensaje
    logger.info(f"Received message {message}")
    make_slow()

# Consumir mensajes de la cola
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

logger.info('Esperando mensajes. Presiona CTRL+C para salir.')
channel.start_consuming()
