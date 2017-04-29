# Считываем названия брендов из файла и заносим их в массив названий BRANDS
def getBrands():
    BRANDS = []
    with open('DataFolder\\brands.txt','r') as brandFile:
        array = brandFile.readlines()
        for brand in array:
            BRANDS.append(brand.strip())
    return BRANDS
# ====================
# Корректируе возможные неверные написания брендов и возвращаем правильный результат
def correctBrand(someBrand):
    BRANDS = {'BONECRUSHER':        'BONE CRUSHER',
              'COLDVINE':           'COLD VINE',
              'COLDWINE':           'COLD VINE',
              'COLD WINE':          'COLD VINE',
              'DEDIETRICH':         'DE DIETRICH',
              'DE LONGHI':          'DELONGHI',
              'ELECTRONICS DELUXE': 'ELECTRONICSDELUXE',
              'ELECTRONICS DELUX':  'ELECTRONICSDELUXE',
              'ELECTRONICS DE LUXE':'ELECTRONICSDELUXE',
              'ELECTRONICS DE LUX': 'ELECTRONICSDELUXE',
              'ELECTRONIC DELUX':   'ELECTRONICSDELUXE',
              'ELECTRONIC DELUXE':  'ELECTRONICSDELUXE',
              'ELECTRONIC DE LUX':  'ELECTRONICSDELUXE',
              'ELECTRONIC DE LUXE': 'ELECTRONICSDELUXE',
              'EURO CAVE':          'EUROCAVE',
              'FULGOR':             'FULGOR MILANO',
              'GORENJE +':          'GORENJE+',
              'HOTPOINT':           'HOTPOINT-ARISTON',
              'ARISTON':            'HOTPOINT-ARISTON',
              'INSINK ERATOR':      'IN SINK ERATOR',
              'INSINKERATOR':       'IN SINK ERATOR',
              'INDELB':             'INDEL B',
              'IOMABE':             'IO MABE',
              'MABE':               'IO MABE',
              'IPINDUSTRIE':        'IP INDUSTRIE',
              'IP INDUSTRY':        'IP INDUSTRIE',
              'I-ROBOT':            'IROBOT',
              'I ROBOT':            'IROBOT',
              'JETAIR':             'JET AIR',
              'KITCHENAID':         'KITCHEN AID',
              'LASOMMELIERE':       'LA SOMMELIERE',
              'MITSUBISHI':         'MITSUBISHI ELECTRIC',
              'MITSUBISHIELECTRIC': 'MITSUBISHI ELECTRIC',
              'VZUG':               'V-ZUG',
              'V ZUG':              'V-ZUG',
              'ZUG':                'V-ZUG',
              'VEST FROST':         'VESTFROST',
              'ZIGMUND & SHTAIN':   'ZIGMUND&SHTAIN',
              'ZIGMUND SHTAIN':     'ZIGMUND&SHTAIN',
              'ZIGMUNDSHTAIN':      'ZIGMUND&SHTAIN',
              'ZIGMUND AND SHTAIN': 'ZIGMUND&SHTAIN',
              'Z&S':                'ZIGMUND&SHTAIN'}
    try:    return BRANDS[someBrand.upper()]
    except: return someBrand