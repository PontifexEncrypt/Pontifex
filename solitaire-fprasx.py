import random

DECKSIZE = 54
A = DECKSIZE - 1
B = DECKSIZE
d = [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,
    29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,A,B
    ]
random.seed(5318008)
random.shuffle(d)

assert DECKSIZE == len(d)

# golf start
index=lambda x:d.index(x)
push=lambda l,i:l[:i]+[l[i+1]]+[l[i]]+l[i+2:]
cyclebot2top=lambda i:[d[0],d[i],*d[1:i]]

def keystream():
    global d, A, B, DECKSIZE
    # cycle ajoker
    a = index(A)
    d=a!=DECKSIZE-1 and push(d,a)or cyclebot2top(a)

    # cycle bjoker
    b = index(B)
    d=b!=DECKSIZE-1 and push(d,b)or cyclebot2top(b)

    b = index(B)
    d=b!=DECKSIZE-1 and push(d,b)or cyclebot2top(b)

    # triple cut
    lo, hi = sorted([index(A), index(B)])
    d = d[hi+1:]+d[lo:hi + 1]+d[:lo]

    # count end
    bot = min(d[-1], A)
    d = d[bot:-1]+d[:bot]+[d[-1]]

    # return value
    top = min(d[0], A)
    return d[top] if d[top] < A else keystream()
    
# golf end

expected = "rvwszsylhrnfpkpeetpooeuqenlkhfynbncoohblhadptklqqkliqggoddcwqcfgxsazququpdzjkeqgcsachmjskaxcxqheawtwqymadnibxsxylrtkahsrwwvlcfhf"
result = ""
for c in "mvdpbacxvvlpmeabquboslrcrxdaqfedkywedhybmpanzabutgjdahejnkhrgsbaxczydcdyuinxkptidzwlnocetmjnwxekzzyjyhsgjkuecfsicwprfpgfsmqkzkki":
    enc = 96 + ((ord(c) - 96 + keystream()) % 26 or 26)
    result += chr(enc)
assert result == expected
