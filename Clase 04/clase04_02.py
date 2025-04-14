#Como Ingenierios de Software del parque de diversiones CodingLandia
#Deben hacer un programa que evalue si un niñ@ puede subir a la montaña rusa.
#Las condiciones son:
#1. Si va acompañado de adulto, entonces debe medir al menos 110 cm
#2. Si va solo, entonces debe medir al menos 140 cm
#3. Si cualquiera de esas condiciones no se cumple, entonces no puede subir al juego
#4. El programa debe mostrar un texto que indique si puede pasar o no

alone = input("¿El niño/niña va con sus padres? (si)/(no): ")
height = int(input("Ingrese estatura (cm) del niño/niña: "))

if alone == "si" and height < 110:
    print("No puede subir")
elif alone == "si" and height >= 110:
    print("Puede subir")
elif alone == "no" and height < 140:
    print("No puede subir")
elif alone == "no" and height >= 140:
    print("Puede subir")