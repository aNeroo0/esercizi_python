# Analisi delle vendite di negozi
n = int(input("Quanti negozi vuoi inserire: "))
while(n<1):
    print("Numero negozi <= 0")
    n = int(input("Quanti negozi vuoi inserire: "))

vetMin = []
vetMax = []
somMin = 0
somMax = 0

for i in range(n):
    print(f"NEGOZIO {i+1}")
    vMin = float(input("Inserisci prezzo vendita minima: "))
    vetMin.append(vMin)
    somMin += vMin 

    vMax = float(input("Inserisci prezzo vendita massima: "))
    vetMax.append(vMax)
    somMax += vMax

mediaMin = somMin/n
print(f"Media vendite minime: {mediaMin}")  
print(f"Media vendite massime: {somMax/n}") 

for i in range(n):
    if(vetMin[i] < mediaMin):
        print(f"Negozio {i+1} ha vendita minima inferire alla media!")

cercaNegozio = int(input("Inserisci il numero negozio che stai cercando (1,2,3...): "))
j = cercaNegozio-1
if(j>0 and j<=n):
    print(f"NEGOZIO {cercaNegozio}")
    print(f"Vendita massima: {vetMax[j]}")
    print(f"Vendita minima: {vetMin[j]}")
else:
    print("Negozio non trovato!")

venMax = vetMax[0]
venMin = vetMin[0]
for i in range(n,1):
    if(venMax < vetMax[i]):
        venMax = vetMax[i]
    elif(venMin > vetMin[i]):
        venMin = vetMin[i]