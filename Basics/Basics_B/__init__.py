# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/10/3 9:42


# fixture


# 优势:
#       命名方式灵活，不局限于setup和teardown这几个命名
#       conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置
#       scope="module" 可以实现多个.py跨文件共享前置
#       scope="session" 以实现多个.py跨文件使用一个session来完成多个用例


# fixture(scope="function", params=None, autouse=False, ids=None, name=None):
#   可以使用此装饰器（带或不带参数）来定义fixture功能。
#   fixture功能的名称可以在以后使用，引用它会在运行测试之前调用它：
#   test模块或类可以使用pytest.mark.usefixtures（fixturename标记。
#   测试功能可以直接使用fixture名称作为输入参数，在这种情况下，夹具实例从fixture返回功能将被注入。
#
#   :arg scope: scope 有四个级别参数 "function" (默认), "class", "module" or "session".
#
#   :arg params: 一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它
#
#   :arg autouse:  如果为True，则为所有测试激活fixture func 可以看到它。 如果为False（默认值）则显式需要参考来激活fixture
#
#   :arg ids: 每个字符串id的列表，每个字符串对应于params 这样他们就是测试ID的一部分。 如果没有提供ID它们将从params自动生成
#
#   :arg name:   fixture的名称。 这默认为装饰函数的名称。 如果fixture在定义它的同一模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽; 解决这个问题的一种方法是将装饰函数命名
#                        “fixture_ <fixturename>”然后使用”@ pytest.fixture（name ='<fixturename>'）“”。
# Fixtures可以选择使用 yield 语句为测试函数提供它们的值，而不是 return。 在这种情况下，yield语句之后的代码块作为拆卸代码执行，而不管测试结果如何。fixture功能必须只产生一次