import os

# Guardar el archivo en la misma carpeta exacta donde está este código
CARPETA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(CARPETA, "datos_asistente.txt")

def guardar_datos():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write(f"{presupuesto_inicial}\n")
        f.write(f"{presupuesto}\n")
        f.write(",".join(str(g) for g in gastos) + "\n")
        f.write("|".join(tareas) + "\n")

# 1. Cargar datos si el archivo ya existe y tiene información
if os.path.exists(ARCHIVO) and os.path.getsize(ARCHIVO) > 0:
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lineas = f.read().splitlines()
        presupuesto_inicial = float(lineas[0])
        presupuesto = float(lineas[1])
        gastos = [float(x) for x in lineas[2].split(",")] if len(lineas) > 2 and lineas[2] else []
        tareas = lineas[3].split("|") if len(lineas) > 3 and lineas[3] else []
    print("\n✅ ¡Bienvenido de vuelta! Tus datos anteriores fueron cargados.")
else:
    print("\n=== BIENVENIDO A TU ASISTENTE DE AHORRO Y TAREAS ===")
    presupuesto_inicial = float(input("¿Cuál es tu presupuesto inicial disponible? "))
    presupuesto = presupuesto_inicial
    gastos = []
    tareas = []
    guardar_datos()  # Guarda el presupuesto apenas lo escribes

while True:
    print("\n--- MENÚ PRINCIPAL (V2 CON MEMORIA) ---")
    print("1. Registrar un gasto")
    print("2. Agregar una tarea o pendiente")
    print("3. Ver resumen de ahorro y tareas")
    print("4. Reiniciar presupuesto y datos")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "1":
        monto = float(input("¿Cuánto gastaste? "))
        gastos.append(monto)
        presupuesto = presupuesto - monto
        guardar_datos()
        print("Gasto guardado en memoria. Te quedan:", presupuesto)
        if presupuesto < presupuesto_inicial * 0.20:
            print("⚠️ ALERTA: Te queda menos del 20% de tu presupuesto.")
        
    elif opcion == "2":
        tarea = input("Escribe tu tarea o recordatorio: ")
        tareas.append(tarea)
        guardar_datos()
        print("Tarea guardada.")
        
    elif opcion == "3":
        print("\n--- RESUMEN ACTUAL ---")
        print("Presupuesto inicial:", presupuesto_inicial)
        print("Total gastado:", sum(gastos))
        print("Saldo disponible para ahorrar:", presupuesto)
        print("Tus tareas pendientes:", tareas)
        
    elif opcion == "4":
        presupuesto_inicial = float(input("Ingresa el nuevo presupuesto inicial: "))
        presupuesto = presupuesto_inicial
        gastos = []
        tareas = []
        guardar_datos()
        print("Datos reiniciados correctamente.")
        
    elif opcion == "5":
        print("¡Todo guardado! Hasta luego, Rodrigo.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
