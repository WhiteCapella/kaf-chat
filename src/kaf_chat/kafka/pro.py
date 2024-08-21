from kafka import KafkaProducer

import time
import json
def send_message():
    topic = input("Enter Topic : ")
    producer = KafkaProducer (
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x:json.dumps(x).encode('utf-8')
        )

    start = time.time()
    while(True):
        message = input(">> ")  # 사용자 입력 받기
        if message == "exit":
            break
        m_message = f'{topic} >> {message}'
        producer.send(topic, value=m_message)  # Kafka 토픽에 전송
        producer.flush()  # 메시지 전송 완료



    end = time.time()
    print("[DONE}:", end - start)
