import numpy as numpy
from scipy.sparse import linalg
from scipy.sparse import csr_matrix
import random
from equities import rankedcards, equities, f, g, h

fish=0.0

n=int(raw_input('n? ')) # this is the number of big blinds in both stacks combined
s=4*n-4 # number of rows in matrix
shove = [168]*3 + [100]*(s-3) # very crude guesstimate for ranges

shove[-2] = 168 # big blind when your stack is n-1

# rows
diagonalrow=[k for k in range(s)]
foldrow=[k for k in range(3,s)]
minushalvesrow=[0,1,2,s-2]
winoddrow=[2*k+1 for k in range(1,n-1)]
winevenrow=[2*k for k in range(2,n-1)]
loseoddrow=[s-2*k+1 for k in range(1,n-1)]
loseevenrow=[s-2*k for k in range(2,n-1)]
# columns
diagonalcolumn=[k for k in range(s)]
foldcolumn=[k-3 for k in range(3,s)]
minushalvescolumn=[3,2,7,s-5]
winoddcolumn=[4*k+2 for k in range(1,n-1)]
winevencolumn=[4*k+3 for k in range(2,n-1)]
loseoddcolumn=[s-4*k-2 for k in range(1,n-1)]
loseevencolumn=[s-4*k-1 for k in range(2,n-1)]

snowmen_are_creepy = diagonalrow + foldrow + minushalvesrow + winoddrow + winevenrow + loseoddrow + loseevenrow

will_someone_hire_me_please = diagonalcolumn + foldcolumn + minushalvescolumn + winoddcolumn + winevencolumn + loseoddcolumn + loseevencolumn

def alice_stinks(shove):
    # data
    diagonaldata=[1 for k in range(s)]
    folddata=[-g[shove[k]] for k in range(3,s)]
    minushalvesdata=[-0.5,-0.5,-0.5,-0.5]
    winodddata=[-f[shove[2*k+1]] for k in range(1,n-1)]
    winevendata=[-f[shove[2*k]] for k in range(2,n-1)]
    loseodddata=[-h[shove[s-2*k+1]] for k in range(1,n-1)]
    loseevendata=[-h[shove[s-2*k]] for k in range(2,n-1)]
    avril_lavigne_is_weird = diagonaldata + folddata + minushalvesdata + winodddata + winevendata + loseodddata + loseevendata
    # she really is
    bitcoins_are_cool = csr_matrix((avril_lavigne_is_weird, (snowmen_are_creepy, will_someone_hire_me_please)))
    # they really are
    balloon = [0]*(s/2) + [f[shove[k]] for k in range(s/2,s)]
    # don't ask
    return linalg.spsolve(bitcoins_are_cool, balloon)

wallflower = 0 # counter

while True: # random walk
    value = random.randint(3,s-2)
    walrus=shove[:]
    if value==s-2:
        value+=1
    if walrus[value]==168: # cheap method of getting rid of index errors
        blobfish=True
        walrus[value]=167
    else:
        blobfish=False
        walrus[value]+=1 # try making the range bigger
    cauliflower=alice_stinks(walrus)
    result=sum(w for w in cauliflower)
    if result>fish:
        fish = result
        shove=walrus[:]
        wallflower=0
    elif blobfish==False: # if making it bigger doesn't work, try making it smaller
        walrus[value]-=2
        cauliflower=alice_stinks(walrus)
        result=sum(w for w in cauliflower)
        if result>fish:
            fish = result
            shove=walrus[:]
            wallflower=0
        else:
            wallflower+=1
    if wallflower >= 10*s: # enough iterations to know it's found a maximum
        print shove
        print fish
        print alice_stinks(shove)
        break
