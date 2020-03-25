import random
import re
swtname=input("Enter your name-->")
value="123456789"
num=re.findall("[1-9]",value)
number=random.choice(num)
name=""
n=5
while n>2:
    numm=random.choice(num)
    name=name+numm
    n-=1

txt="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Upperword=re.findall("[A-Z]",txt)
upperchar=""
while n>0:
    Upperchar=random.choice(Upperword)
    upperchar=upperchar+Upperchar
    n-=1

textt="abcdefghijklmnopqrstuvwxyz"
Lowerword=re.findall("[a-z]",textt)
Lowerchar=random.choice(Lowerword)

spl="!@#$%^&*"
splword=re.findall("[!-*]",spl)
splchar=random.choice(splword)


print("Hi,",swtname)
print("Your Email Id :",end=" ")
strr="@gmail.com"
print(swtname+name+strr)

print("Your Password :",end=" ")
print(upperchar+number+Lowerchar+splchar+number)
