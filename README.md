# CaoLiu_AutoReply（腾讯云函数）

注：当前分支基于 [0honus0/CaoLiu_AutoReply at 708c2d277c17277411eb120d43e0c2fbb4146c09](https://github.com/0honus0/CaoLiu_AutoReply/tree/708c2d277c17277411eb120d43e0c2fbb4146c09)，此分支将会不时从[上游仓库](https://github.com/0honus0/CaoLiu_AutoReply/)同步更新。

### 更新日志

```
2023.07.30-Based-0.23.07.03.1
           优化重试登录，在登录账户时，为两次重试登录之间，加入一个至少6秒，至多1分钟的延时，避免重试过于频繁。

2023.07.20-Based-0.23.07.03.1
           从上游仓库同步更新，Commit：“更新版本号”
           修复在获取已回复帖子列表时无法识别置顶帖（绿色链接）的问题
           注：更新了config.example.yml

2023.07.02-Based-0.23.07.01.1
           从上游仓库同步更新，Commit：“增加回复板块选择，修改登陆参数”
           更新了config.example.yml

2023.05.16-Based-0.23.05.13.1
           修复了同一个帖子重复回复的问题。

2023.05.13-Based-0.23.05.13.1
           更新：配置文件新增关键字屏蔽

2023.04.23-Based-0.23.04.04.1
           更新：新增调试模式。
                该模式下将会测试社区的域名是否可用，并不会执行自动回帖任务。

2023.04.13-Based-0.23.04.04.1
           修复：
           1、由于腾讯云函数写入权限问题，禁用Cookie保存的功能；
           2、彻底禁用自动更新，仅保留更新提醒。
           PS：由于腾讯云函数“阅后即焚”的特性，Cookie保存和自动更新的功能毫无意义。
              如有需要，请手动从云函数控制台上传更新。

2023.04.11 发布：基于2023.04.04的版本移植到腾讯云函数。
```

### 用前须知：合理使用，得码不易，且行且珍惜。

[调试模式](#调试模式)

### 腾讯云函数配置

由于国内节点经常屏蔽社区域名，建议使用海外节点创建云函数。

- 创建一个云函数，选择“从头开始”创建。

- 运行环境：设为 `Python 3.6` 或 `Python 3.7`；

  ![image-20230412101036409](https://s2.loli.net/2023/03/24/Xd1nxSzBUrQkDH5.png)

- 时区：设为  `Asia/Shanghai(北京时间)`；

- 提交方法：选择本地上传zip包

- 执行方法：请设为 `index.main_handler`（默认）

- [获取代码包](https://github.com/pooneyy/CaoLiu_AutoReply/releases/latest)。将其上传：

  ![image-20230413092951560](https://s2.loli.net/2023/04/13/PDCMxemLZ7EH1aT.png)

- 执行超时时间：请按照实际运行时间设定，应略大于实际运行时间。红框是因为未启用异步执行。

  - 计算执行超时时间：在`config.yml`文件内寻找参数`TimeIntervalEnd`（时间间隔最大值），执行超时时间应大于该参数乘以`ReplyLimit`（回复次数限制）加上1之和的值再加上账户数乘以300的值。

  - 具体公式为：`账户数 * 300 + TimeIntervalEnd * (ReplyLimit + 1)`

  - 如`TimeIntervalEnd: 2048`，`ReplyLimit: 10`，有 5 个账户，那么执行超时时间应大于`5 * 300 + 2048 * 11`，即`24028`，这是比较稳妥的，可以避免因超时而导致任务提前结束。

  - 为了便于计算，现已加入执行超时时间计算器`ExecutionTimeoutCalculator.py`可使用它快速计算

    ![image-20230720211140098](https://s2.loli.net/2023/07/20/XVYTS8baLwxh3c7.png)

  - 需要注意的是，由于开启异步执行后，云函数超时时间最大值为`86400`秒，所以请根据账号数量设置云函数超时时间和`TimeIntervalEnd`的值。

    ![image-20230411220418260](https://s2.loli.net/2023/04/11/IDLkK2JBTPOAMoe.png)

- 日志配置：可不配置日志

- **执行配置**：**请启用异步执行**

  ![image-20230411220658627](https://s2.loli.net/2023/04/11/fPKwAZF52qg1LYp.png)

- 将配置文件 `config.example.yml`，重命名为 `config.yml`，按照提示修改内容即可，

- 上传相关的文件：

  现在你只需上传Cookie（如果有的话）。config.yml、requirements.txt、sendLog.py不需要上传了、

  ![image-20230412103258289](https://s2.loli.net/2023/04/12/yk1bPNMqaKh2Afp.png)

- ~~安装依赖：~~

  代码包包含依赖。

- **部署函数**：云函数只有部署才会生效。

  ![image-20230411215251860](https://s2.loli.net/2023/04/11/lpKjOnZki7UxwQH.png)

- 设置触发器。建议选择自定义触发周期，使用cron表达式。例如`20 12 14 * * * *`则为每天 14:12:20 运行一次。

### 高级配置

##### 调试模式

调试模式下将会测试社区的域名是否可用，并不会执行自动回帖任务。

调试模式默认关闭，如果需要开启，请在`config.yml`文件寻找以下内容，若没有请自行添加：

```yaml
gobal_config:
    DebugMode: True
```

