from funciones import jugar
from funciones import resultados

while True:
    selection = input("Would you like to a) play a new game, b) see the best scores, or c) quit? ")

    if selection == "a":
        jugar()
    elif selection == "b":
        resultados()
    else:
        break