def stav_naklonu(naklon):
    if naklon > 10:
        return "padam"
    elif naklon > 5:
        return "koriguji"
    else:
        return "stojim rovne"

print(stav_naklonu(12))
print(stav_naklonu(7))
print(stav_naklonu(2))