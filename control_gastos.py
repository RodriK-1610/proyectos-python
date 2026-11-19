print("=== BIENVENIDO A TU ASISTENTE DE AHORRO Y TAREAS ===")
presupuesto_inicial = float(input("¿Cuál es tu presupuesto inicial disponible? "))
presupuesto = presupuesto_inicial

gastos = []
tareas = []

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar un gasto")
    print("2. Agregar una tarea o pendiente")
    print("3. Ver resumen de ahorro y tareas")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        monto = float(input("¿Cuánto gastaste? "))
        gastos.append(monto)
        presupuesto = presupuesto - monto
        print("Gasto guardado. Te quedan:", presupuesto)
        
    elif opcion == "2":
        tarea = input("Escribe tu tarea o recordatorio: ")
        tareas.append(tarea)
        print("Tarea agregada.")
        
    elif opcion == "3":
        print("\n--- RESUMEN ACTUAL ---")
        print("Presupuesto inicial:", presupuesto_inicial)
        print("Total gastado:", sum(gastos))
        print("Saldo disponible para ahorrar:", presupuesto)
        print("Tus tareas pendientes:", tareas)
        
    elif opcion == "4":
        print("¡Excelente trabajo organizando tu día! Hasta luego.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
