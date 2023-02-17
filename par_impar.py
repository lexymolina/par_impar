x = int(input("digite un numero"))

r = x%2

if r==0:
    msj = "par"

else:
    msj = "impar"    

print("el numero " + str(x) + "es" + msj)
