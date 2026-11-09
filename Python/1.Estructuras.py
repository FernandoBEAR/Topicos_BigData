print("Estructura Condicionales")
#Condicional Simple
notaTBI = 18 
if notaTBI>=10.51:
    print("Aprobaste")
#Condicional Doble
edad = 17
if edad>=18:
    print("Tomar bebidas en exceso es malo pibe no lo hagas")

#Condicional Anidado
nota = 15
if nota>20:
    print("No estiste mentiroso")
elif nota>17:
    print("Excelente, pibe")
elif nota>=14:
    print("Tas bien pibe well played")
elif nota>=10.51:
    print("Lo importante es aprobar pibe")
else:
    print("Estudia malcriado")

#Python 3.9.0 a versiones anteriores no existe condicional multiple, todo se trabajaba con condicional anidado
#Ahora con python 3.10 o superior se trabaja con MATCH
num = 1
match num:
    case 1: print("Vocal A")
    case 2: print("Vocal B")
    case 3: print("Vocal C")
    case 4: print("Vocal D")
    case 5: print("Vocal E")
    case _: print("No existe letra")