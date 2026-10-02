def s_rameckem(funkce):
    def obal():
        print("=====")
        funkce()
        print("=====")
    return obal


@s_rameckem
def pozdrav():
    print("Ahoj robote")


def rozlouceni():
    print("Čau robote")


pozdrav()
rozlouceni()

with open("uhly.txt", "w") as f:
    f.write("45\n")
    f.write("90\n")
    f.write("20\n")

print("Hotovo, soubor zapsán.")

with open("uhly.txt", "r") as f:
    obsah = f.read()

print(obsah)