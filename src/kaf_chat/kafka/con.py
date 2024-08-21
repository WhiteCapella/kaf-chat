from kafka import KafkaConsumer

import time
import json

def receive_message():
    topic = input("Enter Topic : ")
    receiver = KafkaConsumer(
            topic,
            bootstrap_servers='localhost:9092',
            )
    start_time = time.time()  # 시작 시간 기록
    timeout_seconds = 60  # 타임아웃 시간 (초)

    while True:
        # 1초 동안 메시지 폴링 (timeout_ms=100)
        messages = receiver.poll(timeout_ms=100)

        if messages:  # 메시지가 있으면 처리
            for message in messages.values():
                for msg in message:
                    decoded_message = msg.value.decode('utf-8')
                    print(decoded_message)
            start_time = time.time()  # 메시지 수신 시 시작 시간 갱신

        # 60초 동안 메시지가 없으면 종료
        if time.time() - start_time > timeout_seconds:
            print("60초 동안 메시지가 수신되지 않아 종료합니다.")
            break


