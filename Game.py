import random

print('''Bienvenido al juego de adivinar números!!
Estoy pensando en un número del 1 al 100.
Dependiendo de la dificultad, son los intentos que tendrás.
''')

# Dificultades y número de intentos
dificultades = {
    1: "Fácil (10 intentos)",
    2: "Intermedio (5 intentos)",
    3: "Difícil (3 intentos)"
}

intentos = {
    1: 10,
    2: 5,
    3: 3
}

op = str#opcion para seguir jugando
while(op !="n"):#bucle que permite al usuario salir del juego o seguir jugando
    # Selección de dificultad
    opcion = input("Ingrese una opción:\n 1. Fácil (10 intentos)\n 2. Intermedio (5 intentos)\n 3. Difícil (3 intentos)\n ")
    opcion = int(opcion)  # Convierte la opción a entero

    if opcion not in intentos:
        print("Opciones inválidas. Por favor selecciona 1, 2 o 3.")
        exit()

    # Configuración del juego
    numintentos = intentos[opcion]
    numero = random.randint(1, 100)
    print(f"¡Genial! Has escogido la opción: {dificultades[opcion]}. ¡A jugar!")


    # Juego de adivinanza

    for intento in range(1, numintentos + 1):
        jugador = int(input(f"Intento {intento}/{numintentos}: Ingresa tu número: "))
        if jugador > numero:
            print("El número es menor, sigue intentando.")
        elif jugador < numero:
            print("El número es mayor, sigue intentando.")
        else:
            print(f"¡Genial! Acabas de encontrar el número {numero} en el intento {intento}.")
            break
    else:
        print(f"Lo siento, se te acabaron los intentos. El número era {numero}.")
        op=(input("Quieres seguir jugando? S(si) o N(no)"))#si el usuario pone s se repite el ciclo de nuevo pero si pone n sale del juego