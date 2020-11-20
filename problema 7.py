#a.
n=eval(input("Varsta lui Mihai: "))
s = 1
c = 1
for i in range(1,n+1):
    c *= 2
    s += c + i
print(f'a.Mihai a primit {s} dolari la varsta de {n} ani')

#b.
s = 1
i = 0
c = 1
while (s<=100):
    i += 1
    c *= 2
    s += c + i
print(f'b.Cadoul lui Mihai a fost mai mare de 100 dolari la varsta de {i} ani')