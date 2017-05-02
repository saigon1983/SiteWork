import os, openpyxl

from Libs.bitrixDataParser import *
from Libs.classSKUList import *
from string import ascii_letters
from Libs.constructTable_parameters import constructParametersTable

#data1 = parseData('DataFolder\\no_text.txt')
data2 = parseData('DataFolder\\no_properties.txt')
SKUS2 = SKUList()
for item in data2[0]:
    SKUS2.append(SKU.fromData(item))
newBase = Database.loadDatabase()
#newBase = Database.construct()
#newBase.saveDatabase()

for item in SKUS2:
    item.fillFromDatabase(newBase)
homogenList = SKUS2.splitToHomogenous()
for skuList in homogenList.values():
    #skuList.saveToExcel(skuList.types[1])
    if skuList.types[0]:
        print(skuList.types[1])