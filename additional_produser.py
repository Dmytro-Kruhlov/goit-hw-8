import pika
from models import Users

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.exchange_declare(exchange="sending", exchange_type='direct')
channel.queue_declare(queue='email_queue', durable=True)
channel.queue_bind(exchange='sending', queue='email_queue')
channel.queue_declare(queue='sms_queue', durable=True)
channel.queue_bind(exchange='sending', queue='sms_queue')

sms_contacts = Users.objects(preferred_contact_method="SMS")
email_contacts = Users.objects(preferred_contact_method="Email")

for user in sms_contacts:
    channel.basic_publish(
        exchange="sending",
        routing_key="sms_queue",
        body=str(user.id).encode()
    )


for user in email_contacts:
    channel.basic_publish(
        exchange="sending",
        routing_key="email_queue",
        body=str(user.id).encode()
    )


connection.close()
