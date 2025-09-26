num1= int(input("Dame el primer numero"))
num2= int(input("Dame el segundo numero"))

if num2 != 0 :
    resultado = num1/num2
    print ("El resultado es :"+ str(resultado))
elif num2 == 0:
    print ("Error")