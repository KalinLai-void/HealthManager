import csv
import MakerThon.urls
from Food_control.models import Food


def write():
    with open('food.csv', newline='') as csvfile:
        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.DictReader(csvfile)

        for row in rows:
            if row['蛋白質'] == '':
                row['蛋白質'] = 0
            if row['脂肪'] == '':
                row['脂肪'] = 0
            if row['飽和脂肪'] == '':
                row['飽和脂肪'] = 0
            if row['反式脂肪'] == '':
                row['反式脂肪'] = 0
            if row['碳水化合物'] == '':
                row['碳水化合物'] = 0
            if row['鈉'] == '':
                row['鈉'] = 0
            if row['糖'] == '':
                row['糖'] = 0
            obj = Food.objects.create(name=row['名字'], calorie=row['熱量'], protein=row['蛋白質'],
                                      fat=row['脂肪'], saturated_fat=row['飽和脂肪'], trans_fat=row['反式脂肪'],
                                      carbohydrate=row['碳水化合物'], sodium=row['鈉'], sugar=row['糖'])
            obj.save()
"""
    name = models.CharField(max_length=20)
    calorie = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    saturated_fat = models.FloatField()
    trans_fat = models.FloatField()
    carbohydrate = models.FloatField()
    sodium = models.FloatField()
    sugar = models.FloatField()
"""
