tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
    ]),
    ("Cusago", [
        ("gennaio", ("elettrico", 310)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
    ]),
    ("Napoli", [
        ("gennaio", ("elettrico", 350)),
        ("gennaio", ("gas", 120)),
        ("febbraio", ("elettrico", 290)),
        ("febbraio", ("gas", 160)),
    ]),
    ("Rimini", [
        ("gennaio", ("elettrico", 250)),
        ("gennaio", ("gas", 110)),
        ("febbraio", ("elettrico", 110)),
        ("febbraio", ("gas", 160)),
    ]),
    ("Magenta", [
        ("gennaio", ("elettrico", 320)),
        ("gennaio", ("gas", 50)),
        ("febbraio", ("elettrico", 180)),
        ("febbraio", ("gas", 120)),
    ]),
)


def analizza_consumi_energetici(citta, risorsa, tupla_consumi_energetici):
    media = calcolo_media(citta, risorsa, tupla_consumi_energetici)
    if media == -1:
        print("Citta o servizio non trovato!")
        return None 
    else:
        valoreMax, meseMax = max_risorsa(citta, risorsa, tupla_consumi_energetici)
        tuplaFinale = (media, (valoreMax, meseMax))
        return tuplaFinale
    

def calcolo_media(citta, risorsa, tupla_consumi_energetici):
    somma = 0
    i = 0
    for nome, dati_consumo in tupla_consumi_energetici:
        if nome == citta:
            for mese, risorsa_consumo in dati_consumo:
                servizio, num = risorsa_consumo
                if risorsa == servizio:
                    somma += num
                    i+=1
            break
            
    if i > 0:
        media = round(somma/i, 2)
        return media
    else:
        return -1

def max_risorsa(citta, risorsa, tupla_consumi_energetici):
    Vmax = 0
    Mmax = None
    for nome, dati_consumo in tupla_consumi_energetici:
        if nome == citta:
            for mese, risorsa_consumo in dati_consumo:
                servizio, num = risorsa_consumo
                if risorsa == servizio:
                    if num > Vmax:
                        Vmax = num
                        Mmax = mese
            break
            
    return Vmax, Mmax

while True:
    print("")
    print("1. Analizza consumi energetici")
    print("2. Esci")
    
    try:
        n_str = input("Inserisci numero comando: ")
        n = int(n_str)
    except ValueError:
        print("Errore! Riprova")
        continue
        
    print("")
    if n == 1:
        citta = input(str("Inserisci il nome della città: "))
        risorsa = input(str("Inserisci nome risorsa: "))
        tuplaFinale = analizza_consumi_energetici(citta, risorsa, tupla_consumi_energetici)
        if tuplaFinale is not None:
             print(tuplaFinale)
    elif n == 2:
        print("Programma Terminato!")
        break
    else:
        print("Errore! Riprova")
