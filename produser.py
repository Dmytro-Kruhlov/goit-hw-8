from faker import Faker
import random
from models import Users

import pika


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_exchange', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_exchange', queue='task_queue')

fake = Faker()
contact_method = ["SMS", "Email"]
for _ in range(10):
    user = Users(
        fullname=fake.name(),
        email_address=fake.email(),
        phone_number=fake.phone_number(),
        preferred_contact_method=random.choice(contact_method)
    )
    user.save()
    ob_id = str(user.id)

    channel.basic_publish(
        exchange='task_exchange',
        routing_key='task_queue',
        body=ob_id.encode(),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))

    print(" [x] Sent %r" % ob_id)

connection.close()
