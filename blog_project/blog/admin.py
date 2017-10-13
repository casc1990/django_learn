#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.contrib import admin
from .models import Post, Tag, Category
# Register your models here.


#定义post模型，指定显示的字段
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time', 'modified_time', 'category', 'author' ]


#定义tag模型，指定显示的字段
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


#定义tag模型，指定显示的字段
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# 把新增的 PostAdmin 也注册进来
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)