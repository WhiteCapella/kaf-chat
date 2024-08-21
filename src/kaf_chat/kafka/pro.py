from kafka import KafkaProducer

import keyboard
import time
import json

producer = KafkaProducer (
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x:json.dumps(x).encode('utf-8')
        )

start = time.time()
while(True):
    if keyboard.is_pressed('f4'):  # F4 키가 눌렸는지 확인
        break
    message = input(">>")  # 사용자 입력 받기
    producer.send('topic1', value={'message': message})  # Kafka 토픽에 전송
    producer.flush()  # 메시지 전송 완료


end = time.time()
print("[DONE}:", end - start)
