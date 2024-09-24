require 'bunny'

# Conexión con RabbitMQ
connection = Bunny.new(automatically_recover: false)
connection.start

# Crear un canal
channel = connection.create_channel

# Declarar la cola
queue_name = 'cola1'
queue = channel.queue(queue_name, durable: true)

# Mensaje a enviar
message = "Hello Word Ruby Publisher 1 =)"

# Publicar el mensaje en la cola
channel.default_exchange.publish(message, routing_key: queue.name)
puts " [x] Enviado '#{message}' a la cola '#{queue_name}'"

# Cerrar la conexión
connection.close