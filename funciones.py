import json
import datetime
import random

def jugar ():
    #generamos un numero aleatorio entre 1 y 30
    secret = random.randint(1, 30)
    #variable en la que almacenamos el numero de intentos del jugador
    attempts = 0
    # variable en la que vamos a guardar el nombre del jugador
    name = input("May I ask your name? ")
    #abrimos el archivo .txt para guardar en el la lista de resultados
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
    #creamos una lista nueva para guardar los resultados erroneos
    wrong_guess = []
    #añadimos una variable para controlar la dificultad
    dificultad = input("If you like to play hard mode press 1, if you are a chicken and prefer easy mode, press 2: ")
    #si ha escogido dificultad facil entramos en este bucle
    if dificultad == "1":
        # bucle que comprueba si hemos acertado el numero o no
        while True:
            # pedimos que se vaya introduciendo un numero entre 1 y 30 y lo comparamos con el numero aleatorio generado
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1
            if guess == secret:
                # guardams la fecha actual en la variable fecha
                fecha = datetime.datetime.now()
                # añadimos un diccionario con varias claves/valores dentro de nuestra lista
                score_list.append({"attempts": attempts, "date": str(fecha.ctime()), "name": name, "secret number": secret,
                                   "wrong_guesses": wrong_guess})
                # abrimos el archivo con nuestra lista en modo escritura
                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                print("You have guessed it - It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
            elif guess > secret:
                print("Your guess is not correct... try something smaller")
                # añadimos el numero que no es el correcto a la lista wrong_guess para tener una lista de numeros fallados
                wrong_guess.append(guess)
            elif guess < secret:
                print("Your guess is not correct... try something bigger")
                # añadimos el numero que no es el correcto a la lista wrong_guess para saber tener una lista de numeros fallados
                wrong_guess.append(guess)

    #si ha elegido dificultad dificul entramos en este bucle
    if dificultad == "2":
        # bucle que comprueba si hemos acertado el numero o no
        while True:
            # pedimos que se vaya introduciendo un numero entre 1 y 30 y lo comparamos con el numero aleatorio generado
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1
            if guess == secret:
                # guardams la fecha actual en la variable fecha
                fecha = datetime.datetime.now()
                # añadimos un diccionario con varias claves/valores dentro de nuestra lista
                score_list.append({"attempts": attempts, "date": str(fecha.ctime()), "name": name, "secret number": secret,
                                   "wrong_guesses": wrong_guess})
                # abrimos el archivo con nuestra lista en modo escritura
                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                print("You have guessed it - It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
            elif guess != secret:
                print("Your guess is not correct, sort it out yourself")
                # añadimos el numero que no es el correcto a la lista wrong_guess para saber los numeros qe ha fallado
                wrong_guess.append(guess)


def resultados():
        # abrimos el archivo .txt para guardar en el la lista de resultados
        with open("score_list.txt", "r") as score_file:
            score_list = json.loads(score_file.read())
        # creamos una nueva lista ordenada que solo contenga el resulado de los 3 mejores intentos
        sorted_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
        print("Top scores: ")
        # bucle que recorre la lista ordenada y muestra por pantalla los valores de cada una de las claves almacenadas
        for score_dict in sorted_list:
            print(str(score_dict["attempts"]) + " Attempts, Date: " + str(score_dict.get("date")) + " Name:", str(score_dict.get("name")),
            " The secret number was:", str(score_dict.get("secret number")),
            " Missed numbers: " + str(score_dict.get("wrong_guesses")))

