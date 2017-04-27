from Libs.bitrixDataParser import *
from Libs.classSKUList import *

data1 = parseData('DataFolder\\no_text.txt')

SKUS = SKUList()
for item in data1[0]:
    SKUS.append(SKU.fromData(item))

data = SKUList.fromExcel('DataFolder\\ExcelFiles\\Вытяжки ВСТР.xlsx', 'Встраиваемая техника', 'Вытяжка')
data2 = data.getItemsByGroup(groupName='В столешницу')
for item in data2:
    print(item)
itemX = data2.getItemByArticle('CKASE')
data2.remove(itemX)
print('========================')
for item in data2:
    print(item)
print(len(data2.articlesArray))