import random

DECKSIZE = 54
A = DECKSIZE - 1
B = DECKSIZE
deck = [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,
    29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,A,B
    ]
random.seed(5318008)
random.shuffle(deck)

assert DECKSIZE == len(deck)

# golf start
index=lambda l,x:l.index(x)
push=lambda l,i:l[:i]+[l[i+1]]+[l[i]]+l[i+2:]

def keystream():
    global deck, A, B, DECKSIZE
    # cycle ajoker
    aidx = index(deck, A)
    deck = push(deck, aidx) if aidx != DECKSIZE - 1 else (
        [deck[0], deck[aidx], *deck[1:aidx]])

    # cycle bjoker
    bidx = index(deck, B)
    deck = push(deck, bidx) if bidx != DECKSIZE-1 else (
        [deck[0], deck[bidx], *deck[1:bidx]])

    bidx = index(deck, B)
    deck = push(deck, bidx) if bidx != DECKSIZE-1 else (
        [deck[0], deck[bidx], *deck[1:bidx]])

    # triple cut
    [lo, hi] = sorted([index(deck, A), index(deck, B)])
    deck = [*deck[hi+1:], *deck[lo:hi + 1], *deck[:lo]]

    # count end
    bot = min(deck[-1], A)
    deck = [*deck[bot:-1], *deck[:bot], deck[-1]]

    # return value
    top = min(deck[0], A)
    return deck[top] if deck[top] < A else keystream()
    
# golf end

for c in "hifelixthisisbennettgillig":
    enc = 96 + ((ord(c) - 96 + keystream()) % 26 or 26)
    print(chr(enc), end="")
