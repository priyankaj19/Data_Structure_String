#  Python Program to Remove the Characters of Odd Index Values in a String.

str = "My name is Priyanka Prakash Jinturkar"
n = len(str)
new_str = ""
for x in range(0,n):
    if(x%2 == 0):
        new_str += str[x]
print(new_str)