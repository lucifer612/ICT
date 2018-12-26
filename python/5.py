# take user details and display them
import datetime as dt
user_name=str(input("Enter your name : "))
birth_date=input("Enter your BirthDate (yyyy-mm-dd): ")
semester=int(input("Enter your semester : "))
a= dt.datetime.now()
print(dt.datetime.now())  # printing the time at which we submit the 

print("user details are: ",user_name+" "+str(birth_date)+" "+str(semester))   # printing user details

current_year=a.strftime("%Y")  #getting current year
index=birth_date.find('-') 
age=int(current_year)-int(birth_date[:index]) # calculating age
print("your age :",age)




