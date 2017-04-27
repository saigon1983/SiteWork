# Модуль описывает класс SKU, который представляет из себя интерфейс товара - модели техники на продажу

class SKU:
    def __init__(self,
                 model = '',
                 article = '',
                 brand = '',
                 gg1 = '',
                 gg2 = '',
                 gg3 = '',
                 gg4 = '',
                 gg5 = ''):
        self.model = model
        self.article = article
        self.setupBrand(brand)
        self.gg1 = gg1.capitalize()
        self.gg2 = gg2.capitalize()
        self.gg3 = gg3.capitalize()
        self.gg4 = gg4.capitalize()
        self.gg5 = gg5.capitalize()
    def __str__(self):
        return '{} {} {}'.format(self.gg2, self.brand, self.model)

    def setupBrand(self, brand):
        if brand.upper() not in ['BORA', 'BORK', 'SMEG']: self.brand = brand.title()
        else: self.brand = brand.upper()

    @classmethod
    def fromData(cls, data):
        try: model   = data['Модель']
        except: model = ''
        try: article   = data['Артикул']
        except: article = ''
        try: brand   = data['Бренд']
        except: brand = ''
        try: gg1   = data['ТГ1']
        except: gg1 = ''
        try: gg2   = data['ТГ2']
        except: gg2 = ''
        try: gg3   = data['ТГ3']
        except: gg3 = ''
        try: gg4   = data['ТГ4']
        except: gg4 = ''
        try: gg5   = data['ТГ5']
        except: gg5 = ''
        return cls(model = model, article = article, brand = brand, gg1 = gg1, gg2 = gg2, gg3 = gg3, gg4 = gg4, gg5 = gg5)