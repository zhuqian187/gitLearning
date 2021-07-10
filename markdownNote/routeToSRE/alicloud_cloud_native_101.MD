#### k8s日志系统

- 选择日志等级
- 日志内容规范
- 合理控制日志输出
- 选择多种日志输出目标
- 控制日志性能消耗
- 如何选择日志库
- 日志形态选择
- 日志是否落盘以及落盘介质
- 如何保证日志存储周期

##### 日志等级

| 日志等级     | 描述                                                         | 建议                             |
| ------------ | ------------------------------------------------------------ | -------------------------------- |
| FATAL(致命)  | 来输出非常严重或预期中不会发生的错误，遇到此种错误应当立即报警并人工介 入处理; | 一定是非常严重的错误需要人工处理 |
| ERROR (错误) | 非预期中的错误，此种错误可能导致部分系统异常但不会影响核心业务和系统正 常运行; | 告警维度：ERROR一般需要告警      |
| WARN(警告)   | 潜在的危险或值得关注的信息(比较核心的路径);                  | 告警维度：不需要告警，一般常开   |
| INFO(信息)   | 应用执行过程中的详细信息，一般通过该信息可以看到每个请求的主要执行过程; | 一般常开                         |
| DEBUG(调试)  | 用于线下调试的日志信息，用于分析应用执行逻辑，线上应用切勿开启; | 可以多打，方便分析问题           |
| TRACE(跟踪)  | 输出最细致的运行轨迹，可能包含涉及的数据内容                 |                                  |

##### 日志注意事项

- 所有用户请求日志，必须记录；
- 对于不确定的外部系统调用，日志需尽可能覆盖周全；
- 程序中的日志库需要具备运行期间变更日志等级的能力，方便在遇到问题需要分析时临时更改日志 等级；
- 通常在新功能上线，涉及的日志可适当提升一个等级，方便实时观察和监控，待稳定后再调整到正常(记得加上注释，方便改回来)；

#### 发布工程

注意点： ingress-nginx extension/v1beta1 ingress/annotations/(nginx.ingress.kubernetes.io/service-weight)

#### Helm V3

特性：

1. 移除了 Tiller
   - Helm 使用了与 kubectl 上下文相同的访问权限；
   - 无需使用 helm init 来初始化 helm；
   - Release Name 位于 namespace 中；
2. 分布式仓库以及 Helm Hub
   - 预定义的中心仓库被移除；
   - Helm Hub(一个发现分布式 chart 仓库的平台)被添加到 helm search；
3. JSON Schema 验证
4. Helm 测试
5. 命令行语法

helm 按照以下的顺序安装 k8s 资源。

有点意思的特性：

1. 自动滚动部署。[sha256sum](https://helm.sh/zh/docs/howto/charts_tips_and_tricks/) 方法保证在另一个文件发生更改时更新负载说明；
2. 建议遵循 [SemiVersion](https://github.com/Masterminds/semver) 规范；
3. 如果期待，使用 helm dependencies，大概率需要一个中心端的 charts repo 仓库，将 charts 放置在中心端的仓库里，进行援引，不过，需要考虑的是，依赖 charts 的环境参数配置注入的问题，子 charts values 也许可以搞定这个事情，但是需要验证；

helm 期待的目录结构：

```
wordpress/
  Chart.yaml          # 包含了chart信息的YAML文件
  LICENSE             # 可选: 包含chart许可证的纯文本文件
  README.md           # 可选: 可读的README文件
  values.yaml         # chart 默认的配置值
  values.schema.json  # 可选: 一个使用JSON结构的values.yaml文件
  charts/             # 包含chart依赖的其他chart
  crds/               # 自定义资源的定义
  templates/          # 模板目录， 当和values 结合时，可生成有效的Kubernetes manifest文件
  templates/NOTES.txt # 可选: 包含简要使用说明的纯文本文件
```



#### oam

四条cli开发原则：

1. 默认创建现代化的应用。满足无服务化 (serverless)，基础设 施即代码 (infrastructure as code)，可观测 (observable)，安全 (secure)；
2. 用户应该考虑的是架构，而不是基础设施；
3. 运维也是工作流的一部分；
4. 应用交付是持续的。应用的升级变更也应该方便地集成到 CI/CD 系统中；