#fibbonaci series
n=int (input("Enter the number of terms in the Fibbonacci series : "))
a1=0
a2=1
print(a1,a2,end=" ")
for i in range(0,n-2):
    a3=a1+a2
    print(a3,end=" ")
    a1=a2
    a2=a3

#factorial using loops
n=int (input("Enter number whose multiplication table is to be printed : "))
for i in range (1,11):
    print(n,"*",i,"=",n*i)

# gcd and lcm using loops

def greater(m,n):
    if (m>n):
        greater=m
    else :
        greater=n
    return greater

n=int (input("Enter first number : "))
m=int(input("Enter second number : "))

for i in range (greater(m,n),0,-1):
    if (n%i==0 and m%i==0) :
        gcd=i
        break

x=greater(n,m)
while (True):
    if (x%n==0 and x%m==0):
        lcm=x
        break
    else:
        x +=1

print("gcd : ",gcd)
print("lcm : ",lcm)

