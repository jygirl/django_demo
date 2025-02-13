from django.db import models

# Create your models here.

from django.db.models import *

# class Status(TextChoices):
#     QUALIFIED = 'qualified', '良品'  # 良品选项，值为'qualified'，显示名称为'良品'
#     UNQUALIFIED = 'unqualified', '不良品'  # 不良品选项，值为'unqualified'，显示名称为'不良品'

# class DeliveryMaterial(Model):
#     status = models.CharField(
#         max_length=32,
#         choices=Status.choices,
#         default=Status.QUALIFIED,
#         verbose_name='状态'
#     )


class GoodsCategory(Model):

    name = CharField(max_length=64, verbose_name='名称')

    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')


class Goods(Model):
        
    number = CharField(max_length=32, verbose_name='编号')

    name = CharField(max_length=64, verbose_name='名称')

    barcode = CharField(max_length=32, null=True, blank=True, verbose_name='条码')

    category = ForeignKey('data.GoodsCategory', on_delete=SET_NULL, null=True,related_name='goods_set', verbose_name='产品分类')
    # to: 指定关联的目标模型，可以是模型类或者 "app_name.ModelName" 的字符串形式
    # on_delete: 指定关联对象被删除时的行为，例如：
    # CASCADE: 删除关联对象时，级联删除引用的对象。
    # SET_NULL: 将引用对象设为 NULL（需要设置 null=True）。
    # PROTECT: 阻止删除关联对象。
    # DO_NOTHING: 不执行任何操作（需自行处理外键约束）。
    # SET_DEFAULT: 设置为默认值（需要设置 default）。
    # releated_name 定义反向关系的名称：默认情况下，Django 会使用 <模型名>_set 作为反向关系的名称。

    spec = CharField(max_length=64, null=True, blank=True, verbose_name='规格')
            
    shelf_life_days = IntegerField(null=True, verbose_name='保质期天数')

    purchase_price = FloatField(default=0, verbose_name='采购价')

    retail_price = FloatField(default=0, verbose_name='零售价')

    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
   



"""
models.py 文件跟数据库操作相关。
主要用一个 Python 类来描述数据表。运用这个类,你可以通过简单的 Python 的代码来创建、检索、更新、删除 数据库中的记录
而无需写一条又一条的 SQL 语句。




数据表的构建主要是通过 models.py 文件来完成,models.py文件是Django中定义和操作数据库数据模型的核心文件，它直接影响着应用程序与数据库的交互方式。它的作用可以简要概括如下：

定义数据模型：models.py 文件用于定义应用程序中的数据模型。这些模型通常对应数据库中的表，定义了数据的组织方式和结构。

映射数据库表：通过在models.py中创建类（继承自django.db.models.Model），可以指定数据库表的名称、字段类型以及字段之间的关系（如一对多、多对多）。

字段和行为：在模型类中，每个字段都对应数据库中的一个列，你可以指定字段的类型（如整数、字符串、日期等），以及字段的其他属性（如是否可为空、是否是主键等）。

数据验证：models.py 中的模型可以包含数据验证规则，确保输入的数据符合预期的格式和约束。

生成数据库迁移：当你在models.py中对模型进行更改后，可以通过 Django 的迁移系统生成迁移文件，这些文件包含了将数据库结构更新到最新模型定义所需的SQL命令。

"""