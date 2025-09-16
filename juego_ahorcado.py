import random
import itertools
from functools import reduce

def obtener_palabra_aleatoria() -> str:
    palabras = ["materia", "comida", "agua", "gato", "felicidad", "saltar", "futbol"]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta: str, letras_adivinadas: set[str]) -> None:
    # List comprehension + join
    tablero = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
    print("\n" + " ".join(tablero))

def solicitar_letra(letras_introducidas: set[str]) -> str:
    while True:
        letra = input("Introduce una letra: ").strip().lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Introduce solo UNA letra (a-z).")
            continue
        if letra in letras_introducidas:
            print("Ya probaste esa letra, intenta otra.")
            continue
        return letra

def jugar_ahorcado(intentos_max: int = 10) -> None:
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas: set[str] = set()
    intentos_restantes = intentos_max

    print("¡Bienvenido al Ahorcado!\n")

    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)

        # itertools: ciclo infinito con break cuando hay entrada válida
        letra = next(filter(lambda l: l not in letras_adivinadas, 
                            (solicitar_letra(letras_adivinadas) for _ in itertools.count())))
        letras_adivinadas.add(letra)

        if letra in palabra_secreta:
            # reduce para verificar victoria si todas las letras han sido adivinadas
            adivinada = reduce(lambda acc, ch: acc and (ch in letras_adivinadas), palabra_secreta, True)
            if adivinada:
                mostrar_tablero(palabra_secreta, letras_adivinadas)
                print(f"\n ¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
                return
            else:
                print(" Letra correcta.")
        else:
            intentos_restantes -= 1
            print(f" Letra incorrecta. Te quedan {intentos_restantes} intentos.")

    print(f"\n Has perdido. La palabra secreta era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()
