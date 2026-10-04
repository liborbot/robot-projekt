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

    def vypis_stav_robota(self):
        print(self.jmeno)
        for kloub in self.klouby:
            kloub.vypis_stav()

r = Robot("Miloš")
r.pridej_kloub(Joint("koleno", 45))
r.pridej_kloub(Joint("kotnik", 90))
r.pridej_kloub(MotorizovanyKloub("kycel", 30, 100))

r.vypis_stav_robota()