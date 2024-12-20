import random

# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]

# Función para mostrar animación de espera
def animacion_espera():
    print("¡Eligiendo", end="")
    for _ in range(3):
        print(".", end="", flush=True)
    print("\n")

# Función para obtener la opción del jugador
def obtener_opcion_jugador():
    while True:
        jugador_opcion = input("Elige piedra, papel o tijera: ").lower()
        if jugador_opcion in opciones:
            return jugador_opcion
        else:
            print("Opción no válida. Intenta de nuevo.")

# Función para obtener la opción del sistema (computadora)
def obtener_opcion_sistema():
    return random.choice(opciones)

# Función para determinar el ganador
def determinar_ganador(opcion_jugador, opcion_sistema):
    if opcion_jugador == opcion_sistema:
        return "¡Es un empate!"
    elif (opcion_jugador == "piedra" and opcion_sistema == "tijera") or \
         (opcion_jugador == "papel" and opcion_sistema == "piedra") or \
         (opcion_jugador == "tijera" and opcion_sistema == "papel"):
        return "¡Jugador gana!"
    else:
        return "¡Sistema gana!"

# Función para mostrar el menú
def mostrar_menu():
    print("\n¡Bienvenido al juego Piedra, Papel o Tijera!")
    print("1. Jugar")
    print("2. Salir")
    while True:
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("¡Gracias por jugar!")
            exit()
        else:
            print("Opción no válida. Intenta de nuevo.")

# Función principal del juego
def jugar():
    puntaje_jugador = 0
    puntaje_sistema = 0
    jugando = True
    while jugando:
        # Obtener las opciones del jugador y del sistema
        opcion_jugador = obtener_opcion_jugador()
        opcion_sistema = obtener_opcion_sistema()

        # Mostrar las opciones elegidas
        print(f"\nJugador eligió: {opcion_jugador}")
        print(f"Sistema eligió: {opcion_sistema}")

        # Determinar y mostrar el resultado
        resultado = determinar_ganador(opcion_jugador, opcion_sistema)
        print(resultado)

        # Actualizar puntajes
        if resultado == "¡Jugador gana!":
            puntaje_jugador += 1
        elif resultado == "¡Sistema gana!":
            puntaje_sistema += 1

        # Mostrar puntajes
        print(f"\nPuntaje acumulado: Jugador: {puntaje_jugador} - Sistema: {puntaje_sistema}")

        # Preguntar si quieren jugar otra vez
        jugar_otra_vez = input("¿Quieren jugar otra vez? (si/no): ").lower()
        if jugar_otra_vez != "si":
            jugando = False
            print("¡Gracias por jugar!")

# Iniciar el juego
mostrar_menu()
