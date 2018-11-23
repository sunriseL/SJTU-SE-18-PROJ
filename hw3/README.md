## 网络及存储设置
### 网络测试
#### Test1
    使用www.speedtest.cn的在线测试工具对ping, upload, download, jitter进行测试
    测试结果如下
| - | 1 | 2 | 3 | avg |  
| :-:  | :-: | :-: | :-: | :-: |
|Ping|152.78|71.92|505.13|243.28|
|Download|74.17|93.56|94.65|87.46|
|Upload|69.32|99.74|100.15|89.74|
|Jitter|360.26|2.22|3476.76|1279.3|  
    使用了上海节点，但是显然测试结果很不稳定  

#### Test2
    使用www.speedtest.net的在线测试工具对ping, upload, download, jitter进行测试  
    结果如下
| - | 1 | 2 | 3 | avg |  
| :-:  | :-: | :-: | :-: | :-: |
|Ping|5|5|5|5|
|Download|92.33|92.11|92.75|92.34|
|Upload|91.45|92.41|90.85|91.57|
    结果比较稳定，虽然没有jitter的参数但是看速度曲线变化较小

### 存储测试
    使用windows内置的winsat disk进行性能测试
    测试结果如下
| - | 1 | 2 | 3 | avg |
| :-: | :-: | :-: | :-: | :-: |
| Random 16 Read | 153.18 | 164.52 | 160.62 | 159.44 |
| Sequential 64 Read | 369.54 | 362.06 | 386.37 | 372.65 |
| Sequential 64 Write | 513.62 | 513.93 | 513.73 | 513.76 |
| Delay 95% | 0.151 | 0.162 | 0.180 | 0.164 |
| Max Delay | 22.267 | 26.416 | 18.925 | 22.536 |


# Part C: Design an experiment to quantitive analyzing

## Test tool: kafka官方提供的kafka-perf工具
写入压力测试工具 kafka-producer-perf-test参数说明

| 参数 | 说明 |
| --------------- | ------------- |
| topic | topic名称 |
| num-records | 发送的消息数 |
| record-size |每个记录的字节数 |
| throughput | 每秒钟发送的记录数 |
| producer-props | 生产者的配置信息 |
| threads | 生产者使用几个线程同时发送 |

--------------------- 

消费压力测试工具 kafka-consumer-perf-test参数说明

| 参数 | 说明 |
| --------------- | ------------- |
| topic | topic名称 |
| fetch-size | 指定每次fetch的数据的大小 |
| messages |总共要消费的消息个数 |
| threads | 线程数 |
| producer-props | 生产者的配置信息 |
--------------------- 

### topic test2：3个分区，没有备份。

测试1: 50w条消息，每条消息大小1000，改变throughput，查看性能变化。

```bash
>kafka-topics.bat --create --zookeeper localhost:2181 --topic test1 --partitions 3 --replication-factor 1
```
throughput = 10000：
```bash
>kafka-producer-perf-test.bat --num-records 500000 --record-size 1000 --topic test1 --throughput 10000 --producer-props bootstrap.servers=*.*.*.*:9092
```
> 49992 records sent, 9996.4 records/sec (9.53 MB/sec), 1.3 ms avg latency, 134.0 max latency.</br>
50020 records sent, 10004.0 records/sec (9.54 MB/sec), 0.4 ms avg latency, 5.0 max latency. </br>
50030 records sent, 10004.0 records/sec (9.54 MB/sec), 0.4 ms avg latency, 4.0 max latency.</br>
50010 records sent, 9998.0 records/sec (9.53 MB/sec), 0.5 ms avg latency, 10.0 max latency.</br>
50050 records sent, 10006.0 records/sec (9.54 MB/sec), 0.5 ms avg latency, 26.0 max latency.</br>
50000 records sent, 10000.0 records/sec (9.54 MB/sec), 0.4 ms avg latency, 6.0 max latency.</br>
50050 records sent, 10004.0 records/sec (9.54 MB/sec), 58.2 ms avg latency, 737.0 max latency.</br>
50000 records sent, 10000.0 records/sec (9.54 MB/sec), 0.5 ms avg latency, 20.0 max latency.</br>
50030 records sent, 10006.0 records/sec (9.54 MB/sec), 123.2 ms avg latency, 1061.0 max latency.</br>
500000 records sent, 9998.800144 records/sec (9.54 MB/sec), 50.58 ms avg latency, 1662.00 ms max latency, 0 ms 50th, 404 ms 95th, 1278 ms 99th, 1617 ms 99.9th.

