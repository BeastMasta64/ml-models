#!/usr/bin/env python
from typing import Optional

import pika
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel


class RabbitConnection:
    _connection: Optional[BlockingConnection] = None
    _channel: Optional[BlockingChannel] = None
    #_exchange: AbstractRobustExchange | None = None

    def connect(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue='model_computation')

    def disconnect(self):
        self._connection.close()

    def _send_message(self, model_id):

        self._channel.basic_publish(exchange='', routing_key='model_computation', body=str(model_id))
        print(" [x] Sent 'Hello World!'")

rabbit_connection = RabbitConnection()