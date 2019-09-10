from django.db import models


# Create your models here.
# 以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，
# 数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
class Test(models.Model):
    name = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



