# django_demo
 django_demo, study django



------
[TOC]

------




# Step

## 1. 安装环境





## 2. 创建Django项目和App

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

### 项目应用（app）目录

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

## 4. 配置settings.py 

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

## 5. 启动项目

运行项目先执行数据库相关操作，再启动 django 项目，在下文将详细讲到数据库迁移

数据库迁移操作

`​python manage.py makemigrations​​​​`

`​python manage.py migrate`

启动Django服务

`python manage.py runserver`



## 6. **Django 构建数据表创建与数据迁移**

### 模块功能

数据表的构建主要是通过 models.py 文件来完成,models.py文件是Django中定义和操作数据库数据模型的核心文件，它直接影响着应用程序与数据库的交互方式。它的作用可以简要概括如下：

1. **定义数据模型**：`models.py` 文件用于定义应用程序中的数据模型。这些模型通常对应数据库中的表，定义了数据的组织方式和结构。
2. **映射数据库表**：通过在`models.py`中创建类（继承自`django.db.models.Model`），可以指定数据库表的名称、字段类型以及字段之间的关系（如一对多、多对多）。
3. **字段和行为**：在模型类中，每个字段都对应数据库中的一个列，你可以指定字段的类型（如整数、字符串、日期等），以及字段的其他属性（如是否可为空、是否是主键等）。
4. **数据验证**：`models.py` 中的模型可以包含数据验证规则，确保输入的数据符合预期的格式和约束。
5. **生成数据库迁移**：当你在`models.py`中对模型进行更改后，可以通过 Django 的迁移系统生成迁移文件，这些文件包含了将数据库结构更新到最新模型定义所需的SQL命令。

今天的例子就是在`apps`应用的 models.py 文件中创建两个表：产品分类表和产品信息表。



### models.py

#### 引入模块

引入用到其他app中用到的模块以及将`from django.db import models`换为`from django.db.models import *`,其功能如下：

1. 引入`Django`的数据库操作模块：`Django`是一个`Web`框架，它的`db.models`模块提供了`ORM`（对象关系映射）功能，让我们可以用Python对象来操作数据库。
2. 导入所有模型类和工具：使用*通配符导入意味着你将导入models模块中的所有类、函数和变量。这包括Model基类（用于定义数据模型），各种字段类型（如`CharField`, `IntegerField`等），以及查询相关的工具和函数。
3. 简化代码：通过一次导入所有内容，你可以直接使用`Django ORM`提供的任何功能，而无需每次都写全模块路径，比如django.db.models.CharField可以直接写成`CharField`。
4. 可能的副作用：尽管这种导入方式方便，但也可能导致命名冲突，特别是当你从其他库也导入相似名称的对象时。因此，通常推荐只导入你需要的具体对象，以保持代码的清晰性和可读性。例如，`from django.db.models import Model, CharField`。



> 如果是其他数据库也是可以的，比如MongoDB。但是import模块需要修改（djongo）
>



#### 对象类型、常用字段、常用配置

在Django中，常用的字段类型用于在模型中定义数据模型的字段，每种字段类型对应数据库中的不同数据类型，并提供了特定的功能和选项。

以下是一些Django中常用的字段类型：

```python
"""
CharField：用于存储字符串类型，有最大长度限制
IntegerField：用于存储整数类型
FloatField：用于存储浮点数类型
BooleanField：用于存储布尔类型
DateField：用于存储日期类型
DateTimeField：用于存储日期和时间类型
ImageField：用于存储图片类型
FileField：用于存储文件类型
ForeignKey：外键 用于表示数据库表之间的关联关系

OneToOneField：一对一 用于表示一对一的关联关系
ManyToManyField：多对多 用于表示多对多的关联关系
"""


```

在Django中，字段选项用于为模型中的字段提供额外的配置。以下是一些常用的字段选项

```python
"""
primary_key 字段是否为主键，默认为 False

max_length：字段的最大长度限制，可以应用于多种不同的字段类型。
verbose_name：字段的友好名称，便于在管理员后台可视化操作时使用。
default：指定字段的默认值。
null：指定字段是否可以为空。null=True 设置允许该字段为 NULL 值

blank：指定在表单中输入时是否可以为空白。
choices：用于指定字段的可选值枚举列表。

editable 默认为True，表示字段在表单中可以编辑
unique 字段是否唯一，默认为 False

related_name：指定在多对多等关系中反向使用的名称。
on_delete：指定如果外键关联的对象被删除时应该采取什么操作。

"""
```

##### 示例

```python
class Status(TextChoices):
    QUALIFIED = 'qualified', '良品'  # 良品选项，值为'qualified'，显示名称为'良品'
    UNQUALIFIED = 'unqualified', '不良品'  # 不良品选项，值为'unqualified'，显示名称为'不良品'

class DeliveryMaterial(Model):
    status = models.CharField(
        max_length=32,
        choices=Status.choices,
        default=Status.QUALIFIED,
        verbose_name='状态'
    )
```

`TextChoices` 是 Django 3.0 引入的一个枚举类，用于在模型字段中创建可选择的、文本值的选项。

```
category = ForeignKey('data.GoodsCategory', on_delete=SET_NULL, null=True,related_name='goods_set', verbose_name='产品分类')
```

`related_name` 指定在多对多等关系中反向使用的名称。

`on_delete` 指定如果外键关联的对象被删除时应该采取什么操作

该段定义了一个外键字段 `category`，它建立了当前`Goods`模型与名为 `GoodsCategory` 的模型之间的关联，一个`GoodsCategory`可以关联多个当前模型的实例，表示一个类别下可以有多个产品。当所关联的记录被删除时，该字段会自动设置为 NULL，它可以为空。`related_name` 设置了反向查询的名称，在 `GoodsCategory` 模型中，可以通过 `goods_set` 这个属性来访问所有关联的产品对象集合。 

### 合并数据库（数据迁移）

> 运行项目先执行数据库相关操作，再启动 django 项目，在下文将详细讲到数据库迁移
>
> 数据库迁移操作
>
> `​python manage.py makemigrations​​​​`
>
> `​python manage.py migrate`
>
> 启动Django服务
>
> `python manage.py runserver`
>
> **第五步**



这两个命令是 Django 框架中的关键命令，用于进行数据库迁移。当你修改了 Django 模型后，你需要运行这两个命令，以将这些更改应用到数据库中。

```
python manage.py makemigrations
```

这个命令用于生成迁移脚本，迁移脚本用于告诉数据库如何根据这些结构变化进行更新。当你更新了模型文件之后，需要运行该命令，Django 会检测模型的改变，然后自动生成相应的迁移脚本，存储在 `migrations/` 目录下。通常来说，你需要针对每个应用运行一次该命令。

```
python manage.py migrate
```

这个命令用于将迁移脚本应用到数据库中。当你在模型文件中进行更改之后，需要先通过 `makemigrations` 命令生成迁移脚本，然后运行该命令将这些脚本应用到数据库中。对于新的迁移脚本，Django 会逐个执行它们，从而更新数据库结构。对于已经执行过的脚本，Django 会跳过它们，避免重复执行。

这两个命令是 Django 框架中非常重要的命令，在修改数据库相关内容时必须时刻清醒地记住使用它们。

```shell
PS D:\Work\others\django_demo\erp> python manage.py makemigrations
Migrations for 'erp_test':
  apps\erp_test\migrations\0001_initial.py
    - Create model GoodsCategory
    - Create model Goods
  
  
PS D:\Work\others\django_demo\erp> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, erp_test, sessions
Running migrations:
  Applying erp_test.0001_initial... OK
```














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