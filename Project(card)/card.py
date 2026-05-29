from random import shuffle

class Cards :
    global suites, values
    suites = ['Hearts', 'Diamonds' , 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5,', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self) :
        pass

class Deck (Cards):
    def __init__(self) :
        self.mycardset = []
        for i in range(0, len(suites)) :
            for j in range(0, len(values)) :
                self.mycardset.append('%s of %s'% (values[j] ,suites[i]))

    def shuffleDeck(self):
        shuffle(self.mycardset)


    def popCard(self):
        return self.mycardset.pop()

class Player(object) :
    def __init__(self, nickname) :
        self.nickname = nickname
        self.__cards = []