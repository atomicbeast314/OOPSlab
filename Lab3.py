# Disarium Number
import math
n=int(input("Enter a number : "))
temp=n
temp1=n
sum=0

c=0
while(temp1!=0):
    temp1 //= 10
    c += 1

i=c
while (temp!=0):
    digit = temp%10
    sum += math.pow(digit,i)
    print(digit)
    print(i)
    print(sum)
    temp //= 10
    i -= 1

if (sum==n): print("Disarium No.")
else : print("Not a disarium number")


# Harshad Number
n=int(input("Enter a number : "))
temp=n
sum=0

while(temp!=0):
    digit = temp%10
    sum += digit
    temp //= 10

if (n%sum==0): print("Harshad  No.")
else : print("Not a Harshad number")



# Armstrong numbers from 1 to 1000
import math

for i in range (1,1001):
    sum=0
    temp =i;
    while(temp != 0):
        digit = temp%10
        sum += math.pow(digit,3)
        temp //= 10
    if (sum==i): print(i,end=" ")