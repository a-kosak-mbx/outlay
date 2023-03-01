from django.db import models


class Tag(models.Model):
    name = models.TextField(max_length=32, unique=True)
    description = models.TextField(max_length=128)
    color = models.IntegerField(null=False)
    parent = models.ManyToManyField('Tag')


class ItemGroup(models.Model):
    name = models.TextField(max_length=256, unique=True)
    description = models.TextField(max_length=1024)
    parent = models.ForeignKey('ItemGroup', on_delete=models.CASCADE)


class Item(models.Model):
    name = models.TextField(max_length=256, unique=True)
    description = models.TextField(max_length=1024)
    group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


class ItemCode(models.Model):
    data = models.JSONField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Expense(models.Model):
    date = models.DateField(null=False)
    time = models.TimeField()


class ExpenseItem(models.Model):
    packs = models.IntegerField(null=False, default=1)
    items_in_pack = models.FloatField(null=True, default=1)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=250)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)


class Receipt(models.Model):
    data = models.JSONField(null=False)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)


class Payment(models.Model):
    data = models.JSONField(null=False)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
