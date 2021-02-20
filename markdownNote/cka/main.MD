课程 | 学习进度
--- | ---
[阿里巴巴云原生公开课](https://edu.aliyun.com/lesson_1651_13076) | N/A

---
### 第一讲 云原生生态

### 第二讲 容器基本概念
扩展阅读：
- linux namespace
- linux cgroup

扩展知识：
- dockerFile 打包工具链
- 容器三大件，进程、网络资源、文件系统，提供程序所需的运行时环境

总结：
- 容器是一个进程的集合，具有自己独特的视角；
- 镜像是容器所需的所有文件集合，剧本一次构建、到处运行的特点；
- 容器的生命周期和initial进程的生命周期一致；
- 容器与VM相比，各有优劣，容器技术需要加强的是隔离性和安全性；

### 第三讲 kubernetes
kubernetes的核心功能：
- 服务发现、负载均衡；
- 维持期望；
- 提供配置、密文管理；
- 自动发布与应用回滚；
- 弹性扩缩容；

kubernetes 服务端四大件：
- api-server
- controller
- scheduler
- etcd(持久化KV)

kubernetes 客户端二把刀：
- kubelet
- kube-proxy

核心概念：
- Pod
- Volume
- Deployment
- Service
- Namespace

### 第四讲 理解Pod和容器设计模式
容器设计模式：
- allin Container, 富容器；
- InitContainer， 原本需要在容器里通过ssh做的一些事情，通过 InitContainer 做掉；
- Sidecar 应用与日志收集， 业务容器将日志写在volume里，日志容器共享该volume将日志转发到远端存储，fluentd；
- Sidecar 代理模式， 代理容器对业务容器屏蔽被代理的服务集群，简化业务代码的实现罗技；
- Sidecar 适配器模式， 业务容器暴露出来的接口，通过适配器转换成 /healthz 以适配新的监控系统；

扩展阅读：
- [kubernetes patterns](https://www.redhat.com/cms/managed-files/cm-oreilly-kubernetes-patterns-ebook-f19824-201910-en.pdf)

### 第五讲 应用编排与管理：核心管理 [aliyun](https://edu.aliyun.com/lesson_1651_18353?spm=5176.10731542.0.0.479a20be6Odifn#_18353)
1. kubernetes资源对象： metadata（描述资源本身的信息）、Spec（描述期望的状态）、Status（描述观测到的状态）
2. labels
3. Selector
4. Annotations
5. Ownereference 所有者，指集合类的资源


控制器模式：
1. 控制循环：逻辑组件，控制器、被控制的系统、能够观测系统的传感器  
各组件独立自主的运行，不断使Status观测逼近Spec期望，类似于数学的逼近论；
2. Sensor：主要由Reflector、Informer、Indexer 三个组件构成  
Reflector 通过 List 和 Watch K8s server 来获取资源的数据  
Informer 组件不断地从 Delta 队列中弹出 delta 记录，然后把资源对象交给 indexer，让 indexer 把资源记录在一个缓存中，缓存在默认设置下是用资源的命名空间来做索引的，并且可以被 Controller Manager 或多个 Controller 所共享。  

API的选择，声明式 OR 命令式  
声明式（kubernetes的选择）
1. 天然地记录了状态
2. 幂等操作、可在任意时刻反复操作
3. 正常操作即巡检
4. 可合并多个变更

### 第六讲 应用编排与管理： Deployment
Deployment yaml字段描述
```yaml
apiVersion: apps/v1
kind:Deployment
metadata:
  KEY: VALUE
  ...
spec:
  replicas:
  RollingUpdate: // 升级策略
  selector:
    ...
  template:
    ...
  MinReadySeconds: // 一定要超过 MinReadySeconds 之后，才会判断为 available
  revisionHistoryLimit: // 保留历史 revision
  paused: // paused 是标识，Deployment 只做数量维持，不做新的发布，这里在 Debug 场景可能会用到
  progressDeadlineSeconds: // 当 Deployment 处于扩容或者发布状态时，它的 condition 会处于一个 processing 的状态，processing 可以设置一个超时时间。如果超过超时时间还处于 processing，那么 controller 将认为这个 Pod 会进入 failed 的状态
```

Depolyment管理模式
> Deployment -[Create]-> ReplicaSet -[Create]-> Pod -[OwnerRef]-> ReplicaSet -[OwnerRef]-> Deployment    
> 备注：Deployment 只负责管理不同版本的 ReplicaSet，由 ReplicaSet 来管理具体的 Pod 副本数，每个 ReplicaSet 对应 Deployment template 的一个版本。

升级策略字段解析：
> - MaxUnavailable: 滚动过程中最多有多少个 Pod 不可用，可以是百分比也可以是个数；
> - MaxSurge：滚动过程中最多存在多少个 Pod 超过预期 replicas 数量，可以是百分比也可以是个数；

### 第七讲 应用编排与管理：Job 和 DaemonSet
Job & CronJob  

DaemonSet编排
> - RollingUpdate，会一个一个的更新。先更新第一个 pod，然后老的 pod 被移除，通过健康检查之后再去见第二个 pod，这样对于业务上来说会比较平滑地升级，不会中断；
> - OnDelete，模板更新之后，pod 不会有任何变化，需要我们手动控制

DaemonSet 管理模式
> Daemonset -[Create]-> Pod -[OwnerRef]-> DaemonSet

### 第八讲 应用配置管理
要点
> 需求来源 -- ConfigMap -- Secret -- ServiceAccount -- Resource -- SecurityContext -- InitContainer

ConfigMap使用：
1. 环境变量。通过 valuesFrom ， ConfigMapKeyRef 域里 name 指定 ConfigMap名， key是ConfigMap.data 里的 key。容器启动后，通过env注入；
2. 命令行参数。 环境变量通过 cmd 字段拿到；
3. volume。 通过volume将ConfigMap.data 作为一个文件或者目录挂载到容器文件系统中；

ConfigMap注意点：
> 1. ConfigMap文件大小，小于1M；
> 2. Pod 引入 ConfigMap 的时候，必须是相同的 Namespace 中的 ConfigMap，前面其实可以看到，ConfigMap.metadata 里面是有 namespace 字段的；
> 3. pod 引用不存在的 ConfigMap 资源会导致 Pod 无法成功创建；
> 4. 只有通过 K8s api 创建的 pod 才能使用 ConfigMap 资源。

Secret 常用类型：
> 1. Opaque, 普通的Secret文件；
> 2. service-account-token， 用于 ServiceAccount 身份认证的 Secret；
> 3. dockerconfigjson，用于拉取私有仓库镜像使用的 Secret；
> 4. bootstrap.token，用于节点接入集群校验用的 Secret；

Secret 注意点：
> 1. Secret 文件大小限制 1M；
> 2. 除了采用 base64 编码， Secret 存储跟明文的 ConfigMap 区别不大；
> 3. Secret 读取的最佳实践，建议不要用 list/watch。因为 list/watch 方法会将 namespace 下所有的 Secret 遍历，太消耗系统资源；

Pod 服务质量（QoS）配置
> 1. Guaranteed，必须声明CPU和内存的request和limit；
> 2. Burstable，至少存在CPU和内存的一个request；
> 3. BestEffort，非以上两种的默认QoS级别；

SecurityContext：限制容器行为，保证系统和其他容器的安全。通过Linux内核的SecurityContext能力实现，分为三个级别：
> 1. 容器级别，只针对容器生效；
> 2. Pod级别，对Pod内所有容器生效；
> 3. Cluster级别，对集群内所有Pod生效（危险系数高，强烈不推荐）；

### 第十讲 应用存储和持久化数据卷：存储快照与拓扑调度 [aliyun_cncf_csi](https://edu.aliyun.com/lesson_1651_18383?spm=5176.10731542.0.0.5aed20be1RWHKY#_18383)
常见Pod Volumes类型：
- 本地存储，emptydir/hostpath;
- 网络存储，一种是in-tree，将实现代码放在k8s代码仓库中，随着k8s对存储类型支持的增多，该方式会对k8s本身维护和发展带来巨大负担；第二种是out-of-tree，与k8s解耦，通过抽象接口将不同存储的driver实现从k8三仓库中剥离（是社区主推的网络存储插件方式，CSI）
- Projected Volumes，将配置信息放在 configMap/secret 中，已卷的形式挂载至容器中
- PV与PVC方式

PV Spec 重要字段解析
- Capacity，存储对象的大小
- AccessModes， 单node读写访问，多node只读访问，多node读写访问
- ReclaimPolicy，Delete（PVC删除以后，PV也会删除），Retain（PVC删除以后，PV需要管理员手工处理）；
- StorageClassName，指定使用哪一个模板来生成PV；
- NodeAffinity，PV落点调度

PV&PVC处理流程：
> 1. 第一个阶段(Create阶段)是用户提交完 PVC，由 csi-provisioner 创建存储，并生成 PV 对象，之后 PV controller 将 PVC 及生成的 PV 对象做 bound，bound 之后，create 阶段就完成了；
> 2. 之后用户在提交 pod yaml 的时候，首先会被调度选中某一个 合适的node，等 pod 的运行 node 被选出来之后，会被 AD Controller watch 到 pod 选中的 node，它会去查找 pod 中使用了哪些 PV。然后它会生成一个内部的对象叫 VolumeAttachment 对象，从而去触发 csi-attacher去调用csi-controller-server 去做真正的 attache 操作，attach操作调到云存储厂商OpenAPI。这个 attach 操作就是将存储 attach到 pod 将会运行的 node 上面。第二个阶段 —— attach阶段完成；
> 3. 发生在kubelet 创建 pod的过程中，它在创建 pod 的过程中，首先要去做一个 mount，这里的 mount 操作是为了将已经attach到这个 node 上面那块盘，进一步 mount 到 pod 可以使用的一个具体路径，之后 kubelet 才开始创建并启动容器。这就是 PV 加 PVC 创建存储以及使用存储的第三个阶段 —— mount 阶段。

### 第十一讲 应用健康Liveness与Readiness
使用方式：
> - httpGet，通过HTTP Get方法请求，当返回HTTP状态码在 200 ~ 399 之间，认为应用健康；
> - Exec，执行容器中的一条命令，返回结果为0，认为容器健康；
> - tcpSocket， 通过容器的 IP.PORT 进行TCP健康检查，TCP建链成功，认为容器健康；

应用健康状态矩阵 - Liveness与Readiness总结
[] | Liveness（存活探针）| Readiness（就绪探针）
--- | --- | ---
介绍 | 用于判断容器是否存活，Pod状态是否为Running，如果Liveness探针判断容器不健康，会触发kubelet杀掉容器，并根据配置的策略判断是否重启容器，如果默认不配置Liveness探针，则认为默认返回值成功 | 用于判断容器是否启动完成，即PodCondition是否为Ready，如果探测结果不成功，则会将Pod从Endpoint中移除，直至下一次判断成功，再将Pod挂回Endpoint上
检测失败 | 杀掉Pod | 切断上层流量到Pod
使用场景 | 支持重新拉起的应用 | 启动后无法立即对外服务的应用

注意事项，选择合适的探测方式可以防止被误操作
> 1. 调大判断的超时阈值，防止在容器压力较高的情况下出现偶发超时
> 2. 调整判断次数阈值，3次的默认值在短周期下不一定是最佳实践
> 3. exec的如果执行的是shell脚本判断，在容器中可能调用时间非常的长，需要提前规划好debug方法
> 4. 使用tcpSocket的方式遇到TLS的场景，需要业务层判断是否有影响

### 监控与日志
从监控类型划分，分为四种类型:
1. 资源监控，像CPU/MEM/DISK/NETWORK/PROCESS等常规指标
2. 性能指标，通过APM监控获取的性能指标
3. 安全监控，针对安全维度的可靠性监控
4. 事件监控，日志以及event等

kubernetes监控接口标准
1. Resource Metrics，主要实现 metrics-server,提供对资源的监控
2. Custom Metrics，主要实现是Prometheus，对资源监控和自定义监控
3. External Metrics，external.metrics.k8s.io，对接云厂商的provider

Prometheus 可以跳过

#### 日志
主机内核的日志
> 1. 主机内核的日志，主机内核日志可以协助开发者进行一些常见的问题与诊断
> 2. 驱动异常，比较常见的是一些网络方案里面有的时候可能会出现驱动异常，或者说是类似 GPU 的一些场景，驱动异常可能是比较常见的一些错误
> 3. 文件系统异常, 容器文件系统异常，需要到容器运行时里可能才能看到
> 4. 内核里面的一些 kernel panic，或者是一些 OOM，这些也会在主机日志里面有相应的一些反映

Runtime 日志
> 比较常见的是 Docker 的一些日志，我们可以通过 docker 的日志来排查类似像删除一些 Pod Hang 这一系列的问题

核心组件日志
> K8s 里面核心组件包含了类似像一些外置的中间件，类似像 etcd，或者像一些内置的组件，类似像 API server、kube-scheduler、controller-manger、kubelet 等等这一系列的组件

应用日志
> 可以通过应用的日志来查看业务层的一个状态

### Kubernetes网络概念及策略控制
容器网络：
1. Underlay，与Host网络同层，不容器的IP地址不需要与Host网络取得协同（来自同一个中心分配或者统一划分），实现模型 calico
2. Overlay，实现模型 flannel
 
#### Network Policy的用处
注意事项
> 1. api-server需要开启 extensions/v1beta1/networkpolicies
> 2. 网络插件需要支持 Network Policy，如 calico，Romana，Weave Net和trieme等

三件事
1. 控制对象，通过Spec字段，podSelector等条件筛选；
2. 流方向： Ingress（入Pod流量） + from ， Egress（出Pod流量） + to
3. 流特征：对端（通过name/pod Selector), IP段（ibBlock），协议（protocol），端口（port）

### kubernetes Services

### 深入剖析Linux容器
docker容器三大件： cgroup + namespace + dockerImage  

#### namespace
1. mount，保证容器看到的文件系统的视图，提供容器内部的文件系统
2. uts，隔离 hostname 和 domain
3. pid，保证容器的 init 进程是以1号进程启动
4. network，除了容器使用 host 网络模式外，其他网络模式都有一个自己的 network namespace 文件
5. user，控制用户的 UID 和 GID 在容器内部和宿主机上的一个映射，不过这个 namespace 用的比较少
6. ipc，控制了进程间通信，比如信号量
7. cgroup，用 cgroup namespace 带来的一个好处是容器中看到的 cgroup 视图是以根的形式来呈现的，这样的话就和宿主机上面进程看到的 cgroup namespace 的一个视图方式是相同的。另外一个好处是让容器内部使用 cgroup 会变得更安全

#### cgroup
两种驱动
> 1. systemd cgroup driver, 个驱动是因为 systemd 本身可以提供一个 cgroup 管理方式。所以如果用 systemd 做 cgroup 驱动的话，所有的写 cgroup 操作都必须通过 systemd 的接口来完成，不能手动更改 cgroup 的文件。
> 2. cgroupfs cgroup driver, 比如说要限制内存是多少，要用 CPU share 为多少，其实直接把 pid 写入对应的一个 cgroup 文件，然后把对应需要限制的资源也写入相应的 memory cgroup 文件和 CPU 的 cgroup 文件

容器中常用的 cgroup
> - cpu cpuset cpuacct // CPU 一般会去设置 cpu share 和 cupset，控制 CPU 的使用率
> - memory // 控制进程内存的使用量
> - device // 控制了你可以在容器中看到的 device 设备
> - freezer // 当你停止容器的时候，freezer 会把当前的进程全部都写入 cgroup，然后把所有的进程都冻结掉，这样做的目的是，防止你在停止的时候，有进程会去做 fork。这样的话就相当于防止进程逃逸到宿主机上面去，是为安全考虑
> - blkio // 要是限制容器用到的磁盘的一些 IOPS 还有 bps 的速率限制,blkio 只能限制同步 io，docker io 是没办法限制的
> - pid // pid cgroup 限制的是容器里面可以用到的最大进程数量

不常用的 cgroup
> - net_cls
> - net_prio
> - hugetlb
> - perf_event
> - rdma

### 第十六讲 深入理解etcd - 基本原理解析
etcd是一个分布式的、可靠的 key-value 存储系统，用于存储分布式系统中的关键数据。  
通常由3个或者5个节点组成，通过 Raft 一致性算法完成分布式一致性协同，算法会选举一个主节点作为Leader，由Leader负责数据的同步与数据的分发。当Leader故障后，系统会自动选取另一个节点作为Leader，并重新完成数据的同步与分发。

#### Raft 算法 // TODO 因为比较复杂，感兴趣的可以看一下 Raft 对应的文档

#### etcd api 接口
分为5组
> - Put(key, value) / Delete(key, value)
> - Get(key) / Get(keyFrom, keyEnd)
> - Watch(key / keyPrefix)
> - Transactions(if / then / else ops).Commit()
> - Leases: Grant / Revoke / KeepAlive

### 第十七讲 etcd 性能优化实践 [aliyun_cncf_etcd](https://edu.aliyun.com/lesson_1651_18366)
性能优化维度
> - 硬件部署
> - 服务端软件优化
>> 1. 针对etcd的内存索引层优化：优化内部锁的使用，减少阻塞时间
>> 2. lease规模优化：优化 lease revoke和过期失效算法，将原来遍历失效list时间复杂度从 o(n) 降低为 o(logn)，解决lease规模化使用的问题
>> 3. boltdb 优化：将后端的 batch size limit/interval 进行调整，这样就能根据不同的硬件和工作负载进行动态配置，这些参数以前都是固定的保守值。
> - 客户端软件优化
>> 1. 针对于 Put 操作避免使用大 value，精简精简再精简，例如 K8s 下的 crd 使用；
>> 2. etcd 本身适用及存储一些不频繁变动的 key/value 元数据信息。客户端在使用上需要避免创建频繁变化的 key/value。例如 K8s下对于新的 node 节点的心跳数据上传就遵循了这一实践；
>> 3. 免创建大量的 lease，尽量选择复用。如在 K8s下，event 数据管理：相同 TTL 失效时间的 event 同样会选择类似的 lease 进行复用，而不是创建新的 lease。

### 第十八讲  Kubernetesdi调度和资源管理
k8s四大类基础资源：
1. CPU资源
2. memory资源
3. ephemeral-storage，临时存储资源
4. 通用扩展资源，如GPU/FPGA/RDMA/IFBAND等

#### kubernetes 高级调度能力
优先级调度和抢占(可以类比成linux的nice值)
> - Priority
> - Preemption


### 第二一讲 kubernetes存储架构及插件使用
动态存储模板，数据全挂载过程，全程分为6步
> 1. 用户创建一个包含PVC的Pod；
> 2. PV Controller不断观察 apiServer，如发现一个PVC已经创建完毕但仍然是未绑定的状态，它就会试图把一个 PV 和 PVC 绑定；
> 3. 通过 Scheduler 完成一个调度功能；
> 4. 如果有一个 Pod 调度到某个节点之后，它所定义的 PV 还没有被挂载（Attach），此时 AD Controller 就会调用 VolumePlugin，把远端的 Volume 挂载到目标节点中的设备上（如：/dev/vdb）;
> 5. Volum Manager 发现一个 Pod 调度到自己的节点上并且 Volume 已经完成了挂载，它就会执行 mount 操作，将本地设备（也就是刚才得到的 /dev/vdb）挂载到 Pod 在节点上的一个子目录中。同时它也可能会做一些像格式化、是否挂载到 GlobalPath 等这样的附加操作
> 6. 完成绑定；

kubernetes 存储架构：
- PV Controller: 负责 PV/PVC 的绑定、生命周期管理，并根据需求进行数据卷的 Provision/Delete 操作；
- AD Controller： 负责存储设备的 Attach/Detach 操作，将设备挂载到目标节点；
- Volume Manager： 管理卷的 Mount/Unmount 操作、卷设备的格式化以及挂载到一些公用目录上的操作；
- Volume Plugins：它主要是对上面所有挂载功能的实现。
- Scheduler： 实现对 Pod 的调度能力，会根据一些存储相关的的定义去做一些存储相关的调度
