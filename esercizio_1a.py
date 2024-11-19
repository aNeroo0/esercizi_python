num1 = int(input("Inserisci il primo voto: "))
num2 = int(input("Inserisci il secondo voto: "))
num3 = int(input("Inserisci il terzo voto: "))

mediaInfo = int(input("Come vuoi la media (1 in centesimi o 2 trentesimi): "))

media = ( num1 + num2 + num3 ) / 3

if ( mediaInfo == 1 ):
    print("Media selezionata in centesimi!")
    media = ( media*100 ) / 30
    print(f"La media viene {media}")
elif ( mediaInfo == 1):
    print("Media selezionata in trentesimi!")
else:
    print("Media NON selezionata in modo corretto!")

