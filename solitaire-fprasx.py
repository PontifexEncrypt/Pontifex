import random

# golf start
A=53
def encrypt(s,e,d):
    p=lambda j,d:A>(k:=d.index(j))and d[:k]+[d[k+1],j]+d[k+2:]or[d[0],j]+d[1:k]
    d=p(54,p(54,p(A,d)))
    l,h=sorted([d.index(A),d.index(54)])
    d=d[h+1:]+d[l:h+1]+d[:l]
    b=min(d[-1],A)
    d=d[b:-1]+d[:b]+[d[-1]]
    t=min(d[0],A)
    return s and(A>d[t]and encrypt(s[1:],e+chr(97+(ord(s[0])-97+d[t])%26),d)or encrypt(s,e,d))or e
# golf end


expected = "rvwszsylhrnfpkpeetpooeuqenlkhfynbncoohblhadptklqqkliqggoddcwqcfgxsazququpdzjkeqgcsachmjskaxcxqheawtwqymadnibxsxylrtkahsrwwvlcfhf"
plaintext = "mvdpbacxvvlpmeabquboslrcrxdaqfedkywedhybmpanzabutgjdahejnkhrgsbaxczydcdyuinxkptidzwlnocetmjnwxekzzyjyhsgjkuecfsicwprfpgfsmqkzkki"
d = [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,
    29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54
    ]
random.seed(5318008)
random.shuffle(d)
result = encrypt(plaintext, "", d)
assert result == expected, f"{result}"
