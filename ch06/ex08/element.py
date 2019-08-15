class Element():
    def __init__(self, nsnDict):
        self.__name = nsnDict['name']
        self.__symbol = nsnDict['symbol']
        self.__number = nsnDict['number']

    @property
    def name(self):
        print('get name')
        return self.__name

    @property
    def symbol(self):
        print('get symbol')
        return self.__symbol

    @property
    def number(self):
        print('get number')
        return self.__number

    def __str__(self):
        return self.__name + ', ' + self.__symbol + ', ' + str(self.__number)
