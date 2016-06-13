from equities import *
import random

# this thing tests the calculator by simulating 100000 heads up sng's and verifying that the win count matches up with the calculated one.
# however it doesn't deal the cards; it assumes that the given equities are correct, and generates random numbers between 0 and 1 to determine whether a hand is won or lost. will deal the cards out later.

cards=['As', 'Ah', 'Ad', 'Ac', 'Ks', 'Kh', 'Kd', 'Kc', 'Qs', 'Qh', 'Qd', 'Qc', 'Js', 'Jh', 'Jd', 'Jc', 'Ts', 'Th', 'Td', 'Tc', '9s', '9h', '9d', '9c', '8s', '8h', '8d', '8c', '7s', '7h', '7d', '7c', '6s', '6h', '6d', '6c', '5s', '5h', '5d', '5c', '4s', '4h', '4d', '4c', '3s', '3h', '3d', '3c', '2s', '2h', '2d', '2c']

def cookie_monster(zap, kablooie): # gives equity of a pair of cards
    if zap[0]==kablooie[0]: # pair
        thingy=''
    elif zap[1]==kablooie[1]: # suited
        thingy='s'
    else:
        thingy='o'
    return equities[rankedcards.index(zap[0]+kablooie[0]+thingy)]

def leppard(): # hehehe
    potato=random.randint(0,51)
    tomato=random.randint(0,50) # cheap way of dealing with the "pick two" condition
    if tomato<potato:
        return cookie_monster(cards[tomato],cards[potato])
    else:
        return cookie_monster(cards[potato],cards[tomato+1])

# n (total big blinds of both players) is picked in advance, and the shove range is taken from the data values page.
# both of these can be modified to reflect any given stack size and strategy, as long as the array length is right.

n=15
shove=[168, 168, 168, 168, 168, 166, 168, 154, 168, 137, 166, 127, 162, 121, 153, 116, 141, 111, 133, 107, 127, 106, 121, 101, 115, 98, 111, 95, 106, 94, 110, 95, 111, 95, 116, 101, 123, 106, 132, 106, 139, 111, 150, 116, 161, 121, 166, 127, 168, 137, 168, 152, 168, 166, 168, 168]

shove.append(168) # stack size 2*n-1 (not in array)
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
                if yourstack>=n: # win sng
                    return "win"
                else:
                    yourstack*=2
                    something=not something
            else: # lose
                if yourstack<=n: # lose sng
                    return "lose"
                else:
                    yourstack = yourstack*2-2*n
                    something=not something

chicken=0
yourstack=int(raw_input('starting stack? (both stack sizes add to '+str(2*n)+') '))
something=bool(int(raw_input('start as sb? 1 for true, 0 for false ')))
for x in range(100000):
    blah=monkey(yourstack,something)
    if blah == "win":
        chicken+=1

print chicken
