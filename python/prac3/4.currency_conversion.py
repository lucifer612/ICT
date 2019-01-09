import math as m
amount=float(input("Enter the Dollar Amount ::")) # enter amount 
int_amount=amount*100                      # converting floating point to inetger
dollar_amount=int_amount//100      # getting dollar value
print("Dollar   ::",dollar_amount)
decimal_value=m.ceil(int_amount%100)        # getting remaining value for calculating quarters
quarters=decimal_value//25
print("Quarters ::",quarters)
remaining = decimal_value%25  # for getting remaining value after quarter 
dimes=remaining//10                     #dimes
print("Dimes   ::",dimes)
remain_dimes=remaining%10          # getting remainder for nickels
nickels=remain_dimes//5
print("Nickels ::",nickels)
pennies=remain_dimes%5      # remainder of nickels is pennies
print("Pennies ::",pennies)

print(amount," =","Dollar:",dollar_amount,",Quarters:",quarters,",Dimes:",dimes,",Nickels",nickels,",Pennies:",pennies)



