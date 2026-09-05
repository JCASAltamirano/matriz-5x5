# ==========================================
# Programa: Reserva de asiento en sala de cine by Juan Altamirano
# ==========================================
# Inicializamos todos los valores en 0 (0 = asiento libre)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print("=== SISTEMA DE RESERVAS MULTICINES EC ===")
print("La sala tiene 3 filas (0 a 2) y 4 columnas (0 a 3).\n")
# Utilizamos input() para leer el dato y int() para convertirlo a número entero
fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))
# Se accede al elemento exacto utilizando los índices proporcionados por el cliente
asientos[fila][columna] = 1
print("\nEstado de la sala (0 = Libre, 1 = Reservado):")
# Bucle externo para recorrer las 3 filas
for i in range(3):
    # Bucle interno para recorrer las 4 columnas de la fila actual
    for j in range(4):
        # Imprimimos el valor del asiento
        print(asientos[i][j], end=" ")
        # Imprimimos un salto de línea al terminar de recorrer cada fila
    print()