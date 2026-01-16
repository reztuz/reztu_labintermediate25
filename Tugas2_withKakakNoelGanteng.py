import random

word = random.choice(["python", "game", "code"])
guessed = []
display = ["_"] * len(word)
attempts = 6

print("HANGMAN 2.0")
print(" ".join(display))

while attempts > 0 and "_" in display:
    letter = input("Guess a letter: ").lower()

    # error check
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input")
        continue

    # repeated guess
    if letter in guessed:
        print("Already guessed")
        continue

    guessed.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
    else:
        attempts -= 1

    print(" ".join(display))
    print("Attempts left:", attempts)

if "_" not in display:
    print("You win! Word:", word)
else:
    print("You lose! Word:", word)
