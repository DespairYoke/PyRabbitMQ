import pika
#生产着
credentials = pika.PlainCredentials('guest','guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost',5672,'/',credentials
))
channel = connection.channel()

channel.queue_declare(queue='balance')

channel.basic_publish(exchange='',
                      routing_key='balance',
                      body='Hello World!')
print("Send 'helloword")
connection.close()