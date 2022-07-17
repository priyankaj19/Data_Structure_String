#  Python Program to Calculate the Number of Words and the Number of 
# Characters Present in a String.

str = "I am Priyanka Prakash Jinturkar"
len = 0
space = 0
for x in str:
    len += 1
    if(x == " "):
    #if(x.isspace()):      
        space += 1

print("Number of Words : ",(space + 1))
print("Number of Characters : ",(len - space))
