from django.contrib import admin

# Register your models here.
from .models import * # 引入产品表

# 一定要分开逐个注册，不能放在一起

admin.site.register(Goods)

 # 在admin站点中 注册产品表

admin.site.register(GoodsCategory) 

# 在admin站点中 注册产品表