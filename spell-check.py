#### spelling corrector using TextBlob #################
from textblob import TextBlob
n = int(input("enter the number of elemnts:"))
strlist = []
corrected = []

for i in range(1,n+1):
    str1= str(input("enter the value {}:".format(i)))
    strlist.append(str1)
    corrected.append(TextBlob(str1))
    
    
print("input string is:" , strlist)
print("Corrected String is: ", corrected)

for i in corrected:
    print(i.correct())
    
    
