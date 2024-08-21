from kafka import KafkaConsumer

import time
import json

def receive_message():
    topic = input("Enter Topic : ")
    receiver = KafkaConsumer(
            topic,
            bootstrap_servers='localhost:9092',
            )
    for message in receiver:
        decoded_message = message.value.decode('utf-8')  # 바이트 문자열 디코딩
        print(decoded_message)
