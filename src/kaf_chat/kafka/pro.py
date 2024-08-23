from kafka import KafkaProducer

import time
import json
def send_message():
    topic = input("Enter Chatroom : ")
    nickname = input("Enter Nickname : ")
    producer = KafkaProducer (
        bootstrap_servers=['localhost:29092'],
        value_serializer=lambda x:json.dumps(x).encode('utf-8'),
        )

    start = time.time()
    while(True):
        message = input(">> ")  # 사용자 입력 받기
        if message == "exit":
            break
        m_message = f'{nickname} >> {message}'
        producer.send(topic, value=m_message)
        producer.flush()  # 메시지 전송 완료



    end = time.time()
    print("[DONE}:", end - start)
