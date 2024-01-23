from random import shuffle, seed
seed(5318008)
# D=[*range(1,55)]
shuffle(D:=[*range(1, 55)])
# shuffle(D)

# golf start

# 53 is first joker, 54 is second

# d = [0,0,0,0,0,0,0]
# D = [1, 4, 7, 10, 13, 16, 19, 22, 25, 54, 3, 6, 9, 12, 15, 18, 21, 24, 53, 2, 5, 8, 11, 14, 17, 20, 23, 26]

# def p(j,d=d):d[:]=(53>(i:=x(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j,*d[1:i]])
'''
x=lambda i:d.index(i)
p=lambda j:53>(i:=x(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j,*d[1:i]]
def k():
    global d

    p(53);p(54);p(54)
    d=p(53);d=p(54);d=p(54)
   
    l,h=sorted([x(A),x(54)]);
    d=d[h+1:]+d[l:h+1]+d[:l]

    c=min(d[-1],53)
    d=d[c:-1]+d[:c]+[d[-1]]

    t=min(d[0],53)
    return 53>d[t]and d[t]or k()
'''



# d=0;A=53
# p=lambda j:A>(i:=d.index(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j,*d[1:i]]
# def k():global d;d=p(A);d=p(54);d=p(54);l,h=sorted([d.index(A),d.index(54)]);d=d[h+1:]+d[l:h+1]+d[:l];c=min(d[-1],A);d=d[c:-1]+d[:c]+[d[-1]];t=min(d[0],A);return A>d[t]and d[t]or k()
# def k():global d;d=p(54,p(54,p(A,d)));l,h=sorted([d.index(A),d.index(54)]);d=d[h+1:]+d[l:h+1]+d[:l];c=min(d[-1],A);d=d[c:-1]+d[:c]+[d[-1]];t=min(d[0],A);return A>d[t]and d[t]or k()
# def encrypt(s,e):global d;d=e;return "".join(chr((k()+ord(c)-97)%26+97)for c in s)








# A=53
# def k(d):p=lambda j:A>(i:=d.index(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j]+d[1:i];d=p(A);d=p(54);d=p(54);l,h=sorted([d.index(A),d.index(54)]);d=d[h+1:]+d[l:h+1]+d[:l];c=min(d[-1],A);d=d[c:-1]+d[:c]+[d[-1]];t=min(d[0],A);return A>d[t]and(d[t],d)or k(d)
# def encrypt(s,d):o,d=k(d);return s and chr((ord(s[0])-97+o)%26+97)+encrypt(s[1:],d)or""




p=lambda j,d:53>(i:=d.index(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j]+d[1:i]
def e(s,d,t=""):
    
    d=p(54,p(54,p(53,d)));
    
    l,h=sorted([d.index(53),d.index(54)]);
    d=d[h+1:]+d[l:h+1]+d[:l];
    
    c=d[-1];d=d[c:-1]+d[:-1][:c]+[c];

    o=d[d[0]%54or-1];
    return s and(o<53and e(s[1:],d,t+chr((ord(s[0])-97+o)%26+97))or e(s,d,t))or t

encrypt=e






# A=53
# def e(s,d,t=""):

    # p=lambda j:(A>(i:=d.index(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j]+d[1:i],i);
    # d,_=p(A);d,_=p(54);d,B=p(54);

    # p=lambda j,d,_:A>(k:=d.index(j))and(d[:k]+[d[k+1],j]+d[k+2:],k+1)or([d[0],j]+d[1:k],1);
    # d,B=p(54,*p(54,*p(A,d,0)));
    
    # l,h=sorted([d.index(A),B]);
    # d=d[h+1:]+d[l:h+1]+d[:l];
    
    # c=min(d[-1],A);
    # d=d[c:-1]+d[:c]+[d[-1]]

    # o=d[min(d[0],A)];
    # return s and(A>o and e(s[1:],d,t+chr((ord(s[0])-97+o)%26+97))or e(s,d,t))or t

# encrypt=e





# A=53
# def e(s,d,t=""):p=lambda j:A>(i:=d.index(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j]+d[1:i];d=p(A);d=p(54);d=p(54);l,h=sorted([d.index(A),d.index(54)]);d=d[h+1:]+d[l:h+1]+d[:l];c=min(d[-1],A);d=d[c:-1]+d[:c]+[d[-1]];o=d[min(d[0],A)];return s and(A>o and e(s[1:],d,t+chr((ord(s[0])-97+o)%26+97))or e(s,d,t))or t
# encrypt=e



# A=53
# def e(s,d,t=""):p=lambda j:A>(i:=d.index(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j]+d[1:i];d=p(A);d=p(54);d=p(54);l,h=sorted([d.index(A),d.index(54)]);d=d[h+1:]+d[l:h+1]+d[:l];c=min(d[-1],A);d=d[c:-1]+d[:c]+[d[-1]];u=min(d[0],A);return s and(A>d[u]and e(s[1:],d,t+chr((ord(s[0])-97+d[u])%26+97))or e(s,d,t))or t
# encrypt=e

# encrypt=lambda s,d,t="":s and encrypt(*k(s,d,t))or t

    
# def encrypt(s,d):o,d=k(d);return s and+encrypt(s[1:],d)or""

    
    # return "".join(chr((k()+ord(c)-97)%26+97)for c in s)











# A=53;B=54
# def a(x,d=d):d[:]=x
# x=lambda i:d.index(i)
# def p(j):A>(i:=x(j))and d[:i]+[d[i+1],j]+d[i+2:]or[d[0],j,*d[1:i]]
# k=lambda:[map(a,[p(A),p(B),p(B),d[(h:=max(x(A)),x(B))+1]+d[(l:=min(x(A),x(B)):h]+d[:l],d[(c:=min(d[-1],A)):-1]+d[:c]+[d[-1]],]),A>d[(t:=min(d[0],A))]and d[t]or k()][1]





# print(encrypt("hifelix", D))


expected = "rvwszsylhrnfpkpeetpooeuqenlkhfynbncoohblhadptklqqkliqggoddcwqcfgxsazququpdzjkeqgcsachmjskaxcxqheawtwqymadnibxsxylrtkahsrwwvlcfhf"
plaintext = "mvdpbacxvvlpmeabquboslrcrxdaqfedkywedhybmpanzabutgjdahejnkhrgsbaxczydcdyuinxkptidzwlnocetmjnwxekzzyjyhsgjkuecfsicwprfpgfsmqkzkki"
result = encrypt(plaintext, D)
print(expected)
print(result)
assert result == expected

