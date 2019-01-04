#python program  to print pascals triangle
row=0
col=0
space=0

number=int(input("enter the lenght of pascals triangle :"))
for row in range(0,number):
    for space in range(0,number-row):
        print(" ",end="")
    k=1
    for col in range(0,row+1):
        print(" ",end="")
        print(int(k),end="")
        k=k*(row-col)/(col+1)    # main logic to find next value 
    
    print("\n")
