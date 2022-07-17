# Python Program to Take in Two Strings and Display the Larger String 
# without Using Built-in Functions

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
len1 = 0
len2 = 0
for x in str1:
    len1 += 1
for y in str2:
    len2 += 1

if(len1 == len2):
    print("Given strings are equal in lenth.")
elif(len1 > len2):
    print("Larger string: ",str1)
else:
    print("Larger string: ",str2)