import pika
from bson import ObjectId
from models import Users
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue="email_queue", durable=True)




def process_sms_contact(user_id):
    user = Users.objects.get(id=user_id)

    print(f"Sending Email to {user.email_address}")


def callback(ch, method, properties, body):
    process_sms_contact(ObjectId(body.decode()))


channel.basic_consume(queue="email_queue", on_message_callback=callback, auto_ack=True)

channel.start_consuming()