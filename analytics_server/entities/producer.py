from kombu import Queue, Exchange, Connection, Producer


class Publisher:
    def __init__(self, exchange_name, exchange_type, queue_name, routing_key):
        self.routing_key = routing_key
        self.channel = Connection(hostname='localhost', userid='guest', password='guest')
        self.exchange = Exchange(name=exchange_name, type=exchange_type, channel=self.channel)
        self.queue = Queue(name=queue_name, exchange=self.exchange, routing_key=routing_key)
        self.queue(self.channel).declare()

    def publish(self, payload):
        self.producer = Producer(self.channel, exchange=self.exchange, routing_key=self.routing_key)
        self.producer.publish(payload, serializer='json', compression='bzip2')
