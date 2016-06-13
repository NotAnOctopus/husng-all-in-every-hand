from equities import *
import random

cards=['As', 'Ah', 'Ad', 'Ac', 'Ks', 'Kh', 'Kd', 'Kc', 'Qs', 'Qh', 'Qd', 'Qc', 'Js', 'Jh', 'Jd', 'Jc', 'Ts', 'Th', 'Td', 'Tc', '9s', '9h', '9d', '9c', '8s', '8h', '8d', '8c', '7s', '7h', '7d', '7c', '6s', '6h', '6d', '6c', '5s', '5h', '5d', '5c', '4s', '4h', '4d', '4c', '3s', '3h', '3d', '3c', '2s', '2h', '2d', '2c']

def cookie_monster(zap, kablooie):
    if zap[0]==kablooie[0]: # pair
        thingy=''
    elif zap[1]==kablooie[1]: # suited
        thingy='s'
    else:
        thingy='o'
    return equities[rankedcards.index(zap[0]+kablooie[0]+thingy)]

def leppard():
    potato=random.randint(0,51)
    tomato=random.randint(0,50)
    if tomato<potato:
        return cookie_monster(cards[tomato],cards[potato])
    else:
        return cookie_monster(cards[potato],cards[tomato+1])


shove=[168, 168, 168, 168, 168, 166, 168, 152, 168, 139, 166, 128, 160, 121, 150, 117, 144, 113, 136, 107, 127, 103, 121, 98, 115, 95, 111, 91, 107, 91, 106, 89, 101, 86, 97, 82, 95, 79, 91, 76, 89, 74, 85, 71, 81, 71, 79, 70, 76, 67, 74, 65, 74, 64, 71, 64, 71, 64, 71, 61, 70, 59, 69, 59, 67, 59, 64, 58, 64, 57, 60, 54, 59, 54, 58, 51, 57, 49, 55, 49, 54, 49, 53, 49, 51, 48, 49, 47, 49, 47, 49, 46, 48, 46, 47, 44, 46, 42, 46, 41, 47, 44, 49, 46, 49, 47, 51, 48, 54, 49, 54, 49, 57, 49, 58, 51, 59, 53, 59, 54, 59, 54, 61, 55, 61, 56, 64, 57, 65, 57, 67, 59, 70, 59, 70, 59, 70, 60, 71, 61, 71, 61, 71, 64, 74, 64, 74, 64, 74, 65, 76, 67, 79, 70, 84, 71, 89, 74, 91, 76, 95, 79, 97, 81, 101, 85, 106, 89, 108, 91, 112, 91, 115, 95, 117, 95, 123, 101, 132, 106, 140, 111, 150, 117, 161, 123, 166, 127, 168, 137, 168, 153, 168, 166, 168, 168]

shove.append(168)
shove.append(168)

def monkey(yourstack, something):
    while True:
        whatever = leppard()
        if whatever < equities[shove[yourstack*2-2+int(something)]]: # fold
            if something:
                yourstack-=1
                something=False
            else:
                yourstack-=2
                something=True
        else: # all-in
            result=random.random()
            if whatever>result: # win
                if yourstack>=50: # win sng
                    return "win sng"
                else:
                    yourstack*=2
                    something=not something
            else: # lose
                if yourstack<=50: # lose sng
                    return "lose sng"
                else:
                    yourstack = yourstack*2-100
                    something=not something

count=0
yourstack=int(raw_input('starting stack? (both stack sizes add to 100) '))
something=bool(raw_input('start as sb? '))
for x in range(100000):
    blah=monkey(yourstack,something)
    if blah == "win sng":
        count+=1

print count
