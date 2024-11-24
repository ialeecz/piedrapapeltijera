import random

def determinar_ganador(jugador, sistema):
    # Reglas del juego
    if jugador == sistema:
        return "Empate"
    elif (jugador == "piedra" and sistema == "tijera") or \
         (jugador == "papel" and sistema == "piedra") or \
         (jugador == "tijera" and sistema == "papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def juego():
    # Opciones disponibles
    opciones = ["piedra", "papel", "tijera"]

    print("¡Bienvenido a Piedra, Papel o Tijera!")
    while True:
        # Entrada del jugador
        jugador = input("Elige piedra, papel o tijera: ").lower()
        if jugador not in opciones:
            print("Opción inválida. Intenta de nuevo.")
            continue

        # Elección del sistema
        sistema = random.choice(opciones)
        print(f"El sistema eligió: {sistema}")

        # Determinar ganador
        resultado = determinar_ganador(jugador, sistema)
        print(f"Resultado: {resultado}")

        # Preguntar si quiere seguir jugando
        while True:
            jugar_de_nuevo = input("¿Quieres jugar otra vez? (sí/no): ").strip().lower()
            if jugar_de_nuevo == "sí":
                break
            elif jugar_de_nuevo == "no":
                print("¡Gracias por jugar!")
                return  # Sale de la función, terminando el juego
            else:
                print("Por favor, responde 'sí' o 'no'.")

# Iniciar el juego
juego()