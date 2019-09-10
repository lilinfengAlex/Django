# -*- coding: utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
    # test1 = Test(name='Alex')
    # test1.save()
    # test2 = Test(name='Sue')
    # test2.save()

    response = ""
    response1 = ""

    # objects模型管理器的all()获取所有数据
    # 相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于WHERE可以设置过滤条件
    response2 = Test.objects.filter(id=1)
    print(response2)

    # 获取单个对象
    response3 = Test.objects.get(id=1)
    print(response3)

    # OFFSET 0 LIMIT 2
    Test.objects.order_by('name')[0:2]

    Test.objects.filter(name='runoob').order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
