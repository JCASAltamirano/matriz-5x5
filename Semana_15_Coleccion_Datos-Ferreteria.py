def gestionar_ferreteria():
    # 1. Creamos la colección de datos (Diccionario)
    # Inicializamos un diccionario vacío para almacenar los productos y sus precios.
    inventario_ferreteria = {}
    # 2. Agregamos los datos a la colección
    # Insertamos los productos simulando el registro en el sistema.
    inventario_ferreteria["Martillo"] = 12.50
    inventario_ferreteria["Caja de Clavos 2 pulgadas"] = 3.25
    inventario_ferreteria["Taladro"] = 85.00
    inventario_ferreteria["Destornillador Estrella"] = 4.75
    inventario_ferreteria["Cemento Holcim (saco)"] = 7.80
    print("--- REGISTRO EXITOSO ---")
    print("Los productos han sido agregados al sistema.\n")
    # 3. Mostramos de forma clara la información almacenada en la pantalla
    # Utilizamos un bucle for para 'recorrer' los elementos e imprimirlos.
    print("--- INVENTARIO ACTUAL DE LA FERRETERÍA ---")
    for producto, precio in inventario_ferreteria.items():
        print(f"• {producto}: ${precio:.2f}")
    print("------------------------------------------\n")
    # 4. Operación básica: BUSCAR un elemento
    producto_a_buscar = "Taladro"
    print(f"--- BUSCANDO PRODUCTO: '{producto_a_buscar}' ---")
    if producto_a_buscar in inventario_ferreteria:
        precio_encontrado = inventario_ferreteria[producto_a_buscar]
        print(f"Resultado: El producto está disponible y cuesta ${precio_encontrado:.2f}\n")
    else:
        print("Resultado: Producto no encontrado en el inventario.\n")
    # 4. Operación básica: ELIMINAR un elemento
    producto_a_eliminar = "Caja de Clavos 2 pulgadas"
    print(f"--- ELIMINANDO PRODUCTO: '{producto_a_eliminar}' ---")
    if producto_a_eliminar in inventario_ferreteria:
        del inventario_ferreteria[producto_a_eliminar]
        print(f"Éxito: '{producto_a_eliminar}' ha sido retirado del sistema.\n")
    # Imprimimos el inventario final para comprobar la eliminación
    print("--- INVENTARIO ACTUALIZADO ---")
    for producto, precio in inventario_ferreteria.items():
        print(f"• {producto}: ${precio:.2f}")
# Bloque principal de ejecución
if __name__ == "__main__":
    gestionar_ferreteria()