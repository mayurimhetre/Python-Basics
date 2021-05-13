####### Select a crad from Deck of crads #####
import random
cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    print(card[0])
    print(rank[0])
    print("We have selected '{}' of '{}' ".format(rank[0],card[0]))
    

pick_a_card()


######## Roll a dice ########################
import random

dice = [1,2,3,4,5,6]

def  dice_select():
    dice1 = random.choices(dice)
    print("Value on dice after rolling:{}".format(dice1[0]))
dice_select()



### two dice at a the same time 
dice11 = [1,2,3,4,5,6]
dice22 = [1,2,3,4,5,6]

def  dice_select1():
    dice1 = random.choices(dice11)
    dice2 = random.choices(dice22)
    print("Value on dice after rolling Dice1 :{} and Dice2 : {}".format(dice1[0],dice2[0]))
dice_select1()
