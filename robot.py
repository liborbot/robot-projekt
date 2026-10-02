class Joint:
    def __init__(self, nazev, uhel):
        self.nazev = nazev
        self.uhel = uhel

    def vypis_stav(self):
        print("Kloub", self.nazev, "je na uhlu", self.uhel)

    def nastav_uhel(self, novy_uhel):
        self.uhel = novy_uhel

    def __str__(self):
        return "Kloub " + self.nazev + " (uhel " + str(self.uhel) + ")"

    def __repr__(self):
        return "Kloub " + self.nazev + " (uhel " + str(self.uhel) + ")"


class MotorizovanyKloub(Joint):
    def __init__(self, nazev, uhel, vykon):
        super().__init__(nazev, uhel)
        self.vykon = vykon

    def vypis_stav(self):
        super().vypis_stav()
        print(self.vykon)

class Robot:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.klouby = []

    def pridej_kloub(self, kloub):
        self.klouby.append(kloub)

robutek = Robot("Miloš")
kotnik1 = Joint("vrzavý", 30)
kotnik2 = Joint("namazaný", 80)
koleno = MotorizovanyKloub("ultrarychlý", 40, 250)
robutek.pridej_kloub(kotnik1)
robutek.pridej_kloub(kotnik2)
robutek.pridej_kloub(koleno)

for kloub in robutek.klouby:
    kloub.vypis_stav()

print(robutek.klouby)
print(koleno)

klouby = [Joint("koleno", 45),Joint("kotnik", 90),Joint("kycel", 20),]

serazene = sorted(klouby, key=lambda k: k.uhel)

for kloub in serazene:
    print(kloub)

def uhly_seznam(n):
    vysledek = []
    for i in range(n):
        vysledek.append(i * 10)
    return vysledek

print(uhly_seznam(5))

def uhly_generator(n):
    for i in range(n):
        yield i * 10

print(uhly_generator(5))

for u in uhly_generator(5):
    print(u)