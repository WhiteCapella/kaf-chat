from kafka import KafkaProducer

import time
import json

def receive_message():
    topic = input("Enter Topic : ")
    receiver = KafkaConsumer(
            topic
            )
    for message in receiver:
        print(message)
