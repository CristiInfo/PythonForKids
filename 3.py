a = int(input("Dati primul numar intreg 14\n"))
b = int(input("Dati al doilea numar intreg \n"))
d = a%b
if d==0 and b==2:
    print(a,' este numar par')
elif d==1 and b==2:
    print(a,' este numar impar')
else:
    print("Nu putem stabili paritatea lui ",a)

