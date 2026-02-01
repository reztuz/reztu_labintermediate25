def updateText(answer, opened):
    text = ""
    for i in range(len(answer)):
        if opened[i]:
            text += answer[i]
        else:
            text += "_"

        if i != len(answer) - 1:
            text += " "
    return text


def main(answer):
    lives = 5
    opened = [False] * len(answer)

    while lives > 0:
        display = updateText(answer, opened)
        print("Kata:", display)
        print("Sisa nyawa:", lives)

        guess = input("Tebak huruf: ")

        found = False
        for i in range(len(answer)):
            if answer[i] == guess:
                opened[i] = True
                found = True

        if found:
            print("Huruf", guess, "ada di kata!")

        if not found:
            lives -= 1
            print("Huruf tidak ada!")

        if "_" not in display:
            print("Kata:", display)
            print("Selamat anda berhasil!!!!")
            return

    print("Game over!")


main("answer")