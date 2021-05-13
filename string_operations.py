##### taking multiple inputs
while True:
    h = str(input("enter the value:"))
    if h == "stop":
        break;
    else:
        print(h)

#### reverse a string using reversed()
string1 = str(input("enter a string: "))
str2 = list(reversed(string1))
print("reverde string is",''.join(str2))

#### Lenghth of the string ###################

string1 = str(input("enter a string: "))
print("length of the string is" , len(string1))

#### Generating password of n length (given as input) from the string defined in "s" ###################
import random
passlength = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlength ))
print(p)


############## Soring the elements of given string in reverse order ###
n = int(input("enter the number of elemnts:"))
strlist = []
for i in range(1,n+1):
    str1= str(input("enter the value {}:".format(i)))
    strlist.append(str1)
print("input string is:" , strlist)
strlist.sort(reverse=True)
print("reversed string is:",strlist )
