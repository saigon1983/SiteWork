from Libs.bitrixDataParser import *
from Libs.classSKUList import *

#data1 = parseData('DataFolder\\no_text.txt')
#data2 = parseData('DataFolder\\no_properties.txt')
'''
SKUS1 = SKUList()
for item in data1[0]:
    SKUS1.append(SKU.fromData(item))
SKUS2 = SKUList()
for item in data2[0]:
    SKUS2.append(SKU.fromData(item))
'''
data = SKUList.fromExcel('DataFolder\\ExcelFiles\\Вытяжки ВСТР.xlsx', 'Встраиваемая техника', 'Вытяжки')

data.saveAsExcel('table1')