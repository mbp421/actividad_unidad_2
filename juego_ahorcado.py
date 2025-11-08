import random
from collections import deque, Counter

def obtener_palabra():
    return random.choice(["materia", "comida", "agua", "gato", "felicidad", "saltar", "futbol"])

def jugar_ahorcado():
    palabra = obtener_palabra()
    letras_palabra = set(palabra)              # SET → letras únicas de la palabra
    letras_adivinadas = set()                  # SET → letras descubiertas
    historial = []                             # LIST como pila → UNDO
    jugadores = deque(["Jugador 1", "Jugador 2"])  # Cola circular
    errores = { "Jugador 1": 0, "Jugador 2": 0 }   # MAP conteo errores

    intentos = 8
    print("\n=== AHORCADO CON COLECCIONES ===")

    while intentos > 0:
        jugador = jugadores[0]
        print(f"\nTurno de: {jugador}")

        mostrar = "".join([l if l in letras_adivinadas else "_" for l in palabra])
        print("Palabra:", mostrar)

        entrada = input("Letra (o UNDO): ").lower()

        if entrada == "undo":
            if historial:
                ultima = historial.pop()
                letras_adivinadas.remove(ultima)
                print(f"Deshecha: {ultima}")
            continue

        if entrada in letras_adivinadas:
            print("Letra ya usada.")
            continue

        historial.append(entrada)

        if entrada in letras_palabra:
            letras_adivinadas.add(entrada)
            if letras_adivinadas == letras_palabra:
                print(f"¡{jugador} gana! La palabra era: {palabra}")
                break
        else:
            intentos -= 1
            errores[jugador] += 1
            print(f"Incorrecto. Intentos restantes: {intentos}")

        jugadores.rotate(-1)

    print("\nErrores por jugador:", errores)
    ranking = sorted(errores.items(), key=lambda x: x[1])
    print("Ranking:", ranking)
