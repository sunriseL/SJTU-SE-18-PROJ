# 流处理模型报告 #
#
## 流处理模型与ETL特性对比 ##
### ETL：
###ETL，是英文 Extract-Transform-Load 的缩写，用来描述将数据从来源端经过抽取(extract)、转换(transform)、加载(load)至目的端的过程。
### 静态数据与批处理架构，充裕时间处理静态数据，实时性要求不高。
### 流处理模型：
### 数据规模庞大，往往达到ＰＢ级别；数据产生速度极快，可以达到 ＧＢ／ｓ级别；
### 处理过程往往会涉及到复杂的数学模型，需要提供强力的底层支持，以保证这些模型在海量、高速数据环境中可以高效工作；
### 数据的时效性很强，导致对数据处理过程的整体延迟要求非常苛刻，必须在秒级或更短的时间内得到结果，从而进一步作出反应．
	
### 优点:更关注实时性，响应时间短
### 缺点:吞吐量较差


## 比较主流流处理框架 ##
### Apache Storm
#### Storm 是一个分布式实时大数据处理系统，可以帮助我们方便地处理海量数据，具有高可靠、高容错、高扩展的特点。Strom 本身是无状态的，通过 ZooKeeper 管理分布式集群环境和集群状态。Storm是一个典型的Native Streaming系统并且提供了大量底层的操作接口。另外，Storm使用了Thrift来进行拓扑的定义，并且提供了大量其他语言的接口。

### Spark
#### Spark是一个非常流行的提供了类似于SparkSQL、Mlib这样内建的批处理框架的库，并且它也提供了 Spark Streaming这样优秀地流处理框架。Spark的运行环境提供了批处理功能，因此，Spark Streaming毫无疑问是实现了Micro-Batching机制。输入的数据流会被接收者分割创建为Micro-Batches，然后像其他 Spark任务一样进行处理。Spark 提供了 Java, Python 以及 Scala 接口。

### Samza
#### Samza最早是由LinkedIn提出的与Kafka协同工作的优秀地流解决方案，Samza已经是LinkedIn内部关键的基础设施之一。Samza重负依赖于Kafaka的基于日志的机制，二者结合地非常好。Samza提供了Compositional接口，并且也支持Scala。

### Trident
#### Trident 是一个基于Storm构建的上层的Micro-Batching系统，它简化了Storm的拓扑构建过程并且提供了类似于窗口、聚合以及状态管理等等没有被Storm原生支持的功能。另外，Storm是实现了至多一次的投递原则，而Trident实现了恰巧一次的投递原则。Trident 提供了 Java, Clojure 以及 Scala 接口。

## 流处理模式优点：
###1.强一致性：这保证流计算能和批处理平起平坐，强一致性必须是“只处理一次（exactly-onceprocessing）”。

###2.时间推理的工具：这一点让流计算超越批处理。在处理无穷的、无序的、事件—时间分布不均衡的数据时，好的时间推理工具对于流计算系统是极其重要的。现在越来越多的数据已经呈现出上面的这些特征，而现有的批处理系统（也包括几乎所有的流计算系统）都缺少必要的工具来应对这些特性带来的难题。

###3.弹性伸缩功能，即在保证Exactly-once 语义的情况下，流处理应用无需用户的介入也能自动修改并发数，实现应用的自动扩容和缩容。

###4.流上的SQL查询功能以及完整SQL支持，包含窗口，模式匹配等语法支持。

## 评价
### 流处理模式是面向动态数据的细粒度处理模式，这种模式的处理延迟最低，适合用于监控系统、在线金融分析、算法交易等对实时性要求较高的应用场景。此模式在面向动态数据的实时处理领域有着不可替代的地位。