cislo = []
with open("senzory.txt") as soubor:
    for radek in soubor:
        try:
            radek = int(radek.strip())
            cislo.append(radek)
        except ValueError:
            print("Preskakuji radek:", radek.strip())

minimum = min(cislo)
maximum = max(cislo)
suma = sum(cislo)
prumer = sum(cislo) / len(cislo)

print("Prumer: ", prumer)
print("Minimum: ", minimum)
print("Maximum: ", maximum)