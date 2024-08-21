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
        #TODO F4키가 눌려질 경우 종료해버리기
        # if문을 통해서 시도해보았으나 keyboard 모듈 미인식 문제로 대기

        message = input(">> ")  # 사용자 입력 받기
        producer.send(topic, value={topic >> message})  # Kafka 토픽에 전송
        producer.flush()  # 메시지 전송 완료


    end = time.time()
    print("[DONE}:", end - start)
