from Libs.getBrands import *
from Libs.detectTG import *
from collections import OrderedDict
from string import ascii_letters

VALID_SYMBOLS = ascii_letters + '1234567890-/.'

class SKU:
    CAPS_BRANDS = ('BORA', 'BORK', 'SMEG')
    def __init__(self,
                 article = '',
                 name = '',
                 color = '',
                 tradeGroups = {},
                 parameters = OrderedDict()):
        self.article = article.strip()
        self.parseArticle(article.strip())
        self.parseName(name)
        self.setupTradeGroups(tradeGroups)
        self.color = color.lower()
        self.setupParameters(parameters)
# ========== Перегруженные методы ==========
    def __str__(self):
        # Метод строковго представления объекта
        return self.getName()
    def __eq__(self, other):
        # Метод поврехностного сравнения объектов. Две SKU считаются равными, если равны их артикулы
        return self.article == other.article
# ========== Методы настройки объекта ==========
    def parseArticle(self, someArticle):
        # Метод проверяет корректность артикула. Артикул не должен содержать нелатинские буквы и пробелы
        article = someArticle
        if ' ' in article:
            print(article)
            article = article.replace(' ','')
        for letter in article:
            if letter not in VALID_SYMBOLS:
                if letter == 'С':
                    print(article)
                    article = article.replace('С','C')
        self.article = article
    def parseName(self, nameData):
        # Метод разбора переданного имени. Составляет из имени тип прибора, бренд и модель.
        # TODO: реализовать автоматическое определение товарных групп по типу прибора (хотя бы ТГ2)
        BRANDS = getBrands()
        for brand in BRANDS:
            if brand in nameData.upper():
                someBrand   = brand
                splitted    = nameData.split(brand)
                self.model  = splitted[1].strip()
                self.type   = splitted[0].strip().capitalize()
        try:            someBrand
        except:         someBrand   = ''
        try:            self.model
        except:         self.model   = ''
        try:            self.type
        except:         self.type   = ''
        if not self.article: self.parseArticle(self.model)
        self.setupBrand(correctBrand(someBrand))
    def setupBrand(self, brand):
        # Метод корректировки написания бренда. Если бренд находится в указанном списке, то его имя пишется заглавными буквами
        if brand.upper() not in self.CAPS_BRANDS: self.brand = brand.title()
        else: self.brand = brand.upper()
    def setupTradeGroups(self, tradeGroups):
        # Метод установки значений товарных групп. На вход подается словарь параметров с ключами пяти товарных групп
        self.TG = {}
        try:    self.TG['ТГ1'] = tradeGroups['ТГ1'].capitalize()
        except: self.TG['ТГ1'] = ''
        try:    self.TG['ТГ2'] = tradeGroups['ТГ2'].capitalize()
        except: self.TG['ТГ2'] = ''
        try:    self.TG['ТГ3'] = tradeGroups['ТГ3'].lower()
        except: self.TG['ТГ3'] = ''
        try:    self.TG['ТГ4'] = tradeGroups['ТГ4'].lower()
        except: self.TG['ТГ4'] = ''
        try:    self.TG['ТГ5'] = tradeGroups['ТГ5'].lower()
        except: self.TG['ТГ5'] = ''
        # Если ТГ1 или ТГ2 не определены, запускается функция автоматического определения
        '''if not self.TG['ТГ1'] or not self.TG['ТГ2']:
            self.TG['ТГ1'], self.TG['ТГ2'] = detectTG(self)'''
    def setupParameters(self, parameters):
        # Метод установки параметров для SKU. На вход подается словарь параметров <Наименование поля>=<Значение>
        self.parameters = OrderedDict()
        for key, value in parameters.items():
            self.parameters[key] = value
# ========== Методы доступа к атрибутам объекта ==========
    def getName(self):
        # Метод возвращает составное имя объекта (тип прибора + бренд + модель)
        return '{} {} {}'.format(self.type, self.brand, self.model)
    def fillFromDatabase(self, database):
        # Метод заполняет доступные поля, если товар с этими полями найден в базе данных
        if self.article in database.articlesArray:
            mirrorItem = database.getItemByArticle(self.article)
            if not self.TG['ТГ1'] and mirrorItem.TG['ТГ1']:
                print('filled!')
                self.TG['ТГ1'] = mirrorItem.TG['ТГ1']
            if not self.TG['ТГ2'] and mirrorItem.TG['ТГ2']:
                print('filled!')
                self.TG['ТГ2'] = mirrorItem.TG['ТГ2']
            if not self.TG['ТГ3'] and mirrorItem.TG['ТГ3']:
                print('filled!')
                self.TG['ТГ3'] = mirrorItem.TG['ТГ3']
            if not self.TG['ТГ4'] and mirrorItem.TG['ТГ4']:
                print('filled!')
                self.TG['ТГ4'] = mirrorItem.TG['ТГ4']
            if not self.TG['ТГ5'] and mirrorItem.TG['ТГ5']:
                print('filled!')
                self.TG['ТГ5'] = mirrorItem.TG['ТГ5']
            if mirrorItem.parameters:
                print(self)
                for key in mirrorItem.parameters.keys():
                    try:
                        self.parameters[key]
                    except:
                        if mirrorItem.parameters[key]:
                            self.parameters[key] = mirrorItem.parameters[key]
                            print('Parameter "{}" filled from database with value "{}"'.format(key, self.parameters[key]))
            
# ========== Методы класса ==========
    @classmethod
    def fromData(cls, data):
        # Метод класса создает экземпляр на основе некоторого набора данных, преданного методу
        tradeGroups = {}
        parameters  = {}
        try:    name    = data['Название']
        except: name    = ''
        try:    article = data['Артикул']
        except: article = ''
        try:    color   = data['Цвет']
        except: color   = ''
        try:    tradeGroups['ТГ1'] = data['Товарные группы']['ТГ1']
        except: tradeGroups['ТГ1'] = ''
        try:    tradeGroups['ТГ2'] = data['Товарные группы']['ТГ2']
        except: tradeGroups['ТГ2'] = ''
        try:    tradeGroups['ТГ3'] = data['Товарные группы']['ТГ3']
        except: tradeGroups['ТГ3'] = ''
        try:    tradeGroups['ТГ4'] = data['Товарные группы']['ТГ4']
        except: tradeGroups['ТГ4'] = ''
        try:    tradeGroups['ТГ5'] = data['Товарные группы']['ТГ5']
        except: tradeGroups['ТГ5'] = ''
        try:
            for key, value in data['Параметры'].items():
                parameters[key] = value
        except: parameters  = {}
        return cls(article      = article,
                   name = name,
                   color        = color,
                   tradeGroups  = tradeGroups,
                   parameters   = parameters)