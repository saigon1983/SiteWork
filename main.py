import os, openpyxl

from Libs.bitrixDataParser import *
from Libs.classSKUList import *
from string import ascii_letters
from Libs.constructTable_parameters import constructParametersTable

data1 = parseData('DataFolder\\no_text.txt')
#data2 = parseData('DataFolder\\no_properties.txt')
SKUS2 = SKUList()
for item in data1[0]:
    SKUS2.append(SKU.fromData(item))
newBase = Database.loadDatabase()
#newBase = Database.construct()
#newBase.saveDatabase()

i = 0
j = 0
for item in SKUS2:
    item.fillFromDatabase(newBase)
print(i)
print(j)