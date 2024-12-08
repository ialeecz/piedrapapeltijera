import random

# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]

print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
while True:
    # Entrada del jugador
    jugador = input("\nElige piedra, papel o tijera (o 'salir' para terminar): ").lower()

    # Salir del juego
    if jugador == "salir":
        print("¡Gracias por jugar! Hasta luego.")
        break

    # Validar entrada
    if jugador not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        continue

    # Elección del sistema
    sistema = random.choice(opciones)
    print(f"El sistema eligió: {sistema}")

    # Determinar resultado
    if jugador == sistema:
        print("¡Es un empate!")
    elif (jugador == "piedra" and sistema == "tijera") or \
         (jugador == "papel" and sistema == "piedra") or \
         (jugador == "tijera" and sistema == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")