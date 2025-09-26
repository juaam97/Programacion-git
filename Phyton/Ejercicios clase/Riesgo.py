Historialcrediticio = float(input("Introduce un numero negativo si tu historial es negativo o uno positivo si tu historial es positivo"))
Empleo = float(input("Introduce cuantos años estas trabajando:"))
Solicitud = float(input("Introduce la cantidad de tu solicitud:"))
Sueldo = float(input("Introduce tu sueldo:"))


if Historialcrediticio < 0 or Empleo < 2 or Solicitud > (0.01 * Sueldo) :
    print ("Es de riesgo")
else : 
    print ("No es de riesgo")
print ("gracias por venir")    
