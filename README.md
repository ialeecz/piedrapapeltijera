# Piedra, Papel o Tijera

Este proyecto implementa el clásico juego de "Piedra, Papel o Tijera" utilizando Python. Su propósito principal es reforzar conceptos clave de programación como estructuras de control, funciones, y manejo de datos a través de una aplicación interactiva y divertida.

---

## **Características**
- Interfaz en la terminal que permite al jugador interactuar fácilmente con el juego.
- Lógica para determinar el ganador entre el jugador y el sistema.
- Seguimiento de puntajes acumulados durante las partidas.
- Capacidad de jugar múltiples rondas o salir del juego en cualquier momento.

---

## **Requisitos**
Para ejecutar el código, necesitas:
- Python 3 instalado en tu computadora.

---

## **Cómo jugar**
1. Clona este repositorio o descarga el archivo `piedra_papel_tijera.py`.
2. Abre una terminal y navega al directorio donde guardaste el archivo.
3. Ejecuta el juego con el siguiente comando:
   ```bash
   python piedra_papel_tijera.py
   ```
4. Sigue las instrucciones en pantalla:
   - Selecciona entre "Piedra", "Papel" o "Tijera".
   - Revisa quién gana cada ronda.
   - Decide si quieres jugar otra vez o salir.

---

## **Estructura del código**
### **1. Opciones y funciones principales**
- `opciones`: Lista que contiene las opciones disponibles (piedra, papel, tijera).
- `obtener_opcion_jugador`: Pide al jugador que elija una opción válida.
- `obtener_opcion_sistema`: Selecciona una opción aleatoria para la computadora usando la biblioteca `random`.
- `determinar_ganador`: Compara las opciones del jugador y el sistema para determinar el ganador.

### **2. Menú principal**
La función `mostrar_menu` presenta las opciones del juego:
- Jugar.
- Salir.
Si el jugador elige jugar, se llama a la función principal `jugar`. Si elige salir, el programa termina.

### **3. Lógica del juego**
La función `jugar` realiza lo siguiente:
- Inicializa los puntajes del jugador y del sistema.
- Ejecuta un bucle para que las rondas continúen hasta que el jugador decida salir.
- Muestra los puntajes acumulados y pregunta si desea jugar otra ronda.

---

## **Objetivo del Proyecto**
El objetivo es brindar una experiencia educativa e interactiva que refuerce conocimientos en programación y permita explorar cómo construir un software funcional y accesible.

---

## **Autor**
Desarrollado como parte del proyecto final integrador de programación.
