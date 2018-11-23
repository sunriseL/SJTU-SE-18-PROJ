from kafka import KafkaConsumer

consumer = KafkaConsumer('test',  bootstrap_servers=['59.78.46.195:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)