n=int(input('Introduceti un numar natural:'))
print("Numerele perfecte sunt")
for i in range(1,n+1):
    s=0
    for j in range(1,i//2+1):
         if (i%j==0):
             s+=j
    if (i==s):
        print(i, end=" ")