from kafka import KafkaConsumer, KafkaProducer
from json import loads

import time
import threading

is_producer = False
server_add="172.17.0.1:9092"

def mode_receive(partner_topic):
    global is_producer
    global server_add

    consumer = KafkaConsumer(
            bootstrap_servers=server_add,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    consumer.subscribe([partner_topic])

    for message in consumer:
        print(f"Received message: {message.value}")
        if is_producer:  # Producer 모드로 전환되었으면 Consumer 종료
            break

def mode_send(my_topic):
    global is_producer
    global server_add
    
    producer = KafkaProducer(
        bootstrap_servers=server_add,
        value_serializer=lambda x:json.dumps(x).encode('utf-8'),
    )
    while is_producer:
        message = input(">> ")
        producer.send(my_topic, value=message)
        producer.flush()


def input_check():
    global is_producer

    while True:
        input()  # Enter 키 입력 대기
        is_producer = not is_producer

def make_chat():
    arg1 = input("Enter Your Nickname : ")
    arg2 = input("Enter Partner Nickname : ")

    consumer_thread = threading.Thread(target=mode_receive, args=(arg2,))
    producer_thread = threading.Thread(target=mode_send, args=(arg1,))
    input_thread = threading.Thread(target=input_check)

    consumer_thread.start()
    producer_thread.start()
    input_thread.start()

    consumer_thread.join()
    producer_thread.join()
    input_thread.join()

