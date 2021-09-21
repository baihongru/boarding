# Boarding

 本项目是极客时间课程[Django快速开发实战](https://time.geekbang.org/course/intro/100061901)的学习笔记，由于Django是一个提供易用性的WEB框架，它封装了很多特性便于简洁地实现你的目的，因此如果你对Django的设计哲学不够了解直接阅读代码并不是一个好的选择，所以必须从[Django官方教程](https://docs.djangoproject.com/zh-hans/3.2/intro/)起步，了解Django的设计哲学和如何实现易用性，在此基础上学习极客时间的课程才能系统地理解一个Django项目地开发过程。

本项目的目的并不是重现课程的源码，而是希望按照Django的设计哲学完成这个项目，更重要的是跟随课程了解一个现代项目的开发过程，包含MVC、DevOps、容器部署等。

最权威的参考：[Django文档](https://docs.djangoproject.com/zh-hans/3.2/)

欢迎上船！

## 运行这个应用

由于仅仅是一个简单的示例，这里将以开发模式运行这个应用。推荐在虚拟环境中安装和运行这个应用。

1. 下载最新的源代码到本地。

2. 在源代码目录中激活虚拟环境并安装依赖。

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. 创建数据库表和管理后台超级用户。

    ```bash
    # 生成数据库迁移文件
    # 由于源代码中已经包含数据库迁移文件，可跳过生成步骤
    python manage.py makemigrations
    # 数据库迁移
    python manage.py migrate
    # 创建管理后台超级用户
    python manage.py createsuperuser
    ```

4. 启动开发服务器。

    ```bash
    python manage.py runserver 0:8000
    ```

5. 访问这个服务器。

    ```text
    访问投票应用：
    http://<你的IP>:8000/polls/
    访问职位发布应用：
    http://<你的IP>:8000/jobs/
    访问管理后台：
    http://<你的IP>:8000/admin/
    ```
