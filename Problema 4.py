from fractions import Fraction
n=int(input('Introduceti numaratorul primei fractii:'))
m=int(input('Introduceti numitorul primei fractii:'))
a=int(input('Introduceti numaratorul pentru a doua fractie:'))
b=int(input('Introduceti numitorul pentru a doua fractie:'))
s = Fraction(n,m) + Fraction(a,b)
p = Fraction(n,m) * Fraction(a,b)
print(f'a)Suma lor este {s},  b)Produsul lor este {p}')