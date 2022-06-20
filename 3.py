Data = []

while True:
    user = input("Masukan Angka: ")
    if user == "n":
        break
    Data.append(int(user))

total = sum(Data)
rata = total/len(Data)
print(rata)
