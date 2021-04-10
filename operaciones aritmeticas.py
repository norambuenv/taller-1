numero1= float(input("digite un numero: "))
numero2= float(input("digite un numero: "))

operaciones= input("digite la operacion: ")
if operaciones== "+":
    suma=numero1+numero2
    print("su resultado es " + str(suma))
elif operaciones== "-":
    resta=numero1-numero2
    print("su resultado es " + str(resta))
elif operaciones== "*":
    multiplicacion= numero1*numero2
    print("su resultado es " + str(multiplicacion))
elif operaciones== "/":
    division= numero1/numero2
    print("su resultado es " + str(division)) 
else: 
    print("se equivoco de operacion, volver a intentar")

    





