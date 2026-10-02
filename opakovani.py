def secti(a, b):
    return a + b

vysledek = secti(3, 4)
print(vysledek)
try:
    cislo = int("chyba")
    print(cislo)
except ValueError:
    print("To neni cislo, preskakuji")