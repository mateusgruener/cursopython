"""
5. An implication C = (A ⇒ B) is a Boolean expression that is defined as
            C is True if A is False or A and B are both True
            C is False otherwise
        Write a Python function implication(A, B).
"""
def implication(A, B):
    if A==0 or (A!=0 and B!=0):
        implication = 1
    else:
        implication = 0
    return implication

A=1
B=0

if bool(implication(A, B))==True:
    print("implication é True")
else:
    print("implication é False")

