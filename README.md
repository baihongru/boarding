# boarding

 Django官方教程，一个投票应用。

## 运行这个应用

由于仅仅是一个简单的示例，这里将以开发模式运行这个应用。推荐在虚拟环境中安装和运行这个应用。

1. 下载Releases的源代码到本地。

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
    访问管理后台：
    http://<你的IP>:8000/admin/
    ```
