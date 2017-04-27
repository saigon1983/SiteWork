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
    splitted_2 = []
    counter = 0
    for i in range(len(splitted_1)):
        item = {}
        for brand in BRANDS:
            if brand in splitted_1[i][0]:
                item['Бренд'] = brand
                temp = splitted_1[i][0].split(brand)
                subtemp = temp[0].split(')')
                item['ТГ2'] = subtemp[1].strip()
                item['Модель'] = temp[1].strip()
        try:
            item['Бренд']
            if not splitted_1[i][1].strip():
                item['Артикул'] = item['Модель']
            else:
                item['Артикул'] = splitted_1[i][1].strip()
            splitted_2.append(item)
        except:
            wasteArray.append(splitted_1[i])
    for item in splitted_2:
        skuData = OrderedDict()
        skuData['ТГ2']      = item['ТГ2']
        skuData['Артикул']  = item['Артикул']
        skuData['Бренд']    = item['Бренд']
        skuData['Модель']   = item['Модель']
        resultArray.append(skuData)
    resultArray.sort(key = lambda k: k['ТГ2'])

    return (resultArray, wasteArray)