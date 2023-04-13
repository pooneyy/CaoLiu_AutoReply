# CaoLiu_AutoReply（腾讯云函数）

注：此分支基于 [0honus0/CaoLiu_AutoReply at 832398a5bca0850913b096069aa33dd66475c99e](https://github.com/0honus0/CaoLiu_AutoReply/tree/832398a5bca0850913b096069aa33dd66475c99e)，此分支将会不时从[上游仓库](https://github.com/0honus0/CaoLiu_AutoReply/)同步更新。

### 更新日志

```
2023.04.13 修复：
           1、由于腾讯云函数写入权限问题，禁用Cookie保存的功能；
           2、彻底禁用自动更新，仅保留更新提醒。
           PS：由于腾讯云函数“阅后即焚”的特性，Cookie保存和自动更新的功能毫无意义。如有需要，请手动从云函数控制台上传更新。

2023.04.11 发布：基于2023.04.04的版本移植到腾讯云函数。
```

### 用前须知：合理使用，得码不易，且行且珍惜。

### 腾讯云函数配置

- 创建一个云函数，选择“从头开始”创建。

- 运行环境：设为 `Python 3.6` 或 `Python 3.7`；

  ![image-20230412101036409](https://s2.loli.net/2023/03/24/Xd1nxSzBUrQkDH5.png)

- 时区：设为  `Asia/Shanghai(北京时间)`；

- 提交方法：选择本地上传zip包

- 执行方法：请设为 `index.main_handler`（默认）

- [获取代码包](https://github.com/pooneyy/CaoLiu_AutoReply/releases/latest)。将其上传：

  ![image-20230413092951560](C:/Users/29451/AppData/Roaming/Typora/typora-user-images/image-20230413092951560.png)

- 执行超时时间：请按照实际运行时间设定，应略大于实际运行时间。红框是因为未启用异步执行。

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
