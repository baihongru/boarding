## 命令行

### tag

> 注意与远程存储库相关的操作需要输入GitHub账户的用户名和具备相应权限的Personal access token

- 查看tag

    ```bash
    # tag列表
    git tag
    # 使用通配符查看列表
    gti tag -l 'v1.*'
    # tag信息
    git show <tag>
    ```

- 创建和删除tag

    ```bash
    # 创建tag，不带详细信息
    git tag v1.0
    # 创建tag，带详细信息
    git tag -a v1.0 -m 'first version'
    # 删除本地tag
    git tag -d v1.0
    # 删除远程tag
    git push origin :refs/tags/v1.0
    ```

- 将tag推送到GitHub

    ```bash
    # 推送指定tag
    git push origin v1.0
    # 推送全部tag
    git push origin --tags
    ```

- 创建一个基于指定tag的分支

    ```bash
    # TODO
    ```
