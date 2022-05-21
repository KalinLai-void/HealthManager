from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
名字 char
熱量 float
蛋白質 float
脂肪 float
    飽和 float
    反式 float
碳水 float
鈉 float 
糖 float
"""





class Food(models.Model):
    name = models.CharField(max_length=20)
    calorie = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    saturated_fat = models.FloatField()
    trans_fat = models.FloatField()
    carbohydrate = models.FloatField()
    sodium = models.FloatField()
    sugar = models.FloatField()

    def __str__(self):
        return self.name


class User_table(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField(upload_to='photos')
