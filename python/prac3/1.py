import random
number=random.randint(10,100)
r1=number//10
r2=number%10
u_input=int(input("enter your number :"))
u1=u_input//10
u2=u_input%10
print("Lottery Number is  : ",number)
if(number==u_input):
    print("congrats !! , you've won 10000$ !!")
elif((r1==u1 and r2==u2) and (r2==u1 or r2==u2)):
    print("congrats !! , you've won 3000$ !! ")
elif((r1==u1 and r2==u2) or (r2==u1 or r2==u2)):
    print("congrats !! , you've won 1000$ !! ")
else:
    print("Better Luck Next Time !")
    
    
    
    


