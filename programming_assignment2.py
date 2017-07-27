import random

print "Q1********************************************Q1"

A = set()
B = set()
C = set()
D = set()

arr = [A,B,C,D]

for x in arr:
    for num in range(0,11):
        x.add(random.randrange(40))



equal =((A&B)|(C&D))==((A&D)|(C&B))
print "((A&B)|(C&D))==((A&D)|(C&B)) ==> " + str(equal)

equal =((A-(B|C))==((A-C)&(A-B)))
print "((A-(B|C))==((A-C)&(A-B))) ==> " + str(equal)


print

print "Q2********************************************Q2"



def isReflexive(S):
    arr = [(1,1),(0,0)]
    
    count = 0
    for x in S:
        for y in arr:
            if(x == y):
                count += 1

    if(count == 2):
        return True
    else:
        return False


def isIrreflexive(S):
    arr = [(1,1),(0,0)]
    
    count = 0
    for x in S:
        for y in arr:
            if(x == y):
                count += 1

    if(count == 0):
        return True
    else:
        return False



def isSymmetric(S):
    arr = []
    
    for x in S:
         tup = x[::-1]
         if (tup == x):
             continue 
         arr.append(tup)

    for x in arr: 
        z = {x}
        if(not(z<=S)):
            return False

    return True

    
    
def isAsymmetric(S):
    arr = []
    
    for x in S:
         tup = x[::-1]
         if (tup == x):
             continue 
         arr.append(tup)

    for x in arr: 
        z = {x}
        if(z<=S):
            return False

    return True


    

def isAntisymmetric(S):
    arr = []
    count = 0 
    
    for x in S:
         tup = x[::-1]
         if (tup == x):
             continue 
         arr.append(tup)

    for x in arr: 
        z = {x}
        if(z<=S):
            count = count+1   

    if(count == 0):
        return True
    else:
        return False
    
    

        
def isTransitive(S):

    trn = set()
    arr = []

    for x in {1,0}:
        for y in S:
            if(y[0]==x):
                for z in S:
                    if(z[0]==y[1]):
                        trn.add((y[0],z[1]))

    if(trn <= S):
        return True
    else:
        return False
                    
                        
A = set()
B = {(1,1)}
C = {(0,0)}
D = {(1,0)}
E = {(0,1)}
F = B | C
G = B | D
H = B | E
I = C | D
J = C | E
K = D | E
L = B | C | D
M = B | C | E
N = B | D | E
O = C | D | E
P = C | D | E | B

arr = [A,B,C,D,E,F,H,I,J,K,L,M,N,O,P]


for t in arr:
    print t
    print "is reflexive: " + str(isReflexive(t))
    print "is irreflexive: " + str(isIrreflexive(t))
    print "is symmetric: " + str(isSymmetric(t))
    print "is asymmetric: " + str(isAsymmetric(t))
    print "is antisymmetric: " + str(isAntisymmetric(t))
    print "is transitive: " + str(isTransitive(t))
    print
    

print
print "Q3********************************************Q3"


def relateTo(S,R):

    nums = {1,2,3,4,5}
    trn = set()

    for x in nums:
        for y in S:
            if(y[0]==x):
                for z in R:
                    if(z[0]==y[1]):
                        trn.add((y[0],z[1]))

    return trn




def getRCubed(S):
    return relateTo(relateTo(S,S),S)


def printRelation(S):
    trn = set()
    
    nums = {1,2,3,4,5}
    for x in nums:
        for z in S:
            if(z[0]==x):
                trn.add((z[0],z[1]))
        print trn
        trn = set()
                
    


R = {(1, 1),(1, 2),(1, 3),(2, 3),(2, 4),(3, 1),
(3, 4), (3, 5), (4, 2), (4, 5), (5, 1), (5, 2),(5, 4)}


print "R3 of the relation "
printRelation(R)
print "is equal to:"
print
printRelation(getRCubed(R))



    

    

    


    

