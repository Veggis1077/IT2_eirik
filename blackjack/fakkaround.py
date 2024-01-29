import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Player:
    def __init__(self, deck, flipped=False, busted=False, chips=1000):
        self.busted = busted
        self.flipped = flipped
        self.deck = deck
        self.hand = []  # Navn type og verdi
        self.fancy = []  # Visedr kortet
        self.chips = chips

    def deal(self):
        # Bør bytte ut med bare return self.deck.pop()

        a = self.deck[-1]
        self.deck.pop()
        return a

    def cre_hand(self):
        for i in range(2):
            j = self.deal()
            self.hand.append(j[-1])
            if not self.flipped:
                self.fancy.append(j[1] + " of " + j[0])
            else:
                if i == 1:
                    self.fancy.append("FLIPPED")
                else:
                    self.fancy.append(j[1] + " of " + j[0])
        return self.fancy

    def hit(self):
        j = self.deal()
        self.hand.append(j[-1])
        self.fancy.append(j[1] + " of " + j[0])
        return self.fancy

    def clear_hand(self):

        #self.spilldekk = Deck()  # Legger tilbakje ogs tokker (init dette vet du breh)

        self.hand = []
        self.fancy = []
    def summ(self):
        ess = 0
        s = 0
        for i in self.hand:
            if i == [1, 11]:
                ess+=1
            else:
                s+=i
        sum1 =  s + ess*11
        if sum1 > 21:
            while True:
                if ess*11 -10 >0:
                    sum1-=10
                else:
                    self.busted = True
                    break
        return sum1



class Dealer(Player):
    def __init__(self, deck, flipped):
        super().__init__(deck, flipped, chips=1000)

    def draw_cards(self, msum):
        while self.summ() < 22 and msum > self.summ():
            self.hit()



class Blackjack:#Objekt spill
    def __init__(self, players_list=[]):
        self.player_list = players_list
        self.deck = []
        for suit in suits:
            for rank in values:
                self.deck.append([suit, rank, values[rank]])
        random.shuffle(self.deck)
        self.spiller = Player(self.deck)
        self.dealer = Dealer(self.deck, flipped=True)
        self.spillere = []
        self.spillere.append([self.spiller, self.dealer])

    def spill(self):
        for i in self.spillere[0]:
            i.cre_hand()
            if i != self.spillere[-1]:
                print(i.fancy, sum(i.hand))
            else:
                print(i.fancy)

        for i in range(len(self.spillere)):
            while True:
                print(self.dealer.fancy)
                if self.spillere[0][i].busted == True:
                    print("busted")
                    break
                print(self.spillere[0][i].fancy, sum(self.spillere[0][i].hand))
                a = input("Vil du stande eller hitte? (hit/stand) >>")
                if a == "stand":
                    break
                elif self.spillere[0][i].summ() > 21:
                    self.spillere[0][i].busted = True
                    self.spillere[0][0].chips-=100
                    print("busted")
                    break
                else:
                    self.spillere[0][i].hit()
        if not self.spillere[0][0].busted:
            self.spillere[0][-1].draw_cards(sum(self.spillere[0][0].hand))





a = Blackjack()
a.spill()

