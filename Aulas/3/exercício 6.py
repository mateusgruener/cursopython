#6.
def  S(p,q):
    if (p==1 or q==1) and not(p==q==1):
        S= 1
    else:
        S=0
    return S

def  C(p,q):
    if p == q == 1:
        C= 1
    else:
        C=0
    return C

def halfadder(p,q):
    halfadder = [S(p,q), C(p,q)]
    return halfadder

p= 0
q= 0
print(halfadder(p, q))
