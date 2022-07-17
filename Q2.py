# Python Program to Remove the nth Index Character from a Non-Empty String.

#str =input("Enter a string: ")
str = "Priyanka Prakash Jinturkar"
n = len(str)
index = int(input("Enter a index to remove:"))
result = ""
for i in range(0,n):
    if(i != index):
        result += str[i]
    
print("Result: ",result)