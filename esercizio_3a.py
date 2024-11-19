lancio1 = float(input("Inserisci il valore del primo lancio: "))
lancio2 = float(input("Inserisci il valore del secondo lancio: "))
lancio3 = float(input("Inserisci il valore del terzo lancio: "))
lancio4 = float(input("Inserisci il valore del quarto lancio: "))
lancio5 = float(input("Inserisci il valore del quinto lancio: "))

somma = lancio1 + lancio2 + lancio3 + lancio4 + lancio5

if (lancio1 == 0):
    media = somma / 4
    if (lancio2 == 0):
        media = somma / 3
        if (lancio3 == 0):
            media = somma / 2
            if (lancio4 == 0):
                media = somma / 1
                if (lancio5 == 0):
                    print("Tutti i lanci sono nulli!")
elif (lancio2 == 0):
    media = somma / 4
    if (lancio3 == 0):
        media = somma / 3
        if (lancio4 == 0):
            media = somma / 2
            if (lancio5 == 0):
                media = somma / 1
elif (lancio3 == 0):
    media = somma / 4
    if (lancio4 == 0):
        media = somma / 3
        if (lancio5 == 0):
            media = somma / 2
elif (lancio4 == 0):
    media = somma / 4
    if (lancio5 == 0):
        media = somma / 3
else:
    media = somma / 4

print(f"La media dei lanci è {media}")