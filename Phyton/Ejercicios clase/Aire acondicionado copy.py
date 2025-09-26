Temperatura = float(input("La temperatura del aire es:"))
if Temperatura > 26 :
    print ("Enciende el aire")
    Temperatura = float(input("La temperatura del aire es: "))
    if Temperatura < 23 :
        print("apago el aire")
elif Temperatura < 10 : 
    print ("Enciende calefacción")
    Temperatura = float(input("La temperatura del aire es: "))
    if Temperatura > 15 :
         print("Apaga la calefacción")
else :
    print ("No cumple ninguna condicion no hacer nada")
print ("La temperatura es: " + str(Temperatura))
