import pika
from ml.ml import RegressionModel

from db.db import add_result


class RabbitConsumer():
    host: str = 'rabbitmq'
    queue: str = 'model_computation'

    def callback(self, ch, method, properties, body):
        delivery_tag = method.delivery_tag
        result = RegressionModel().start_predictions()

        add_result(delivery_tag, float(result))

        #print(f'{delivery_tag}\n{result}')

    def consume(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)
        channel.basic_consume(queue=self.queue, on_message_callback=self.callback, auto_ack=True)
        print('Ожидание сообщений...')
        channel.start_consuming()


def main():
    RabbitConsumer().consume()


if __name__ == '__main__':
    main()