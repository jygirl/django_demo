__init.py__ 是一个空文件，作用同前。

admin.py 文件跟网站的后台管理相关。

models.py 文件跟数据库操作相关。主要用一个 Python 类来描述数据表。运用这个类,你可以通过简单的 Python 的代码来创建、检索、更新、删除 数据库中的记录而无需写一条又一条的 SQL 语句。

views.py 包含了页面的业务逻辑，接收浏览器请求，进行处理，返回页面操作相关。

tests.py 文件用于开发测试用例，在实际开发中会有专门的测试人员使用。

apps.py 文件是 Django1.10 之后增加的，通常里面包含对应用的配置。

migrations 是 Django 1.8 之后推出的 migrations 机制，使 Django 数据模式管理更容易。migrations 机制有两个指令，makemigrations 和 migrate。makemigrations 指令是用 models.py文件 里面的model 和当前的 migrations 代码里面的 model 做对比，如果有新的修改，就生成新 migrations 代码。migrate 指令是用 migrations 目录中代码文件和 Django 数据库 django_migrations 表中的代码文件做对比，如果表中没有，那就对没有的文件按顺序及依赖关系做 migrate apply ，然后再把代码文件名加进 migrations 表中。在目录中自动生成了 __init__.py 文件。