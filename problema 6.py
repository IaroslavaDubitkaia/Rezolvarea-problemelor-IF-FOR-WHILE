#a.
n=eval(input('Introduceti un numar:'))
s1 = 0
s2 = 0
for i in range(1,n+1):
    s1 += i**3
    s2 += i
s2 **= 2
print(f'a.Prima suma este {s1}, iar a doua suma este {s2}')
if (s1<s2):
    print("Prima suma este mai mica decat a doua suma")
elif (s1>s2):
    print("Prima suma este mai mare decat a doua suma")
else:
    print("Sumele sunt egale")

#b.
n=eval(input('Introduceti un numar '))
s1 = 0
s2 = 0
for i in range(1,n+1):
    s1 += i ** 2
    s2 += i
s1 *= 3
s2 += n ** 3 + n ** 2
print(f'b.Prima suma este {s1}, iar a doua suma este {s2}')
if (s1<s2):
    print("Prima suma este mai mica decat a doua suma")
elif (s1>s2):
    print("Prima suma este mai mare decat a doua suma")
else:
    print("Sumele sunt egale")