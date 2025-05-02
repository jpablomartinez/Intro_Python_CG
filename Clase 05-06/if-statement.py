## Ejercicio 1; Manejo de puntaje
actualRecord = int(input("Ingrese su puntaje: "))
bestRecord = 100
if actualRecord > bestRecord:
    bestRecord = actualRecord
else:
    print("No subiste tu puntuación. L")
print(f"Tu mejor record es {bestRecord} puntos")