import random

# golf start
p=lambda j,d:53>(k:=d.index(j))and d[:k]+[d[k+1],j]+d[k+2:]or[d[0],j]+d[1:k]
def e(s,d,t=""):d=p(54,p(54,p(53,d)));l,h=sorted([d.index(53),d.index(54)]);d=d[h+1:]+d[l:h+1]+d[:l];b=d[-1];d=d[b:-1]+d[:-1][:b]+[b];o=d[d[0]%54or-1];return s and(o<53and e(s[1:],d,t+chr((ord(s[0])-97+o)%26+97))or e(s,d,t))or t
encrypt=e
# golf end


expected = "rvwszsylhrnfpkpeetpooeuqenlkhfynbncoohblhadptklqqkliqggoddcwqcfgxsazququpdzjkeqgcsachmjskaxcxqheawtwqymadnibxsxylrtkahsrwwvlcfhf"
plaintext = "mvdpbacxvvlpmeabquboslrcrxdaqfedkywedhybmpanzabutgjdahejnkhrgsbaxczydcdyuinxkptidzwlnocetmjnwxekzzyjyhsgjkuecfsicwprfpgfsmqkzkki"
d = [*range(1,55)]
random.seed(5318008)
random.shuffle(d)
result = e(plaintext, d)
assert result == expected, f"\n{expected}\n{result}"
