###############################################################################################Q1,Q2
D = {1,2,3,4,5,6,7,8,9,10}  #definition of domain D

def P(x):                   #definition of predicate P(X)
    if (x%3 == 0):
        return True
    else:
        return False
    
def Q(x,y):                 #definition of predicate Q(X,Y)
    if (((x+y)%4) == 0):
        return True
    else:
        return False



def AxPx():                 #function which evaluates universal quantifier on P(x)
    tcount = 0
    fcount = 0

    for x in D:
        if(not P(x)):
            fcount += 1     #count of Fs

    if (fcount > 0):
        return False
    else:
        return True


def ExPx():                 #function which evaluates existential quantifier on P(x)
    tcount = 0
    fcount = 0

    for x in D:
        if(P(x)):
            tcount += 1     #count of Ts

    if (tcount > 0):
        return True
    else:
        return False


def AxEyQxy():              #function which evaluates formula AxEyQ(x,y)
    
    tcount = 0

    for x in D:
       for y in D:
           if (Q(x,y)):
               tcount += 1    #count of Ts
               break

    if (tcount == len(D)):
        return True
    else:
        return False




#output statements
print "The correct value for the well formed formula AxP(x) is: " + str(AxPx())
print
print "The correct value for the well formed formula ExP(x) is: " + str(ExPx())
print
print "The correct value for the well formed formula AxEyQ(x,y) is: " + str(AxEyQxy())
print
###############################################################################################Q3
P = {0,1}                                   #setting up boolean values
Q = {0,1}
R = {0,1}

def implies(x, y):                          #defintion of "implies"
    return int(not x or y)





tcount = 0
fcount = 0

print "P Q  formula-A"                      #truth table header

for x in P:
    for y in Q:
        A = implies((not x and (x or y)),y)         #definition of formula-A
        if (A):
            tcount += 1                             #count Ts
        else:
            fcount += 1                             #count Fs
        print "" + str(x) + " " + str(y) + "    " + str(A)          


if(fcount == (len(P) * len(Q))):                    #condition for contradiction
   print "This formula is a contradiction"
elif(tcount == (len(P) + len(Q))):                  #condition for tautology
     print "This formula is a tautology"
else:                                               #condition for contingency
     print "This formula is a contingency"



#--------------------------------------------------------------------------------



tcount = 0
fcount = 0                                          #re-setting counters 

print
print
print "P R  formula-B"

for x in P:
    for y in R:
        B = y and (implies(x, not y) and implies (not x, not y))    #definition of formula-B
        if (B):
            tcount += 1
        else:
            fcount += 1
        print "" + str(x) + " " + str(y) + "    " + str(B)          #same as part A
        
                   
if(fcount == (len(P) * len(R))):
   print "This formula is a contradiction"
elif(tcount == (len(P) * len(R))):
     print "This formula is a tautology"                            #same as part A
else:
     print "This formula is a contingency"



#--------------------------------------------------------------------------------



tcount = 0     
fcount = 0

print
print
print "P Q R  formula-C"

for x in P:
    for y in Q:
        for z in R:
            C = implies((implies(x,implies(y,z))),(implies(implies(x,y),z)))
            if(C):
                tcount += 1
            else:
                fcount += 1
            print "" + str(x) + " " + str(y) + " " + str(z) + "    " + str(C)



if(fcount == (len(P) * len(R) * len(P))):
    print "This formula is a contradiction"
elif(tcount == (len(P) * len(R) * len(P))):
    print "This formula is a tautology"
else:
    print "This formula is a contingency"
###############################################################################################Q4     
P = {0,1}                                   #setting up boolean values
Q = {0,1} 
R = {0,1}
S = {0,1}



def implies(x, y):                          #method definition of "implies"
    return int(not x or y)


count = 0                                   #counter for mismatches

print
print
print "P Q R S  formula-1    formula-2"     #header for truth table display

for x in P:
    for y in Q:                             #loops for exploring all interpretations 
        for z in R:
            for a in S:
                A = implies(implies(x,y),implies(z,a))                      #formula 1  
                B = implies(implies(x,z),implies(y,a))                      #formula 2 
                print "" + str(x) + " " + str(y) + " " + str(z) + " " + str(a) + "    " + str(A)+ "             " + str(B), 
                if (A != B):                                                #if the two formulas don't match --> print message
                    print "  Mismatch!"
                    count += 1                                              #increment mismatch counter
                else: print
                


if(count > 0):
    print
    print "The two formulas did not match and are therefore non-equivalent" 
else:
    print "The two formulas are equivalent"                                 #printing conclusion
        
                
            



     





   

     
        


        








        


