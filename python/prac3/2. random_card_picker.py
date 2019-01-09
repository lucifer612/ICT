import math
import random

num=random.randint(1,52)    # selecting a random number  from a card 

if(math.ceil(num%4)==0):
   shape="Clubs"
elif(math.ceil(num%4)==1):
    shape="Diamonds"
elif(math.ceil(num%4)==2):      # selecting shape of card 
    shape="Hearts"
elif(math.ceil(num%4)==3):
    shape="Spades"

if(math.ceil(num%13)==1):
    card="Ace"
elif(math.ceil(num%13)==2):
    card="2"
elif(math.ceil(num%13)==3):       # selecting a card number 
    card="3"
elif(math.ceil(num%13)==4):
    card="4"
elif(math.ceil(num%13)==5):
    card="5"
elif(math.ceil(num%13)==6):
    card="6"
elif(math.ceil(num%13)==7):
    card="7"
elif(math.ceil(num%13)==8):
    card="8"
elif(math.ceil(num%13)==9):
    card="9"
elif(math.ceil(num%13)==10):
    card="10"
elif(math.ceil(num%13)==11):
    card="Jack"
elif(math.ceil(num%13)==12):
    card="Queen"
elif(math.ceil(num%13)==0):
    card="King"
    

print("your card is :"+card+" of "+shape)



