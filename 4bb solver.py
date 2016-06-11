import numpy as numpy
from scipy.sparse import linalg
import random
from equities import rankedcards, equities, f, g, h
# this. this sparse linalg solver is the only reason i installed numpy and scipy. and it took me two bloody hours to find out how to install the damn things. why does it have to be so complicated? and what the hell is pip and why do i have to upgrade it every five nanoseconds?

# this thing is a calculator to work out optimal shove ranges against someone going all in every hand in a poker heads up sit and go, where you know that they're going all in every hand.
# yeah some people genuinely really do this.
# this is a toy version where blinds are 1/2 and total start stacks are 8
# j=shove[n] means if your stack size and position are indicated by n in the array below, you shove top j+1 out of 169 hands ranked in order (i.e. top hand is aces and bottom hand is 32off)

# pos: bb1  sb1  bb2  sb2  bb3  sb3  bb4  sb4  bb5  sb5  bb6  sb6
shove=[168, 168, 168, 160, 150, 150, 140, 140, 150, 160, 168, 160] # these ranges are way too tight; it's a starting point

fish=0.0

def yourface(shove):
    [aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn]=[-f[shove[3]], -g[shove[3]], -f[shove[4]], -g[shove[4]], -f[shove[5]], -g[shove[5]], -g[shove[6]], -g[shove[7]], -h[shove[8]], -g[shove[8]], -h[shove[9]], -g[shove[9]], -h[shove[11]], -g[shove[11]]]
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
    balloon = [0, 0, 0, 0, 0, 0, f[shove[6]], f[shove[7]], f[shove[8]], f[shove[9]], 0.5, f[shove[11]]]
    return linalg.spsolve(bullshit,balloon) # basically this algorithm is a big Ax=b matrix calculation a bazillion times

while True: # random walk
    value = random.randint(3,10)
    walrus=shove[:]
    if value==10:
        value+=1
    if walrus[value]==168: # cheap method of getting rid of index errors
        blobfish=True
        walrus[value]=167
    else:
        blobfish=False
        walrus[value]+=1 # try making the range bigger
    cauliflower=yourface(walrus)
    result=sum(w for w in cauliflower)
    if result>fish:
        fish = result
        shove=walrus[:]
    elif blobfish==False: # if making it bigger doesn't work, try making it smaller
        walrus[value]-=2
        cauliflower=yourface(walrus)
        result=sum(w for w in cauliflower)
        if result>fish:
            fish = result
            shove=walrus[:]
    if result>5.256723: # unique optimal. in this case it happens to be the same as the nash chart
        print shove
        fish = result
        print result
        print cauliflower
        break

# the output should be
# [168, 168, 168, 168, 168, 166, 168, 155, 168, 166, 168, 168]
# 5.25672317619
# [ 0.125       0.12559684  0.25119368  0.25        0.375       0.37569033
#   0.5         0.50238736  0.625       0.62566128  0.75119368  0.75      ]
