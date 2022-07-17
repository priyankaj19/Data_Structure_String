#  Python Program to Count the Number of Vowels in a String.

str = "Priyanka Prakash Jinturkar"
v = 0
for x in str:
    if (x in "aeiouAEIOU"):
        v += 1
print("Number of vowels: ",v)