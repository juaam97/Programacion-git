humano = int(input("Piedra = 1 , Papel = 2, Tijera = 3:  "))
import random
maquina = random.randint(1,3)

match humano :
    case 1 :
        match maquina :
            case 1 :
                print ("empate")
            case 2:
                print ("Gana maquina")
            case 3:
                print ("Gana Humano")
    case 2 :
        match maquina :
            case 1 :
                print ("Gana humano")
            case 2:
                print ("Empate")
            case 3:
                print ("Gana maquina") 
    case 3 :
        match maquina :
            case 1 :
                print ("Gana maquina")
            case 2:
                print ("Gana humano")
            case 3:
                print ("Empate")     
