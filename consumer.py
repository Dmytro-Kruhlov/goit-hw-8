from connect import bd
from models import Users
from bson import ObjectId
import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")


def send_message(user_email, message):
    print(f"message: {message} has been sent to this email: {user_email}")


def callback(ch, method, properties, body):
    str_ob_id = body.decode()
    ob_id = ObjectId(str_ob_id)

    user = Users.objects.get(id=ob_id)
    user_email = user.email_address
    send_message(user_email, "Hello World")
    user.take_msg = True
    user.save()

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback)

channel.start_consuming()
