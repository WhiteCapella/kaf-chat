import streamlit as st
import threading
import time
from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads

# Kafka 설정
KAFKA_TOPIC = 'chat-topic'
KAFKA_SERVER = '172.17.0.1:9092'

# Kafka Producer와 Consumer 생성 (초기화)
producer = None
consumer = None

# Kafka Producer 생성
@st.cache_resource
def create_producer():
    global producer
    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_SERVER],
            value_serializer=lambda x: dumps(x).encode('utf-8'),
            compression_type='snappy',
            batch_size=1
        )
        print("프로듀서 생성완료")
    return producer

# Kafka Consumer 생성
@st.cache_resource
def create_consumer():
    global consumer
    if consumer is None:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=[KAFKA_SERVER],
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            auto_offset_reset='latest',
            enable_auto_commit=False,
            group_id='chat-group'
        )
        print("컨수머 생성완료")
    return consumer

# 채팅 메시지를 Kafka에 전송
def send_message(producer, user_name, message):
    data = {"user": user_name, "message": message, "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')}
    producer.send(KAFKA_TOPIC, value=data)
    producer.flush()
    print("메시지 보내기 완료")

# Kafka 메시지를 스트리밍하여 Streamlit에 출력
def get_messages(consumer):
    messages = []
    for msg in consumer:
        messages.append(f"[{msg.value['timestamp']}] {msg.value['user']}: {msg.value['message']}")
        break  # Only get the latest message
    return messages

st.set_page_config(
    page_title='삼둘샵 사내 메신저'
)

st.title('삼둘샵 사내 메신저')

st.markdown('***')
st.markdown('**업무용 메신저 입니다**')

# 세션 상태 초기화
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = None
    print("닉네임 초기화")
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    print("메시지 초기화")

# 사용자 이름 입력 섹션
if st.session_state['user_name'] is None:
    user_name = st.text_input("사용하실 이름을 입력해주세요.")
    submit_button = st.button(label="확인")
    if submit_button and user_name:
        st.session_state['user_name'] = user_name
        consumer = create_consumer()
        get_messages(consumer)
else:
    # 채팅 입력 섹션
    st.write(f"안녕하세요, {st.session_state['user_name']}님!")
    message = st.chat_input("메시지를 입력하세요: ")
    if message:
        producer = create_producer()
        send_message(producer, st.session_state['user_name'], message)

        # 새 메시지를 가져와서 화면에 표시
        consumer = create_consumer()
        new_messages = get_messages(consumer)
        st.session_state['messages'].extend(new_messages)

        # 채팅 기록 표시
        st.markdown('### 채팅 기록')
        print("!!!!!!!!!!!!")
        print(new_messages)
        print(st.session_state['messages'])

        for chat_message in st.session_state['messages']:
            st.markdown(chat_message)
 
        print("!!!!!!!!!!!!")
