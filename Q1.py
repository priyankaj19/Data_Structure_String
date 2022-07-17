# Python Program to Replace all Occurrences of ‘a’ with $ in a String.

str = "Priyanka Prakash Jinturkar"
print("Given: ",str)
result = ""
for i in str:
    if(i == 'a'):
        result += '$'
    else:
        result += i
    
print("Result: ",result)