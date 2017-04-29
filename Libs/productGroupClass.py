# В модуле описан класс Товарной группы

class ProductGroupStructure:
    def __init__(self, name, level, parent = None, children = ()):
        self.name       = name      # Название товарной группы
        self.level      = level     # Уровень товарной группы (от 1 до 5)
        self.parent     = parent    # Родительская надгруппа, если есть
        self.children   = children  # Группы - потомки, если есть
    def __str__(self):
        return self.name
    def addChild(self, child):
        # Метод добавляет группу-потомка
        if isinstance(child, ProductGroupStructure):
            child.level     = self.level + 1
            child.parent    = self
            self.children.add(child)
        elif isinstance(child, str):
            if self.level == 1:
                newGroup = ProductGroup2(child, self)
                self.addChild(newGroup)
            elif self.level == 2:
                newGroup = ProductGroup3(child, self)
                self.addChild(newGroup)
            elif self.level == 3:
                newGroup = ProductGroup4(child, self)
                self.addChild(newGroup)
            elif self.level == 4:
                newGroup = ProductGroup5(child, self)
                self.addChild(newGroup)
            else:
                raise IndexError ('Can not add child to 5th Product Group!')
        else:
            raise TypeError ('Added child must be ProductGroup class or String!')
    def hasLegacy(self, parentName):
        # Метод возвращает True, если одним из предков группы является группа с названием parentName
        if self.parent:
            if self.parent.name == parentName:  return True
            else:                               return self.parent.hasLegacy(parentName)
        return False
    def hasParent(self, parentName):
        # Метод возвращает True, если если непосредственным предком группы является группа с названием parentName
        if self.parent:
            if self.parent.name == parentName:  return True
        return False
    def hasDescendent(self, childName):
        # Метод возвращает True, если одним из потомков группы является группа с названием childName
        if self.children:
            for child in self.children:
                if child.name == childName: return True
                else:                       child.hasChild(childName)
        return False
    def hasChild(self, childName):
        # Метод возвращает True, если одним из потомков группы является группа с названием childName
        if self.children:
            for child in self.children:
                if child.name == childName: return True
        return False

class ProductGroup1(ProductGroupStructure):
    # Класс Товарной группы 1
    def __init__(self, name):
        super().__init__(name, 1)

class ProductGroup2(ProductGroupStructure):
    # Класс Товарной группы 2
    def __init__(self, name, parent):
        super().__init__(name, 2, parent)

class ProductGroup3(ProductGroupStructure):
    # Класс Товарной группы 3
    def __init__(self, name, parent):
        super().__init__(name, 3, parent)

class ProductGroup4(ProductGroupStructure):
    # Класс Товарной группы 4
    def __init__(self, name, parent):
        super().__init__(name, 4, parent)

class ProductGroup5(ProductGroupStructure):
    # Класс Товарной группы 5
    def __init__(self, name, parent):
        super().__init__(name, 5, parent)