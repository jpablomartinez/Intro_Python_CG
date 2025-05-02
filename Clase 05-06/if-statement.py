## Ejercicio 1; Manejo de puntaje
#actualRecord = int(input("Ingrese su puntaje: "))
#bestRecord = 100
#if actualRecord > bestRecord:
#    bestRecord = actualRecord
#else:
#    print("No subiste tu puntuación. L")
#print(f"Tu mejor record es {bestRecord} puntos")
MAXHP = 250
MAXPOTIONS = 10
hp = int(input("¿Cuánto hp te queda?: "))
if hp > MAXHP:
    print("Ese valor es inválido. Te dejaremos el máximo de 250 hp")
    hp = MAXHP
potions = int(input("¿Cuántas pociones te quedan?: "))
if potions > MAXPOTIONS:
    print("Ese valor es inválido. Te dejaremos el máximo de 10 pociones")
    potions = MAXPOTIONS
print("////////////////////////")
print(f"HP: {hp}")
print(f"Pociones: {potions}")
print("////////////////////////")
answer = int(input("¿Quieres usar una poción para recuperar salud?(1.Si / 2.No): "))
if answer == 1:
    if potions > 0:
        if hp == MAXHP:
            print("Tu vida está al máximo. Continua tu aventura")
        else:
            potions-=1
            hp+=50
            print("Te has curado")
            print(f"hp actual: {hp}")
            print(f"pociones: {potions}")
    else:
        print("Espero hayas guardado la partida. Continua con precaución")
else:
    print("Continua con tu aventura")