class Element():
    def __init__(self, nsnDict):
        self.name = nsnDict['name']
        self.symbol = nsnDict['symbol']
        self.number = nsnDict['number']

    def dump(self):
        print(self.name, self.symbol, self.number)
