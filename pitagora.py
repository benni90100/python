a = int(input("inserisci base"))
b = int(input("inserisci altezza"))
c = int(input("inserisci ipotenusa"))

if a**2+b**2==c**2 or a**2==c**2 + b**2 or a**2+c**2 == b**2:
    print ("il triangolo è rettangolo")
else:  
    print("il triangolo non e' rettangolo")