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
        self.busted = False
        self.hand = []
        self.fancy = []
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

    def summ(self):
        ess = 0
        sum1 = 0
        for i in self.hand:
            if i == [1,11]:
                ess+=1
            else:
                sum1 +=i
        sum1 += 11*ess
        for i in range(ess):
            if sum1>21:
                sum1-=10
        if sum1>21:
            self.busted = True
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
        self.spiller2 = Player(self.deck)
        self.dealer = Dealer(self.deck, flipped=True)

        self.spillere = []
        self.spillere.append(self.spiller)
        self.spillere.append(self.spiller2)
        self.bet = 200

    def spill(self):
        bett = int(input("Kva øynskjyer dykk å spelle om dinna runda (Nynorsk før extrapoeng)>>"))
        self.bet = bett
        for i in self.spillere:
            i.cre_hand()
        self.dealer.cre_hand()
        for i in self.spillere:
            if i.hand == self.dealer.hand:
                break

            while True:
                print(i.fancy, i.summ())
                print(self.dealer.fancy)
                a = input("Vil du hitte eller stande? (h/s) >>")
                if a == "h":
                    i.hit()
                    if i.summ() > 21:
                        print(i.fancy, i.summ())
                        i.busted = True
                        print("BUSTED")
                        break
                else:
                    break
        #Hvis det er en spiller så kan man bruke metoden i dealer klassen, men det er ikke fordelaktig her.
        while self.dealer.summ() < 21:
            for i in self.spillere:
                if i.summ() < self.dealer.summ():
                    i.busted = True
            self.dealer.hit()
        o = 0
        for i in self.spillere:
            o+=1

            if i.busted == True:
                i.chips-=self.bet
                print(f"Spiller {o} tapte, og har nå {i.chips} igjen")
            else:
                i.chips +=self.bet
                print(f"Spiller {o} vant, og har nå {i.chips} igjen")



a = Blackjack()
while True:
    a.spill()
    stoppe = input("Ønsker du å foprtsette (y) >>")
    if stoppe!= "y":
        break

