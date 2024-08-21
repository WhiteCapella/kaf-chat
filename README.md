# kaf-chat

## Introduce
이 레포지토리는 Kafka-python을 이용하여 메세지 송수신 기능을 구현한 레포지토리입니다.

## Installation

### Requirement Version
본 레포지토리는 Python 3.8이상을 요구하고 있습니다.

### Repository Instaillation
설치시 아래 코드를 이용하여 주십시오.

```bash
$ git clone https://github.com/WhiteCapella/kaf-chat.git
```

설치 후, 가상환경 세팅을 위해 다음을 실행하여 주십시오.

```bash
$ source .venv/bin/activate
```

가상환경 설치가 끝나면 pip 모듈을 설치합니다.
```bash
$ pip install .
```

### Kafka Setting
kafka를 준비해야합니다.
kafka를 설치한 위치에서 다음과 같이 진행하여 주십시오.

```bash
$ bin/kafka-server-start.sh config/server.properties
```

## Usage

본 레포지토리는 3개의 실행가능한 함수가 구현되어있습니다.
- kchat-ping
- kchat-s
- kchat-r

## kchat-ping

정상설치여부 확인을 위한 테스트 함수로 아래와 같이 입력하면 pong 단어를 출력합니다.

```bash
$ kchat-ping
pong
```

## kchat-s

해당 함수를 입력시 메세지 송신모드로 전환되며 메세지를 전달할 수 있습니다.
첫 입력시 topic을 입력받습니다.
```
Enter Topic : <Your Topic>
```

Topic을 입력하게 되면 메세지 송신창으로 전환됩니다.

```
>> <Your Message>
```

## kchat-r

해당 함수를 입력시 메세지 수신모드로 전환되며 메세지를 수신 할 수 있습니다.
첫 입력시 topic을 입력받습니다.
```
Enter Topic : <Your Topic>
```

Topic을 입력하게 되면 메세지 수신창으로 전환됩니다.

```
Enter Topic : <Your Topic>
"<Your Topic> >> <Your Message>"
```

![image](https://github.com/user-attachments/assets/c83f8ac1-497e-4300-9df8-755ed9dfe862)


