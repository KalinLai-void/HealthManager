from django.test import TestCase

# Create your tests here.
E = [['北蕉平均值', 1], ['木瓜平均值', 1], ['芭樂平均值(白肉)', 1], ['芒果平均值(西洋種)', 1], ['甜瓜平均值(網紋洋香瓜)', 1], ['蓮霧平均值(粉紅色種)', 1],
         ['西洋梨平均值', 1], ['蘋果平均值(混色)', 1], ['甜橙平均值(普遍系)', 1]]

import random

l = random.choices(E,None,k=3)

print(l)