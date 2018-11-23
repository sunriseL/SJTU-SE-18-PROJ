# -*- coding: utf-8 -*-
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='59.78.46.195:9092')

msg_dict = {
    "sleep_time": 1,

    "table": "msg",
    "msg": "Hello World"
}
msg = json.dumps(msg_dict).encode('utf-8')
for i in range(10):
    producer.send('test', msg, partition=0)
producer.close()