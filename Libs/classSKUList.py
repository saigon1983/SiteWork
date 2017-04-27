# Класс SKUList представляет из себя список любого количества SKU. Для работы с классом предоставляются многие методы из
# класса list, а так же некоторые свои специфические

import openpyxl
from Libs.getBrands import getBrands
from Libs.classSKU import *

class SKUList:
    def __init__(self, someList = None):
        # Конструктор принимает в качестве аргумента список или кортеж. Если аргумент явно не передается, создается пустой
        # экземпляр, который в последствии может быть заполнен методом append
        if type(someList) == tuple:     self.array = list(someList)
        elif type(someList) == list:    self.array = someList
        elif not someList:              self.array = []
        else:                           raise TypeError ('Wrong data passed to SKUList constructor!')
        self.setupArticlesArray()
    def setupArticlesArray(self):
        # Метод создает отдельный список артикулов списка SKU для более быстрого поиска элементов по артикулу
        self.articlesArray = []
        for sku in self.array:
            self.articlesArray.append(sku.article)
    def append(self, item):
        # Метод добавления элемента в список. Элемент обязан быть либо экземпляром класса SKU, либо списком или кортежем
        # экземпляров этого класса. Так же item может быть другим объектом SKUList
        if type(item) == SKU:
            self.array.append(item)
            self.articlesArray.append(item.article)
            return
        elif type(item) == SKUList:
            data = item.array
        elif type(item) == list:
            for element in item:
                if type(element) != SKU:
                    raise TypeError ('Wrong data in list, that you try to append to SKUList!')
            data = item
        elif type(item) == tuple:
            for element in item:
                if type(element) != SKU:
                    raise TypeError ('Wrong data in tuple, that you try to append to SKUList!')
            data = list(item)
        else:
            raise TypeError ('Wrong data passed to append() method of SKUList object!')
        self.array == data
        for item in data:
            self.articlesArray.append(item.article)
    def remove(self, item):
        # Метод удаляет указанный элемент из списка
        try:
            index = self.array.index(item)
            self.array.remove(item)
            self.articlesArray.remove(self.articlesArray[index])
        except:
            raise ValueError ('No such item in SKUList object!')
    def getIndexByItem(self, item):
        # Метод возвращает индекс указанного SKU
        if type(item) != SKU: raise TypeError ('Non-SKU object passed to getIndexByItem() method')
        try:
            return self.array.index(item)
        except:
            raise ValueError ('No such item in SKUList object!')
    def getIndexByArticle(self, article):
        # Метод возвращает индекс SKU по ее артикулу
        if type(article) != str: raise TypeError ('Article, passed to SKUList.getIndexByArticle() must be str, not {}!'.format(type(article)))
        try:
            return self.articlesArray.index(article)
        except:
            raise ValueError ('No such item in SKUList object!')
    def getItemByIndex(self, index):
        # Метод возвращает объект SKU по указанному индексу
        if type(index) != int: raise TypeError ('Index, passed to SKUList.getItemByIndex() must be int, not {}!'.format(type(index)))
        try:
            return self.array[index]
        except:
            raise ValueError ('Wrong index argument, passed to SKUList.getItemByIndex()')
    def getItemByArticle(self, article):
        # Метод возвращает SKU по указанному артикулу, если таковая существует, или None в ином случае
        if type(article) != str: raise TypeError ('Article, passed to SKUList.getItemByArticle() must be str, not {}!'.format(type(article)))
        try:
            return self.array[self.articlesArray.index(article)]
        except:
            return None
    def __str__(self):
        # Метод строкового представления объекта списка товаров
        result = ''
        for item in self.array:
            result += str(item)
            result += '\n'
        return result
    @classmethod
    def fromExcel(cls, excelFile, gg1, gg2):
        # Метод класса, создающий список SKU на основе предоставленной таблицы excel
        try:    workBook = openpyxl.load_workbook(excelFile)
        except: raise ValueError ('No Excel file {} found!'.format(excelFile))
        BRANDS = getBrands()
        workSheet = workBook.get_active_sheet()
        firstRow = workSheet[1]
        headers = {}
        for header in firstRow:
            headers[header.value] = firstRow.index(header)
        elementsList = []
        for row in workSheet.iter_rows(min_row = 2):
            skuData = {}
            skuData['ТГ1'] = gg1
            skuData['ТГ2'] = gg2
            skuData['Артикул'] = row[headers['Артикул']].value.strip().upper()
            nameData = row[headers['Название']].value.upper()
            for brand in BRANDS:
                if brand in nameData:
                    skuData['Бренд'] = brand
                    skuData['Модель'] = nameData.split(brand)[-1].strip()
            elementsList.append(SKU.fromData(skuData))
        return cls(elementsList)