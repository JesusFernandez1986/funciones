import json
import datetime
import random

# funcion que se ejecuta si quiere jugar el juego
def jugar ():
    secret = random.randint(1, 30)
    attempts = 0
    name = input("May I ask your name? ")
    #abrimos el archivo .txt para guardar en el la lista de resultados
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
    wrong_guess = []
    
    #añadimos una variable para controlar la dificultad
    dificultad = input("If you like to play hard mode press 1, if you are a chicken and prefer easy mode, press 2: ")
    if dificultad == "1":
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1
            if guess == secret:
                # guardams la fecha actual en la variable fecha
                fecha = datetime.datetime.now()
                score_list.append({"attempts": attempts, "date": str(fecha.ctime()), "name": name, "secret number": secret,
                                   "wrong_guesses": wrong_guess})
                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                print("You have guessed it - It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
            elif guess > secret:
                print("Your guess is not correct... try something smaller")
                wrong_guess.append(guess)
            elif guess < secret:
                print("Your guess is not correct... try something bigger")
                wrong_guess.append(guess)

    #si ha elegido dificultad dificil entramos en este bucle
    if dificultad == "2":
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1
            if guess == secret:
                fecha = datetime.datetime.now()
                score_list.append({"attempts": attempts, "date": str(fecha.ctime()), "name": name, "secret number": secret,
                                   "wrong_guesses": wrong_guess})
                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                print("You have guessed it - It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
            elif guess != secret:
                print("Your guess is not correct, sort it out yourself")
                wrong_guess.append(guess)

#funcion que se ejecuta si quiere ver los resultados
def resultados():
        with open("score_list.txt", "r") as score_file:
            score_list = json.loads(score_file.read())
        sorted_list = sorted(score_list, key=lambda k: k["attempts"])[:3] # creamos una nueva lista ordenada que solo contenga el resulado de los 3 mejores intentos
        print("Top scores: ")
        for score_dict in sorted_list: # bucle que recorre la lista ordenada y muestra por pantalla los valores de cada una de las claves almacenadas
            print(str(score_dict["attempts"]) + " Attempts, Date: " + str(score_dict.get("date")) + " Name:", str(score_dict.get("name")),
            " The secret number was:", str(score_dict.get("secret number")),
            " Missed numbers: " + str(score_dict.get("wrong_guesses")))

