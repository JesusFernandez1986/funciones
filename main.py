#primero importamos las dos funciones creadas del archivo funciones.py
from funciones import jugar
from funciones import resultados

#creamos un bucle que pregunte al usuario tres opciones y respondemos a ese input llamando a las funciones definidas anteriormente
while True:
    selection = input("Would you like to a) play a new game, b) see the best scores, or c) quit? ")
    if selection == "a":
        jugar()
    elif selection == "b":
        resultados()
    else:
        break
