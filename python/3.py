# to take filename form user and print it's extension 
user_input=input("enter the filename: ")
index_of_file=user_input.find('.')
extension=user_input[index_of_file:]    
print("the extension of file is :",extension)

