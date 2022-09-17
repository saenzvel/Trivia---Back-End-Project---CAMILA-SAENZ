#bienvenida para quien juegue tu trivia
import time

print ("Bienvenido al desafío: RESPONDIENDO LAS TRIVIAS PARA SALVAR AL PRÍNCIPE DAMON.\n")
time.sleep(1)

print("CONTEXTO:\n")
print("El príncipe Damon, hermano del rey Viserys, ha sido capturado por fuerzas enemigas de la casa Lannister. Debemos rescatarlo antes que sea sentenciado! \n")

time.sleep(2)

# Es importante dar instrucciones sobre cómo jugar:
print ("DESAFÍO:\n")
print ("La misión consiste en obtener la mayor cantidad de puntaje respondiendo las siguientes preguntas y así poder liberar al príncipe.\n")
print ("Pondremos a prueba tus conocimientos así que debes escribir la letra de la alternativa y luego presionar 'Enter' para enviar tu respuesta.\n")
print ("Buena suerte! El rey te encomienda esta misión.\n")
time.sleep(2)

#Algoritmo del juego

def game():
    questions = {"Con qué canción debutó Avril Lavigne?" :"c",
    "Qué planetas están más cerca a la tierra?":"a",
    "Qué equipo de futbol ganó la UCL en el 2019?":"b",
    "Qué película NO pertenece al genero ciencia ficción?":"c"}

    options = [["a. I love it when you hate me", "b. Girlfriend", "c. Complicated","d. Sk8rboy"],
    ["a. Marte y Venus", "b. La tierra es plana", "c. Plutón y Saturno", "d. Jupitér y Saturno"],
    ["a. Real Madrid","b. Liverpool", "c. Chelsea", "d. Barcelona"],
    ["a. Dune", "b. Blade Runner", "c. 12 años de esclavitud", "d. Star Wars"]]

    
    position_op = 1
    guesses = []
    score = 0
     
    for order_quest in questions:
        print (order_quest)
        for i in options [position_op-1]:
            print (i)
        position_op = position_op + 1
        print ()

        guess = input ("Escoge una alternativa (a,b,c o d):")
        guess = guess.lower()       
        answer = questions.get(order_quest)
            
        if answer == guess:
            score = score + 1
            print ("CORRECTO")
            print (score)
            print ()
            
        else:
            print ("INCORRECTO")
            print ()
                

        guesses.append(guess)

    time.sleep(1.5)
    def display_score():
        print("-------------------------")
        print ("RESULTADOS")
        print ()
        print("Respuestas Correctas:", end="")
        for i in questions:
            print (questions.get(i), end="")
        print()

        print("Tus respuestas: ", end ="")
        for i in guesses:
            print(i, end="")
        print()

    display_score()

    time.sleep(1)
    print("-------------------------")
    print("Estadisticas:")
    while score >= 3:
        print ("Muy bien! Tu puntaje es", score)
        print ("Pudimos liberar al príncipe Damon :D, el rey agradece tu ayuda\n")
        break

    while score < 3:
        print("Mejor suerte para la próxima! Tu puntaje es", score)
        print ("No pudimos salvar al príncipe Damon, íntentalo una vez más:D!!")
        print()
        break

game()

time.sleep(1)
def last_answer():
    
    last_answer = input ("¿Quieres volver a jugar? (si o no):")
    last_answer = last_answer.lower()
    if last_answer == "si":
        return game()
    
    elif last_answer == "no":
        print("Gracias por participar!")
        print ("Byeeeeee :D")
        
    else:
        print ("Esa opción no se encuentra disponible, gracias por participar! :D")

last_answer()

