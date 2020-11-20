import math
n=int(input('valoarea lui n='))
s=0
for i in range (1,n+1):
    s = s + math.factorial(i)
print("Suma factorialelor este", s)