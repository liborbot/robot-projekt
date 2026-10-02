with open("senzory.txt") as soubor:
    for radek in soubor:
        try:
            cislo = int(radek.strip())
            print(cislo)
        except ValueError:
            print("Preskakuji chybny radek:", radek.strip())
print(radek)