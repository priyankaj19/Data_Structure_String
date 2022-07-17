# Python Program to Take in a String and Replace Every Blank Space with Hyphen.

str = "Priyanka Prakash Jinturkar"
new = ""
for x in str:
    if (x == " "):
        new += "-"
    else:
        new += x
print(new)

# OR

str = "Priyanka Prakash Jinturkar"
new = ""
for x in str:
    if (x.isspace()):
        new += "-"
    else:
        new += x
print(new)