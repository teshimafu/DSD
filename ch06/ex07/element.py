class Element():
    def __init__(self, nsnDict):
        self.name = nsnDict['name']
        self.symbol = nsnDict['symbol']
        self.number = nsnDict['number']

    def __str__(self):
        return self.name + ', ' + self.symbol + ', ' + str(self.number)
