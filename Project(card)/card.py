from random import shuffle

#카드의 종류와 숫자를 적어놓은 클래스
class Cards :
    global suites, values
    suites = ['Hearts', 'Diamonds' , 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5,', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self) :
        pass

#카드를 이용해 모든 카드를 넣어 놓은 덱을 시작과 함께 만든다.
#덱을 섞는 기능과, 한 장씩 뽑는 기능이 구현되어 있다.
class Deck (Cards):
    def __init__(self) :
        self.mycardset = []
        for i in range(0, len(suites)) :
            for j in range(0, len(values)) :
                self.mycardset.append('%s of %s'% (values[j] ,suites[i]))
    #셔플을 이용한 카드 섞기
    def shuffleDeck(self):
        shuffle(self.mycardset)

    #카드를 한 장 뽑는다.
    def popCard(self):
        return self.mycardset.pop()

#여러명의 사용자를 구현하는 클래스
#이름을 사용자로부터 부여받는다.
class Player(object) :
    def __init__(self, nickname) :
        self.nickname = nickname
        self.__cards = []

    #프린트 시의 양식
    def __str__(self) :
        return "Player %s has %s"% (self.nickname, self.cards)

    #플레이어가 가진 모든 카드 출력
    @property
    def cards(self):
        return self.__cards

    #플레이어에게 한 장의 카드 추가
    @cards.setter
    def cards(self, card) :
        self.__cards.append(card)

if __name__ == "__main__":
    deck = Deck()

    print(f'[Current Deck]\n{deck.mycardset}')
    print()
    shuffled_deck = deck.shuffleDeck()
    print(f'[Shuffled Deck]\n{shuffled_deck.mycardset}')
    print()

    player1 = Player("JH")
    player2 = Player("CY")

    for _ in range(4) :
        player1.cards = shuffled_deck.popCard()
        player2.cards = shuffled_deck.popCard()
    print(player1)
    print(player2)