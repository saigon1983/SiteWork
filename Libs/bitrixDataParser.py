import os
from collections import OrderedDict

from Libs.getBrands import getBrands

def parseData(someFile):
    # Функия разбирает текстовый файл с данными, полученный из Битрикс и сортирует их записывает результат в текстовый
    # файл по категориям
    resultArray = []        # Список упорядоченных словарей всех моделей
    wasteArray = []         # Список непрошедших парсинг элементов
    # Считываем данные из файла построчно, помещая их в список data
    BRANDS = getBrands()
    with open(someFile, 'r') as workFile:
        data = workFile.readlines()
    # Производим первое разделение по символу "-----". Отделяем артикул (если он есть) от всего остального
    splitted_1 = []
    for line in data:
        splitted_1.append(line.strip().upper().split('-----'))
    # Производим второе разделение по названию бренда
    for i in range(len(splitted_1)):
        skuData = {}
        skuData['Название'] = splitted_1[i][0].split(')')[1].strip()
        skuData['Артикул']  = splitted_1[i][1].strip()
        for brand in BRANDS:
            if brand not in skuData['Название']:
                wasteArray.append(skuData)
            else:
                resultArray.append(skuData)
    resultArray.sort(key = lambda k: k['Название'])

    return (resultArray, wasteArray)