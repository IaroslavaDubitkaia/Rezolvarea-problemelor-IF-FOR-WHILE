a=int(input('Primul numar:'))
b=int(input('Al doilea numar:'))
c=int(input('Al treilea numar:'))
if (a<b+c) and (b<c+a) and (c<a+b):
    if (a==b==c):
        print("Aceste numere pot fi laturile unui triunghi echilateral")
    elif (a==b) or (b==c) or (c==a):
        print("Aceste numere pot fi laturile unui triunghi isoscel")
    else:
        print("Aceste numere pot fi laturile unui triunghi scalen")
else:
    print("Aceste numere nu pot fi laturile unui triunghi")