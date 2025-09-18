tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

def media_gol_totali(tupla_partite):
    somma = 0
    media = 0
    conteggio = 0
    for _,_,gol1,gol2 in tupla_partite:
        somma = gol1 + gol2 + somma
        conteggio += 1
    media = somma/conteggio

    return media

def media_gol_squadra(tupla_partite, s):
    somma = 0
    j = 0
    for s1,s2,gol1,gol2 in tupla_partite:
        if s1.lower() == s.lower():
            somma = somma + gol1
            j+=1
        elif s2.lower() == s.lower():
            somma = somma + gol2
            j+=1
    media = somma/j

    return media

def partita_piu_gol(tupla_partite):
    sq1 = ""
    sq2 = ""
    max = 0
    partita = []
    for s1,s2,gol1,gol2 in tupla_partite:
        somma = 0
        somma = gol1 + gol2
        if somma>max:
            max = somma
            sq1 = s1
            sq2 = s2
    partita.append(sq1)
    partita.append(sq2)
    partita.append(max)
    print(partita)

def percentuale_vittorie_squadra(tupla_partite, s):
    giocate = 0
    vinte  = 0
    for s1,s2,gol1,gol2 in tupla_partite:
        if s1.lower() == s.lower():
            giocate+=1
            if gol1>gol2:
                vinte+=1
        elif s2.lower() == s.lower():
            giocate+=1
            if gol2>gol1:
                vinte+=1
    if giocate == 0:
        print("Errore! Squadra non trovata")
    else:
        percentuale = (vinte/giocate)*100
        print("Squadra: ", s)
        print("Partite giocate: ", giocate)
        print("Partite vinte: ", vinte)
        print(f"Percentuale: {percentuale}%")
            

while True:
    print("")
    print("1. Media gol totali")
    print("2. Media gol squadra scelta")
    print("3. Partita con più gol")
    print("4. Percentuale partite vinte da una squadra scelta")
    print("5. Esci")
    n = int(input("Inserisci numero comando: "))
    print("")
    if n == 1:
        media = media_gol_totali(tupla_partite)
        if media == 0:
            print("Errore!")
        else:
            print("La media dei gol è: ", media)
    elif n == 2:
        s = str(input("Inserisci nome squadra: "))
        media = media_gol_squadra(tupla_partite, s)
        if media == 0:
            print("Errore!")
        else:
            print(f"Media gol della squadra {s}: {media}")
    elif n == 3:
        partita_piu_gol(tupla_partite)
    elif n == 4:
        s = str(input("Inserisci nome squadra: "))
        percentuale_vittorie_squadra(tupla_partite, s)
    elif n == 5:
        print("Programma Terminato!")
        break
    else:
        print("Errore! Riprova")