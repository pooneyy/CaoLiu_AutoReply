# CaoLiu_AutoReply（腾讯云函数）

注：此分支基于 [0honus0/CaoLiu_AutoReply at 832398a5bca0850913b096069aa33dd66475c99e (github.com)](https://github.com/0honus0/CaoLiu_AutoReply/tree/832398a5bca0850913b096069aa33dd66475c99e)

### 用前须知：合理使用，得码不易，且行且珍惜。

### 腾讯云函数配置

- 运行环境：设为 `Python 3.6` 或 `Python 3.7`；

  ![image-20230411220149663](https://s2.loli.net/2023/04/11/FKfhqoz5uZejnxw.png)

- 时区：设为  `Asia/Shanghai(北京时间)`；

- **执行方法**：**请设为 `AutoReply.main_handler`**

  ![image-20230411220324907](https://s2.loli.net/2023/04/11/PGcLsi9By7TXgtJ.png)

- 执行超时时间：请按照实际运行时间设定，应略大于实际运行时间。红框是因为未启用异步执行。

  ![image-20230411220418260](https://s2.loli.net/2023/04/11/IDLkK2JBTPOAMoe.png)

- 日志配置：可不配置日志

- **执行配置**：**请启用异步执行**

  ![image-20230411220658627](https://s2.loli.net/2023/04/11/fPKwAZF52qg1LYp.png)

- 安装依赖：

  ```shell
  pip3 install -r ./src/requirements.txt -t ./src/
  ```
  
  ![image-20230411220804302](https://s2.loli.net/2023/04/11/IDvdqgFNrXt9SQs.png)
  
- 将配置文件 `config.example.yml`，重命名为 `config.yml`，按照提示修改内容即可，

- **部署函数**

  ![image-20230411215251860](https://s2.loli.net/2023/04/11/lpKjOnZki7UxwQH.png)

- 设置触发器。建议选择自定义触发周期，使用cron表达式。例如`20 12 14 * * * *`则为每天 14:12:20 运行一次。

### 更新日志

```
2023.04.11 发布：基于2023.04.04的版本移植到腾讯云函数。
```