throughput = 20000：

> 100022 records sent, 19996.4 records/sec (19.07 MB/sec), 13.2 ms avg latency, 316.0 max latency.</br> 
100060 records sent, 20008.0 records/sec (19.08 MB/sec), 14.1 ms avg latency, 348.0 max latency.</br>
100020 records sent, 20004.0 records/sec (19.08 MB/sec), 30.8 ms avg latency, 501.0 max latency.</br>
100060 records sent, 20008.0 records/sec (19.08 MB/sec), 229.0 ms avg latency, 1397.0 max latency.</br>
500000 records sent, 19997.600288 records/sec (19.07 MB/sec), 57.52 ms avg latency, 1397.00 ms max latency, 0 ms 50th, 420 ms 95th, 1207 ms 99th, 1378 ms 99.9th.

throughput = 40000：

> 177050 records sent, 34777.1 records/sec (33.17 MB/sec), 100.0 ms avg latency, 756.0 max latency.</br>
226672 records sent, 45325.3 records/sec (43.23 MB/sec), 75.4 ms avg latency, 776.0 max latency.</br>
500000 records sent, 39987.204095 records/sec (38.13 MB/sec), 69.71 ms avg latency, 776.00 ms max latency, 1 ms 50th, 541 ms 95th, 721 ms 99th, 766 ms 99.9th.

throughput = 100000:
> 442284 records sent, 88456.8 records/sec (84.36 MB/sec), 194.7 ms avg latency, 666.0 max latency.</br>
500000 records sent, 89158.345221 records/sec (85.03 MB/sec), 222.05 ms avg latency, 666.00 ms max latency, 210 ms 50th, 604 ms 95th, 656 ms 99th, 664 ms 99.9th.

| num-record | record-size | messages/sec | MB/sec | avg latency | max latency |
| ---- | ---- |----|----|----|----|----|
|500000|1000|10000|9.54|50.58|1662.00|
|500000|1000|20000|19.07|57.52|1397.00|
|500000|1000|40000|38.13|69.71|776.00|
|500000|1000|100000|85.03|222.05|666.00|

测试2: 消息量与throughput不变，改变分区数partition，查看性能变化。

> replica = 1, num-record = 50w, record-size = 1000,  throughput = 20000

| partition | avg latency | max latency |
|---|---|---|
|1|1.19|162.00|
|3|28.03|1049.00|
|6|43.33|1091.00|

测试3：改变备份数，查看性能变化。

> partitions = 3, num-record = 50w, record-size = 1000,  throughput = 20000

test 4 =3

## 结果分析
- 
- 分区数越大，生产者的延迟时间越大 
## 1. Run Zookeeper
```bash
zookeeper-3.4.10\bin>zkServer.cmd
```
## 2.Run Kafka
```bash
kafka_2.12-2.0.0>"./bin/windows/kafka-server-start" "./config/server.properties"
```

## 3. Create a topic and Run Producer
```bash
kafka_2.12-2.0.0\bin\windows>kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
kafka_2.12-2.0.0\bin\windows>kafka-console-producer.bat --broker-list localhost:9092 --topic test
```

## 4. Run Consumer
```bash
kafka_2.12-2.0.0\bin\windows>kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test --from-beginning
```

