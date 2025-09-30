Diasemana = input("¿Que dia de la semana es?")
Diasemana = Diasemana.upper ()

match Diasemana :
    case "LUNES" | "MARTES" | "MIERCOLES" | "JUEVES" | "VIERNES" :
        print ("Dias de Instituto")
        match Diasemana :
            case "LUNES" :  
                print ("======================")
                print ("========LUNES==========")
                print ("=======================")
                print ("=========8-9 FOL=======")
                print ("========9-10 EDE=======")
                print ("=======10-11 PROG======")
                print ("====11-11:30 RECREO====")
                print ("====11:30-12 PROGR====")
                print ("=======12-14 BBDD=====")
               
    case "SABADO" | "DOMINGO" :
        Hora = input("Que hora es?")
        if "19:00" <= Hora <= "23:45" :
            print ("Trabajo")
        else :
            print ("Casa")

