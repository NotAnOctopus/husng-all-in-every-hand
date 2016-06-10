import random
from equities import rankedcards, equities, f, g, h
import numpy as numpy
from scipy.sparse import linalg # this. this sparse linalg solver is the only reason i installed numpy and scipy. and it took me two bloody hours to find out how to install the damn things. why does it have to be so complicated? and what the hell is pip and why do i have to upgrade it every five nanoseconds?

# this thing is a calculator to work out optimal shove ranges against someone going all in every hand in a poker heads up sit and go, where you know that they're going all in every hand.
# yeah some people genuinely really do this.
# this is a toy version where blinds are 1/2 and total start stacks are 8
# j=shovesb[n] means if you have a stack size of n in the sb, you shove top j+1 out of 169 hands ranked in order (i.e. top hand is aces and bottom hand is 32off)
# same with shovebb

shovesb=[168, 168, 160, 150, 140, 150, 160] # this is a starting point; these ranges are way off
shovebb=[168, 168, 168, 150, 140, 150] # so are these

fish=0.0

def yourface(shovesb, shovebb):
    [aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn]=[-f[shovesb[2]], -g[shovesb[2]], -f[shovebb[3]], -g[shovebb[3]], -f[shovesb[3]], -g[shovesb[3]], -g[shovebb[4]], -g[shovesb[4]], -h[shovebb[5]], -g[shovebb[5]], -h[shovesb[5]], -g[shovesb[5]], -h[shovesb[6]], -g[shovesb[6]]]
    bullshit=numpy.matrix([
    [1, 0, 0,-0.5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1,-0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0,-0.5, 0, 0, 0, 0],
    [bb,0, 0, 1, 0, 0,aa, 0, 0, 0, 0, 0],
    [0,dd, 0, 0, 1, 0, 0, 0, 0, 0, 0,cc],
    [0, 0,ff, 0, 0, 1, 0, 0, 0, 0,ee, 0],
    [0, 0, 0,gg, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0,hh, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0,ii, 0,jj, 0, 0, 1, 0, 0, 0],
    [0, 0,kk, 0, 0, 0,ll, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0,-0.5, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0,mm, 0,nn,0, 0, 1]]) # magic
    balloon = [0, 0, 0, 0, 0, 0, f[shovebb[4]], f[shovesb[4]], f[shovebb[5]], f[shovesb[5]], 0.5, f[shovesb[6]]]
    return linalg.spsolve(bullshit,balloon) # basically this algorithm is a big Ax=b matrix calculation a bazillion times

while True: # random walk
    value = random.randint(1,8)
    direction=random.randint(1,2)
    walrus=shovesb[:]
    octopus=shovebb[:]
    if value<6:
        if walrus[value+1]==168: # cheap method of getting rid of index errors
            walrus[value+1]=167
        elif direction==1:
            walrus[value+1]+=1
        else:
            walrus[value+1]-=1
    else:
        if octopus[value-3]==168:
            octopus[value-3]=167
        elif direction==1:
            octopus[value-3]+=1
        else:
            octopus[value-3]-=1
    cauliflower=yourface(walrus,octopus)
    result=sum(w for w in cauliflower)
    if result>fish:
        fish = result
        shovesb=walrus[:]
        shovebb=octopus[:]
    if result>5.256723: # unique optimal. in this case it happens to be the same as the nash chart
        print shovesb, shovebb
        fish = result
        print result
        print cauliflower
        break

# the output should be
# [168, 168, 168, 166, 155, 166, 168] [168, 168, 168, 168, 168, 168]
# 5.25672317619
# [ 0.125       0.12559684  0.25119368  0.25        0.375       0.37569033
#   0.5         0.50238736  0.625       0.62566128  0.75119368  0.75      ]
