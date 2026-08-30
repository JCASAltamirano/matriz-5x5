matriz = [[0 for _ in range(5)] for _ in range(5)]
print("=== INGRESO DE DATOS (MATRIZ 5x5) ===")
for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor numérico para la posición [{i}][{j}]: "))
        matriz[i][j] = valor
print("\n=== MATRIZ INGRESADA ===")
for i in range(5):
    for j in range(5):
        # end="\t" evita el salto de línea y tabula el espacio entre columnas
        print(matriz[i][j], end="\t")
    print()