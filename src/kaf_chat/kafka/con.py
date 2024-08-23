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
    start_time = time.time()  # 시작 시간 기록
    timeout_seconds = 60  # 타임아웃 시간 (초)
    receiver.subscribe([topic])

    while True:
        # 1초 동안 메시지 폴링 (timeout_ms=100)
        messages = receiver.poll(timeout_ms=100)
        for message in receiver:
            data = message.value
            print(f"{data['nickname']} >> {data['message']}")
        # 60초 동안 메시지가 없으면 종료
            if time.time() - start_time > timeout_seconds:
                print("60초 동안 메시지가 수신되지 않아 종료합니다.")
                break

        


