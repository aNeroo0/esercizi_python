media = float(input("Insersci la media dei voti della pagella: "))

anno = int(input("Inserisci l'anno scolastico (3, 4 o 5): "))

if ( anno == 3 ):
    if ( media < 6 ):
        print("Media non valida")
    elif ( media > 10 ):
        print("Media non valida")
    elif ( media == 6):
        print("Credito 7-8")
    elif ( media <= 7 ):
        print("Credito 8-9")
    elif ( media <= 8 ):
        print("Credito 9-10")
    elif ( media <= 9 ):
        print("Credito 10-11")
    else:
        print("Credito 11-12")
elif ( anno == 4 ):
    if ( media < 6 ):
        print("Media non valida")
    elif ( media > 10 ):
        print("Media non valida")
    elif ( media == 6):
        print("Credito 8-9")
    elif ( media <= 7 ):
        print("Credito 9-10")
    elif ( media <= 8 ):
        print("Credito 10-11")
    elif ( media <= 9 ):
        print("Credito 11-12")
    else:
        print("Credito 12-13")
elif ( anno == 5 ):
    if ( media < 6 ):
        print("Media non valida")
    elif ( media > 10 ):
        print("Media non valida")
    elif ( media == 6):
        print("Credito 9-10")
    elif ( media <= 7 ):
        print("Credito 10-11")
    elif ( media <= 8 ):
        print("Credito 11-12")
    elif ( media <= 9 ):
        print("Credito 13-14")
    else:
        print("Credito 14-15")
else:
    print("Anno non valido!")