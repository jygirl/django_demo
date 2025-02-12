# django_demo
 django_demo, study django


# Step

## 安装环境

## 创建Django项目和App

创建项目
```shell
django-admin startproject projectname
```
`projectname`: `apps`

创建APP
```shell
cd peojectname
django-admin startapp appname
```
`appname`: `data`

创建完成后，需要到 settings.py 中注册

打开 apps(这里是`data`) 下 `apps.py` 文件,将 `name` 变量赋值修改

```python
class DataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "data"
```
改为
```python
class DataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.data"
```

### apps目录
在运行创建项目命令后项目自动生成了

- 项目名文件夹
- 子目录下同名子文件夹
- manage.py 文件

manage.py 提供了一种命令行工具，允许你以多种方式与该 Django 项目进行交互。如：python manage.py help ，能列出它所能做的事情。注意，此文件一般情况下不需要改动。

### apps/apps目录， 子目录文件组成

`__init__.py`： 是一个空文件，作用是所在的这个目录可以被当作包使用。

``settings.py``：该 Django 项目整体配置文件。（该文件非常重要，建议认真理解这个文件中可用的设置类型及其默认值。）

`urls.py`：Django 项目的 URL 设置。可视其为你的 Django 网站的目录。

`asgi.py` 与 `wsgi.py`：常见的网关接口协议：CGI，FastCGI，WSGI，ASGI。asgi.py 是异步服务器网关接口项目配置文件。ASGI 描述了 Python Web 应用程序和Web服务器之间的通用接口。与 WSGI 不同的是，ASGI允许每个应用程序有多个异步事件。另外，ASGI 支持同步和异步应用程序。开发人员可以将原有的同步 WSGI Web 应用程序迁移到 ASGI ，也可以使用 ASGI 构建新的异步Web应用程序。


## 项目应用（app）目录
在应用目录下由以下组成
 
```shell
data               
├─ __init__.py 
├─ admin.py        
├─ apps.py         
├─ models.py       
├─ tests.py        
├─ views.py        
└─  migrations      
   └─ __init__.py  
```   

__init.py__ 是一个空文件，作用同前。

admin.py 文件跟网站的后台管理相关。

models.py 文件跟数据库操作相关。主要用一个 Python 类来描述数据表。运用这个类,你可以通过简单的 Python 的代码来创建、检索、更新、删除 数据库中的记录而无需写一条又一条的 SQL 语句。

views.py 包含了页面的业务逻辑，接收浏览器请求，进行处理，返回页面操作相关。

tests.py 文件用于开发测试用例，在实际开发中会有专门的测试人员使用。

apps.py 文件是 Django1.10 之后增加的，通常里面包含对应用的配置。

migrations 是 Django 1.8 之后推出的 migrations 机制，使 Django 数据模式管理更容易。migrations 机制有两个指令，makemigrations 和 migrate。makemigrations 指令是用 models.py文件 里面的model 和当前的 migrations 代码里面的 model 做对比，如果有新的修改，就生成新 migrations 代码。migrate 指令是用 migrations 目录中代码文件和 Django 数据库 django_migrations 表中的代码文件做对比，如果表中没有，那就对没有的文件按顺序及依赖关系做 migrate apply ，然后再把代码文件名加进 migrations 表中。在目录中自动生成了 __init__.py 文件。

## 配置settings.py 和 启动项目

默认情况下，INSTALLED_APPS 包含以下应用，这些都是由 Django 提供的： 

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```



### 加入安装的库

'apps.erp_test'

'rest_framework',

'django_filters',

'drf_spectacular'

### 加入新增的APP

'apps.erp_test'


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.erp_test'
    'rest_framework',
    'django_filters',
    'drf_spectacular'
]
```

### 启动项目

运行项目先执行数据库相关操作，再启动 django 项目，在下文将详细讲到数据库迁移

数据库迁移操作

`​python manage.py makemigrations​​​​`

`​python manage.py migrate`

启动Django服务

`python manage.py runserver`














# `python manage.py help`

```shell
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```