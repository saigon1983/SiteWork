from Libs.bitrixDataParser import *
from Libs.classSKUList import *

data1 = parseData('DataFolder\\no_text.txt')

SKUS = SKUList()
for item in data1[0]:
    SKUS.append(SKU.fromData(item))

data = SKUList.fromExcel('DataFolder\\ExcelFiles\\Вытяжки ВСТР.xlsx', 'Встраиваемая техника', 'Вытяжка')

for item in data:
    print(item)
    print(item.parameters)