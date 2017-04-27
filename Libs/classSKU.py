# Модуль описывает класс SKU, который представляет из себя интерфейс товара - модели техники на продажу

class SKU:
    CAPS_BRANDS = ('BORA', 'BORK', 'SMEG')
    def __init__(self,
                 model = '',
                 article = '',
                 brand = '',
                 color = '',
                 tradeGroups = {},
                 parameters = {}):
        self.model = model
        self.article = article
        self.setupBrand(brand)
        self.setupTradeGroups(tradeGroups)
        self.color = color.lower()
        self.setupParameters(parameters)
# ========== Перегруженные методы ==========
    def __str__(self):
        # Метод строковго представления объекта
        return '{} {} {}'.format(self.TG['ТГ2'], self.brand, self.model)
    def __eq__(self, other):
        # Метод поврехностного сравнения объектов. Две SKU считаются равными, если равны их артикулы
        return self.article == other.article
# ========== Методы настройки объекта ==========
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
    def setupParameters(self, parameters):
        # Метод установки параметров для SKU. На вход подается словарь параметров <Наименование поля>=<Значение>
        self.parameters = {}
        for key, value in parameters: self.parameters[key] = value
# ========== Методы класса ==========
    @classmethod
    def fromData(cls, data):
        # Метод класса создает экземпляр на основе некоторого набора данных, преданного методу
        tradeGroups = {}
        parameters  = {}
        try:    model   = data['Модель']
        except: model   = ''
        try:    article = data['Артикул']
        except: article = ''
        try:    brand   = data['Бренд']
        except: brand   = ''
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
        return cls(model        = model,
                   article      = article,
                   brand        = brand,
                   tradeGroups  = tradeGroups,
                   color        = color,
                   parameters   = parameters)