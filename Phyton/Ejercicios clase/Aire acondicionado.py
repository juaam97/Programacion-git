Temperatura = float(input("La temperatura del aire es:"))
if Temperatura > 26 :
    print ("Enciende el aire")
    if Temperatura < 23 :
        print("apago el aire")
else :
    print ("Apagar el Aire")
    if Temperatura < 10 : 
        print ("Enciende calefacción")
        if Temperatura > 15 :
            print("Apaga la calefacción")
print ("La temperatura es:" + str(Temperatura))

