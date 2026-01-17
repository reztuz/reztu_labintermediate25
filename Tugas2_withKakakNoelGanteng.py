#ini variabel nya 

word = "python"
display = ["_"] * len(word)
used = []
attempts = 6

#abisfu ini logika gamenya
while attempts > 0 and "_" in display:
    print("Word:", " ".join(display))
    print("Attempts:", attempts)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input")
        continue

    if guess in used:
        print("Already guessed")
        continue

    used.append(guess)

    if guess in word:
        i = 0
        while i < len(word):
            if word[i] == guess:
                display[i] = guess
            i += 1
    else:
        attempts -= 1
# ini akhirnya buat hasilnya
if "_" not in display:
    print("You win! Word:", word)
else:
    print("You lose! Word:", word)
#selese ye
