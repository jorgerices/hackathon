class Card():
    def __init__(self, name, cost, url_img):
        self.name = name 
        self.cost = cost
        self.url_img = url_img

class Unit(Card):
    def __init__(self, name, cost,power, res, url_img):
        super().__init__(name,cost, url_img)
        self.power = power 
        self.res = res

    def attack (self, target):
        if isinstance (target, Unit):
            target.res = target.res - self.power
        else:
            print ("Target must be a unit!try it again")
            raise Exception("Target must be a unit!")

class Effect(Card):
    def __init__(self, name, cost, text, stat, magnitude, url_img):
        super().__init__(name, cost, url_img)
        self.text = text
        self.stat = stat
        self.magnitude = magnitude

    def useEffect(self, target):
        if type(target).__name__ == 'Unit':
            if self.stat == 'res':
                target.res += self.magnitude
            elif self.stat == 'power':
                target.power += self.magnitude
        else:
            raise Exception("Target must be a unit!")
        return self

class Player():
    def __init__(self, name, player_number, lives=20):
        self.name = name
        self.player_number = player_number
        self.lives = lives

    def play(self, card_name, target_number):
        if target_number == 1: target = player1
        else: target = player2
        for card in cards:
            if card_name == card.name:
                print(f'{self.name} is using {card.name} on {target.name}')
            else: continue

    def printPlayerInfo(self):
        print('-' * 20)
        print(f'Player name: {self.name}\nPlayer number: {self.player_number}\nPlayer Lives: {self.lives}')
        print('-' * 20)

# Effect Cards
# hardAlgorithm = Effect('Hard Algorithm', 2, "Increase target's resistance by 3", 'res', 3, 'https://media.makeameme.org/created/algorithms-5ca443.jpg')
# promise = Effect('Promise', 1, "Reduce target's resistance by 2", 'res', -2, 'https://media.makeameme.org/created/i-promise-jmjjcy.jpg')
# pairProgramming = Effect('Pair Programming', 3, "Increase target's power by 2", 'power', 2, "https://cdn.hackernoon.com/hn-images/1*zRrkoarX94CUZe3-NrSYGg.png")

# Unit Cards
# Red_Jinja=Unit("Red Ninja", 3,3,4,"https://www.karatemart.com/images/products/large/red-ninja-uniform-800583.jpg")
# Black_Jinja=Unit("Black Ninja",4,5,4,"https://pbs.twimg.com/profile_images/1336354559048880129/yIQSfFLy_400x400.jpg")

# All cards list
# cards = [hardAlgorithm, promise, pairProgramming, Red_Jinja, Black_Jinja]

# -------------------- Testing ----------------------------
# Testing if Unit           name,  cost,pow, res
# card11 = Unit('test Card-11', 1, 2, 3)
# card22 = Unit('test Card-22', 4, 5, 6)
# print (type(card11).__name__)

# Testing effects
# hardAlgorithm.useEffect(card22) # It works! :D 

# Testing Units
# card1=Unit("Red Ninja",3,3,4,"https://i.blogs.es/a19bfc/testing/450_1000.jpg")
# card2=Unit("Black Ninja",4,5,4,"https://i.blogs.es/a19bfc/testing/450_1000.jpg")
# card1.attack(card2)
# print (card2.name, "disminuyó su resistencia a: ",card2.res)
# print (card1.res)
# card2.attack(card1)
# print ( card1.name, "disminuyó su resistencia a: ",card1.res)

# Other testings
# for card in cards:  # Test if working properly (export to HTML) 
#     print('-' * 20)
# print(f'Card name: {card.name} \nCard cost: {card.cost}')
# print('-' * 20)

# Player testing
# player1 = Player('Testing Player 1','1')
# player2 = Player('Testing Player 2', '2')
# player1.play('Promise', '2')
# player1.printPlayerInfo()
# ------------------- End of Testing ------------------------