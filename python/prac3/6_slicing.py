#program to swap 1st 2 characters in 2 string inputs concate them

string1=input("enter the first string :")
string2=input("enter the second string :")

slice_s2=string2[:2]   # slicing first 2 characters of 2nd string 
slice_s1=string1[:2]   #slicing second 2 characters of 1st string

final_string=(slice_s2+string1[2:]+slice_s1+string2[2:])
print(final_string)
