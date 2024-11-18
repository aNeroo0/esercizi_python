fascine = 5
sacchi = 20
bancali = 50
spedizione = 3
legnaKg = 0.8

numFascine = int(input("Inserisci il numero di fascine (5kg) acquistate: "))
numSacchi = int(input("Inserisci il numero di sacchi (20kg) acquistati: "))
numBancali = int(input("Inserisci il numero di bancali (50kg) acquistati: "))

legnaTot = round((fascine*numFascine) + (sacchi*numSacchi) + (bancali*numBancali), 2)
costoTot = round(legnaTot*legnaKg, 2)

print(f"Peso totale della legna è {legnaTot}kg")
print(f"Per un prezzo di {costoTot}€")

if (legnaTot > 100):
  sconto = (legnaTot/100)*15
  costoTot = round(costoTot-sconto, 2)
  print(f"Prezzo applicando lo sconto del 15% è di: {costoTot}")
else:
  print("Nessuno Sconto Applicato!")

print("Spese di spedizioni di 3€")
costoTot = costoTot + spedizione

print(f"Prezzo Finale su scontrino: {costoTot}")
