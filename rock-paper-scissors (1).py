#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
import sys
print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0
while True :
    print("%s wins, %s losses, %s ties\n"%(wins,losses,ties))
    break
while True :
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    break
playermove = input()
if playermove == 'q':
    sys.exit()
elif playermove == 'r' or playermove == 'p'  or playermove == 's' :
     print("Type one of r, p, s or q")
if playermove == 'r' :
    print("ROCK versus...")
elif playermove == 'p' :
    print("PAPER versus...")
elif playermove == 's' :
    print("SCISSORS versus...")
randomnumber = random.randint(1,3)

if randomnumber == 1 :
     computermove = 'r'
     print("ROCK")
elif randomnumber == 2 :
     computermove ='p'
     print("PAPER")
elif randomnumber == 3 :
      computermove = 's'
      print("SCISSORS")
if playermove == computermove :
      print("Its a tie!")
      ties = ties + 1
elif playermove == 'r' and computermove == 's' :
      print("You win!")
      wins = wins + 1
elif playermove == 'p' and computermove == 'r' :
      print("You win!")
      wins = wins + 1
elif playermove == 's' and computermove == 'p' :
      print("You win!")
      wins = wins + 1
elif playermove == 'r' and computermove == 'p' :
      print("You lose!")
      losses = losses + 1
elif playermove == 'p' and computermove == 's' :
      print("You lose!")
      losses = losses + 1
elif playermove == 's' and computermove == 'r' :
      print("You lose!")
      losses = losses + 1     

    


# In[ ]:




