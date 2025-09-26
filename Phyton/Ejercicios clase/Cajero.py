Dinero = float("100")
DineroRetirado = float(input("Cuanto dinero deseas retirar: "))

if DineroRetirado <= Dinero :
    Dinero -= DineroRetirado
    print ("Gracias por confiar en nosotros su saldo actual es: ")
    print (Dinero)

else :
    print ("No tienes suficiente salgo en la cuenta su saldo es de:")
    print (Dinero)
print ("Vuelve Pronto")
