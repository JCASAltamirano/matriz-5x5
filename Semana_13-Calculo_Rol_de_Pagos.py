# ==========================================
# Cálculo de Horas Extras y aporte al IESS
# ==========================================
# 1. Declaración de la función usando la palabra reservada 'def'
# 2. La función recibe exactamente dos parámetros (valor_hora y cantidad_horas)
def calcular_pago_extras(valor_hora, cantidad_horas):
    """
    Calcula el monto total a pagar por las horas extras.
    Equivale a la lógica de: total = precio * cantidad
    """
    # 3. Dentro de la función se realiza el cálculo
    monto_total = valor_hora * cantidad_horas
    
    # 4. La función retorna el resultado con 'return'
    return monto_total

# 5. Bloque principal del programa
if __name__ == "__main__":
    print("=== SISTEMA DE CÁLCULO DE HORAS EXTRAS Y ROL DE PAGOS ===")
    
    # Ingresamos el salario mensual del trabajador
    salario_mensual = float(input("Ingrese su salario mensual (ej. 482.00): $"))
    
    # Ingresamos el número de horas extras de ambos tipos (puede ingresar 0 si no hizo alguna)
    print("\nIngrese la cantidad de horas extras trabajadas en el mes (ingrese 0 si no aplica):")
    horas_50 = float(input("Número de horas suplementarias (50%): "))
    horas_100 = float(input("Número de horas extraordinarias (100%): "))
    
    # Cálculo del valor de la hora ordinaria (divisor legal 240)
    valor_hora_ordinaria = salario_mensual / 240
    
    # Cálculo de los factores de recargo
    valor_hora_50 = valor_hora_ordinaria * 1.5  # Recargo del 50%
    valor_hora_100 = valor_hora_ordinaria * 2.0 # Recargo del 100%
    
    # Llamamos a la función para cada tipo de hora extra
    pago_suplementarias = calcular_pago_extras(valor_hora_50, horas_50)
    pago_extraordinarias = calcular_pago_extras(valor_hora_100, horas_100)
    
    # Sumamos el total ganado por horas extras
    total_horas_extras = pago_suplementarias + pago_extraordinarias
    
    # Calculamos el total de ingresos
    ingresos_totales = salario_mensual + total_horas_extras
    
    # Calculamos el aporte personal al IESS (9.45%) sobre el total de ingresos
    descuento_iess = ingresos_totales * 0.0945
    
    # Calculamos el líquido a recibir
    liquido_neto = ingresos_totales - descuento_iess
    
    # Mostramos el resultado en consola con print() según el formato solicitado
    print("\n==========================================")
    print("      RESUMEN DEL ROL DE PAGOS NETO       ")
    print("==========================================")
    print(f"Salario base mensual:     ${salario_mensual:.2f}")
    print(f"Total horas extras:       ${total_horas_extras:.2f}")
    print("------------------------------------------")
    print(f"Ingresos totales:         ${ingresos_totales:.2f}")
    print(f"Descuento IESS (9,45%):   ${descuento_iess:.2f}")
    print(f"Líquido neto a recibir:   ${liquido_neto:.2f}")
    print("==========================================")