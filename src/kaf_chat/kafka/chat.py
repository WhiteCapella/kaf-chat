from kafka import KafkaConsumer, KafkaProducer
from json import loads

import time
import threading

isproducer = False


def mode_receive(partner_topic):
    global is_producer

    consumer = KafkaConsumer(
        topic=partner_topic,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        print(f"Received message: {message.value}")
        if is_producer:  # Producer 모드로 전환되었으면 Consumer 종료
            break

def mode_send(my_topic):
    global is_producer

    producer = KafkaProducer(
        topic=my_topic,
        bootstrap_servers='localhost:9092',
        value_serializer=lambda x:json.dumps(x).encode('utf-8'),
    )
    while is_producer:
        message = input(">> ")
        producer.send(topic, value=message)
        producer.flush()


def input_check():
    global is_producer

    while True:
        input()  # Enter 키 입력 대기
        is_producer = not is_producer

if __name__ == "__main__":
    my_topic = input("Enter Your Nickname : ")
    partner_topic = input("Enter Partner Nickname : ")

    consumer_thread = threading.Thread(target=mode_receive, args=(partner_topic))
    producer_thread = threading.Thread(target=mode_send, args=(my_topic))
    input_thread = threading.Thread(target=input_check)

    consumer_thread.start()
    producer_thread.start()
    input_thread.start()

    consumer_thread.join()
    producer_thread.join()
    input_thread.join()
