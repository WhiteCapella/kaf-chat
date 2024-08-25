from kafka import KafkaConsumer, KafkaProducer

import json
import time
import threading

is_producer = False
server_add="localhost:9092"

def mode_receive(chatroom):
	global is_producer
	global server_add

	consumer = KafkaConsumer(
		bootstrap_servers=server_add,
		auto_offset_reset='latest',
		enable_auto_commit=True,
		value_deserializer=lambda x: json.loads(x.decode('utf-8'))
	)
	consumer.subscribe([chatroom])

	for message in consumer:
		data = message.value
		print(f"{data['nickname']} >> {data['message']} : {data['time']}")
		if is_producer:  # Producer 모드로 전환되었으면 Consumer 종료
			break


def mode_send(chatroom, nickname):
	global is_producer
	global server_add
    
	producer = KafkaProducer(
		bootstrap_servers=server_add,
		value_serializer=lambda x:json.dumps(x).encode('utf-8'),
	)
	while is_producer:
		message = input(">> ")
		if message == 'exit':
			producer.close()
		data = {'nickname':nickname, 'message':message, 'time':time.time()}
		producer.send(chatroom, value=data)
		producer.flush()


def input_check():
	global is_producer

	while True:
		input()  # Enter 키 입력 대기
		is_producer = not is_producer

def make_chat():
	nickname = input("Enter Your Nickname : ")
	chatroom = input("Enter Chatroom Name : ")

	consumer_thread = threading.Thread(target=mode_receive, args=(chatroom,))
	producer_thread = threading.Thread(target=mode_send, args=(chatroom, nickname,))
	input_thread = threading.Thread(target=input_check)

	consumer_thread.start()
	producer_thread.start()
	input_thread.start()

	consumer_thread.join()
	producer_thread.join()
	input_thread.join()

