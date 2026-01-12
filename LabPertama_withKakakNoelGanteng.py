kata = "mangga"

print("Game Tebak Kata")
print("Hint: Buah berwarna hijau/kuning")

while True:
    tebakan = input("Masukkan tebakan kamu: ")

    if tebakan == kata:
        print("Benar!")
        break
    else:
        print("Salah, coba lagi.")