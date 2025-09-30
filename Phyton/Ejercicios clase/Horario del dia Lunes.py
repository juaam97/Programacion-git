Dia = float(print("Que hora es?"))

match Dia :
    case "8" | "9" :
        print ("FOL")
    case "9" | "10" :
        print ("EDE")
    case "11" | "11:30" : 
        print ("RECREO")
    case "11:30" | "12" :
        print ("PROG")
    case "12" | "14" :
        print ("BBDD")
    