naklon=int(input("Jaký je náklon robota? "))
if naklon > 10:
    print("Pozor, padam!")
elif naklon > 5:
    print("Nakláním se, koriguju")
else:
    print("Stojim rovne")