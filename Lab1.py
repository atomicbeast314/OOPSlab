n=int(input("Enter a number : "))
flag=0
for i in range(2,n):
    if (n%i==0):
        flag=1
        break
if (flag==0):
    print("prime number")
else :
    print("composite number")

n=int(input("Enter a number : "))
reversed_num=0
test_num=n
while (test_num != 0) :
    digit = test_num%10
    reversed_num = reversed_num*10 + digit
    test_num= test_num//10
print(reversed_num)
if (n==reversed_num):
    print("Palindrome")
else :
    print("Not a Palindrome")

p=int(input("Enter percentage : "))
if (100<=p and p>=91) :
    print("Grade : A+")
elif (p>=81) :
    print("Grade : A")
elif (p>=71) :
    print("Grade : B+")
elif (p>=61) :
    print("Grade : B")
elif (p>=51) :
    print("Grade : C")
elif (p>=41) :
    print("Grade : D")
elif (p>=35) :
    print("Grade : E")
else :
    print("Grade : F")

import math
n=int(input("Enter a number : "))
s=0
t=n
while(t != 0):
    digit = t%10
    s=s+ math.pow(digit,3)
    t //= 10
print(s)
if (n==s):
    print("Armstrong Number")
else :
    print("Not an armstrong number")


import math
r=int(input("Enter radius : "))
a= math.pi * r * r
print("Area : ",a)


n=int(input("Enter a number : "))
l=[]
for i in range (1,n):
    s=i*i
    l.append(s)
x=len(l)
flag=0
for j in range (0,x-1):
    if (n==l[j]):
        flag=1
        break
if (flag==1):
    print("Perfect Square")
else:
    print("Not a Perfect Square")


import math
n=int(input("Enter a number : "))
t=n
s=0
while(t != 0):
    digit=t%10
    s=s + math.factorial(digit)
    t //= 10
print(s)
if (n==s):
    print("Strong Number")
else :
    print("Not a strong number")