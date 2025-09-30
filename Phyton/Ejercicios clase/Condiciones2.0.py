Opcion = input("Dame una opcion")

match  Opcion :
    case "A" | "a" :
        print ("Alto")
    case "B" | "b" :
        print ("Bajo")
    case "C" | "c" : 
        print ("Cambio")
    case _:
        print("Opcion no valido")


