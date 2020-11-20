m=int(input('Introduceti primul numar natural:'))
n=int(input('Introduceti al doilea numar natural:'))
m<n
while (n%m==0):
    n = n // m
if (n%m==1):
    print("Numarul", n, "este putere a lui", m)
else:
    print("Numarul", n, "nu este putere a lui", m)   