from kafka import KafkaConsumer

import time
import json

def receive_message():
    topic = input("Enter Chatroom : ")
    nickname = input("Enter Nickname : ")
    receiver = KafkaConsumer(
            bootstrap_servers='localhost:29092',
            auto_offset_reset='earliest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            )
    receiver.subscribe([topic])

    for message in receiver:
        data = message.value
        print(f"{data['nickname']} >> {data['message']}")

        


