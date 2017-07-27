class DFAnode:
     def __init__(self, final, name):
         self.final = final
         self.name = name

def L1(word):

    start = DFAnode(False, 0)
    one = DFAnode(False, 1)
    two = DFAnode(False, 2)
    three = DFAnode(False, 3)
    four = DFAnode(False, 4)
    five = DFAnode(True, 5)
    trap = DFAnode(False, 6)
    ghost = start

    for x in word:
        
      if(ghost.name == 0):
        if(x == 'a'):
            ghost = trap
        elif(x == 'b'):
            ghost = one
      elif(ghost.name == 1):
        if(x == 'a'):
            ghost = two
        elif(x == 'b'):
            ghost = two
      elif(ghost.name == 2):
        if(x == 'a'):
            ghost = three
        elif(x == 'b'):
            ghost = three
      elif(ghost.name == 3):
        if(x == 'a'):
            ghost = four
        elif(x == 'b'):
            ghost = trap
      elif(ghost.name == 4):
        if(x == 'a'):
            ghost = five
        elif(x == 'b'):
            ghost = five
      elif(ghost.name == 5):
        if(x == 'a'):
            ghost = trap
        elif(x == 'b'):
            ghost = trap

    return ghost.final



def L2(word):

    start = DFAnode(False, 0)
    one = DFAnode(True, 1)
    ghost = start

    for x in word:
         if(ghost.name == 0):
              if(x =='a' or x =='b'):
                   ghost = one
         elif(ghost.name == 1):
                if(x =='a' or x =='b'):
                   ghost = start
        
     
    return ghost.final



def L3(word):

    start = DFAnode(False, 0)
    one = DFAnode(True, 1)
    two = DFAnode(False, 2)
    three = DFAnode(True, 3)
    ghost = start

    for x in word:
         if(ghost.name == 0):
              if(x =='a' or x =='b'):
                   ghost = one
         elif(ghost.name == 1):
                if(x =='a' or x =='b'):
                   ghost = two
         elif(ghost.name == 2):
                if(x =='a' or x =='b'):
                   ghost = three
         elif(ghost.name == 3):
                if(x =='a' or x =='b'):
                   ghost = one   
          
    return ghost.final
    
    

def L4(word):

    start = DFAnode(True, 0)
    one = DFAnode(False, 1)
    two = DFAnode(True, 2)
    three = DFAnode(False, 3)
    four = DFAnode(True, 4)
    five = DFAnode(False, 5)
    six = DFAnode(True, 6)
    seven = DFAnode(True, 7)
    trap = DFAnode(False, 8)
    ghost = start

    for x in word:
        
      if(ghost.name == 0):
        if(x == 'a'):
            ghost = one
        elif(x == 'b'):
            ghost = five
      elif(ghost.name == 1):
           if(x == 'a'):
                ghost = two
           elif(x == 'b'):
                ghost = trap
      elif(ghost.name == 2):
           if(x == 'a'):
                pass
           elif(x == 'b'):
                ghost = three
      elif(ghost.name == 3):
           if(x == 'a'):
                ghost = trap
           elif(x == 'b'):
                ghost = four
      elif(ghost.name == 4):
           if(x == 'a'):
                ghost = trap
           elif(x == 'b'):
                pass
      elif(ghost.name == 5):
           if(x == 'a'):
                ghost = seven
           elif(x == 'b'):
                ghost = six
      elif(ghost.name == 6):
           if(x == 'a'):
                ghost = trap
           elif(x == 'b'):
                pass
      elif(ghost.name == 7):
           if(x == 'a'):
                ghost = trap
           elif(x == 'b'):
                ghost = trap
     
    return ghost.final




print "For L1:"
arrL1 = {"bbbab","baabbb","aaaba","babab","baaab"}


for word in arrL1:
     print word,
     if(L1(word)):
          print " --> accepted"
     else:
           print " --> rejected"

print "-------------------------------------------" 

print "For L2:"
arrL2 = {"baaaabb","aababa","ab","baaab","a"}


for word in arrL2:
     print word,
     if(L2(word)):
          print " --> accepted"
     else:
           print " --> rejected"


print "-------------------------------------------"

print "For L3:"
arrL3 = {"baaaabb","aabba","abbbbbbaaabaab","baabababababb","aa"}

for word in arrL3:
     print word,
     if(L3(word)):
          print " --> accepted"
     else:
           print " --> rejected"

print "-------------------------------------------"

print "For L4:"
arrL4 = {"aaaabb","ba","bbbbb","ab" ,"aaaaab"}

for word in arrL4:
     print word,
     if(L4(word)):
          print " --> accepted"
     else:
           print " --> rejected"
