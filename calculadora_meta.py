nombre = input("¿Cómo te llamas? ")
sueldo_usd = float(input("¿Cuántos dólares al mes quieres ganar? "))
gastos_usd = float(input("¿Cuántos dólares gastarás al mes? "))

ahorro_mes = sueldo_usd - gastos_usd
ahorro_5_anios = ahorro_mes * 12 * 5

print("Hola", nombre)
print("Tu ahorro libre al mes será:", ahorro_mes, "USD")
print("En 5 años acumularás:", ahorro_5_anios, "USD")

