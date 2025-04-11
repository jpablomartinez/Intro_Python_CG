# 1. Pedir al usuario la conversion a realizar (F) para farenheit o (K) para Kelvin
unit = input("Ingrese unidad de conversión (K) o (F): ")
#1.1 Validar opción
if unit != "K" and unit != "F":
    print(f"La opción {unit} no es válida")    
else:
    #2. Pedir al usuario la temperatura en celcius que desea convertir
    celcius = float(input("Ingrese la temperatura en Celcius: "))
    if unit == "K":
        kelvin = celcius + 273.15
        print(f"La temperatura en Kelvin es: {kelvin} {unit}º")
    elif unit == "F":    
        farenheit = (celcius * 1.8) + 32
        print(f"La temperatura en Farenheit es: {farenheit} {unit}º")