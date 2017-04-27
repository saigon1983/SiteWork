from Libs.bitrixDataParser import *
from Libs.classSKUList import *

data1 = parseData('DataFolder\\no_text.txt')

SKUS = SKUList()
for item in data1[0]:
    SKUS.append(SKU.fromData(item))

data = SKUList.fromExcel('DataFolder\\ExcelFiles\\Винные шкафы ВСТР.xlsx', 'Встраиваемая техника', 'Винный шкаф')
print(SKUS)
print(data)

