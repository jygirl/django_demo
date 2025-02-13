settings.py 文件，根据你的需求配置项目设置，例如数据库设置、静态文件路径等。


- __init__.py： 是一个空文件，作用是所在的这个目录可以被当作包使用。

- settings.py：该 Django 项目整体配置文件。（该文件非常重要，建议认真理解这个文件中可用的设置类型及其默认值。）

- urls.py：Django 项目的 URL 设置。可视其为你的 Django 网站的目录。

- asgi.py 与 wsgi.py：常见的网关接口协议：CGI，FastCGI，WSGI，ASGI。asgi.py 是异步服务器网关接口项目配置文件。ASGI 描述了 Python Web 应用程序和Web服务器之间的通用接口。与 WSGI 不同的是，ASGI允许每个应用程序有多个异步事件。另外，ASGI 支持同步和异步应用程序。开发人员可以将原有的同步 WSGI Web 应用程序迁移到 ASGI ，也可以使用 ASGI 构建新的异步Web应用程序。