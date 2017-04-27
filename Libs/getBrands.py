# Считываем названия брендов из файла и заносим их в массив названий BRANDS
def getBrands():
    BRANDS = []
    with open('DataFolder\\brands.txt','r') as brandFile:
        array = brandFile.readlines()
        for brand in array:
            BRANDS.append(brand.strip())
    return BRANDS
# ====================