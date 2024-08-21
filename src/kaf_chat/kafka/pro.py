from kafka import KafkaProducer

import time
import json
def send_message():
    group_id = input("Enter Chatroom : ")
    topic = f"chatroom_{group_id}"  # group_id에 따라 토픽 생성
    nickname = input("Enter Nickname : ")

    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    )

    start = time.time()
    while True:
        message = input(">> ")
        if message == "exit":
            break
        m_message = f'{nickname} >> {message}'
        producer.send(topic, value=m_message) 
        producer.flush() 


    end = time.time()
    print("[DONE}:", end - start)
