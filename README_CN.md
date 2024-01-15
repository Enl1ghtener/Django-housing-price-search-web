# 项目名称

项目简要介绍：该项目使用Django框架搭建了一个Web应用，用于查询各城市的房价信息。通过爬虫获取房价数据，后端读取数据并传递给前端，在前端显示数据并绘制折线图。

## 如何运行

以下是在本地运行项目的简要步骤：

1. 克隆项目到本地：

    ```bash
    git clone [https://github.com/your-username/your-repo.git](https://github.com/Enl1ghtener/Django-housing-price-search-web)

2. 进入项目目录：

    ```bash
    cd your-repo
    ```

3. 创建虚拟环境（可选）：

    ```bash
    python -m venv venv
    ```

4. 激活虚拟环境：

    - 在 Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - 在 macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. 安装依赖

   


6. 运行开发服务器：

    ```bash
    python manage.py runserver
    ```

7. 在浏览器中打开 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 查看项目。

## 项目结构

简要说明项目的目录结构和主要文件。

- `Django_first`: 项目主目录
    - `Django_first`: 框架
    - `crwal`:爬虫
    - `stu`: 主要应用目录
    - `templates/`: HTML模板文件
    - `static/`: 静态文件（CSS, JS, 图片等）
    - `views.py`: 视图函数
    - ...
  - `manage.py`: Django管理脚本
  - `db.sqlite3`: 数据库

## 数据爬取与处理

通过crwal_houseprice.py爬虫程序获取数据，由于网页并非每个城市的网址均为拼音，故只手动爬取了15个城市

## 注意事项

项目中除了城市查询功能，还包括一个login和register的学生登录的测试功能，查询功能也写在了stu内

练手项目，多有不周，之后可能会更新

## 贡献



## 许可证

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.。

