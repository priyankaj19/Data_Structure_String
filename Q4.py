# Python Program to Form a New String where the First Character and 
# the Last Character have been Exchanged

str = "Priyanka"
print(str)
new_str = str[-1:] + str[1:-1] + str[0:1]
print(new_str)

# OR
def swap(string):
      return string[-1:] + string[1:-1] + string[:1]

str1 = input("Please Enter String : ")
print ("Result : ",swap(str1))

# OR
str="Priyanka"
new=""
n=len(str)-1

new+=str[n]
for i in range(1,n):
    new+=str[i]   
new+=str[0]

print(new)