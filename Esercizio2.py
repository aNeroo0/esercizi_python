# Gestione delle prenotazioni dei voli aerei
# Da non svolgere richiesta 3 e 4

n = int(input("Quanti voli ci sono: "))
while(n<1):
    print("Numero voli <= 0")
    n = int(input("Quanti voli ci sono: "))

partVolo = []
arrVolo = []
destVolo = []

for i in range(n):
    print(f"VOLO N.{i+1}")
    dest = str(input("Destinazione volo: "))
    destVolo.append(dest)
    part = int(input("Ora di partenza del volo: "))
    partVolo.append(part)
    arr = int(input("Ora di arrivo volo: "))
    while(arr<part):
        print("Ora di Arrivo minore di Ora di Partenza ")
        arr = int(input("Ora di arrivo volo: "))
    arrVolo.append(arr)


destinazione = str(input("Inserisci destinazione: "))
for i in range(n):
    if(destinazione==destVolo[i]):
        print(f"VOLO N.{i+1}")
        print(f"Partenza: {partVolo[i]}")
        print(f"Arrivo: {arrVolo[i]}")

