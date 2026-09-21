
# 1. Definición de la función con parámetros de entrada
def calcular_pago_por_persona(costo_total, porcentaje_propina, numero_personas):
    # Cálculo de la propina y del total acumulado
    propina = costo_total * (porcentaje_propina / 100)
    monto_total_con_propina = costo_total + propina
    # División equitativa entre los comensales
    monto_por_persona = monto_total_con_propina / numero_personas
    # Uso de la palabra clave return para enviar el resultado
    return monto_por_persona
# Bloque principal de ejecución
if __name__ == "__main__":
    print("=== CALCULADORA DE CUENTA Y PROPINA EN RESTAURANTE ===")
    # Entrada de datos desde el usuario
    costo = float(input("Ingrese el costo total de la comida: $"))
    propina_pct = float(input("Ingrese el porcentaje de propina que desea dejar (ej. 10): "))
    personas = int(input("Ingrese el número de personas: "))
    # Llamada a la función pasando los argumentos requeridos
    pago_individual = calcular_pago_por_persona(costo, propina_pct, personas)
    # Mostrar el resultado en pantalla con formato de dos decimales
    print("\n----------------------------------------------------")
    print(f"Cada persona debe pagar: ${pago_individual:.2f}")
    print("----------------------------------------------------")