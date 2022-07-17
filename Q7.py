#  Python Program to Calculate the Length of a String Without Using a Library Function.
# without using library function
str = "Priyanka Prakash Jinturkar "
len = 0
for x in str:
    len += 1
print("Length of given string : ",len)

# with using library function
str = "Priyanka Prakash Jinturkar"
print("Length of given string : ",len(str))