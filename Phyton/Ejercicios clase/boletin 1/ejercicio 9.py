Numero1= int(input("Introduce primer numero"))
Numero2= int(input("Introduce un segundo numero"))
if Numero1  > 0 and Numero2 > 0  :
    print ("Los dos son positivos")
elif Numero1 < 0 and Numero2 > 0 :
    print ("Solo uno es positivo")
elif Numero1 > 0 and Numero2 < 0 :
    print ("Solo uno es positivo")
else :
    print ("Todos son negativos")