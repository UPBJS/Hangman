import randomword


def game():
    lives = 7
    word = randomword.get_random_word()
    wordlen = len(word)
    guessedvalid = [word[0], word[-1]]
    guessedinvalid = []
    ungesslen = wordlen - 2
    showindexes = [i for i, x in enumerate(
        word) if x == word[0]] + [i for i, x in enumerate(word) if x == word[-1]]

    unguessedpart = word
    for ind in showindexes:
        unguessedpart = unguessedpart.replace(word[ind], "")
    displayword = word
    for ugp in list(unguessedpart):
        displayword = displayword.replace(ugp, "_")
    print(f"\nThe word is: {displayword}\n")
    # GUESSING
    wordguessed = False
    while not wordguessed:
        if displayword == word:
            wordguessed = True
            break
        if lives < 1:
            break
        guess = input("Input letter/word: ")

        if guess in word and len(guess) == 1:  # if letter and valid
            if guess in guessedvalid:
                print("This letter was already guessed !")
                continue
            print(f"The letter {guess} was IN the word!")
            guessedvalid.append(guess)
            guessindexes = [i for i, x in enumerate(word) if x == guess]
            for ind in guessindexes:
                unguessedpart = unguessedpart.replace(word[ind], "")
            displayword = list(displayword)
            for ind in guessindexes:
                displayword[ind] = word[ind]
            displayword = ''.join(displayword)
            for ugp in list(unguessedpart):
                displayword = displayword.replace(ugp, "_")
            print(f"""
==========================
The word is: {displayword}
--------------------------
Correct letters guessed: {', '.join(guessedvalid)}
Incorrect letters guessed: {', '.join(guessedinvalid)}
--------------------------
Lives remaining: [{lives}]
==========================
""")
        elif guess not in word and len(guess) == 1:  # if letter and invalid
            if guess in guessedinvalid:
                print("\nThis letter was already guessed !\n")
            else:
                guessedinvalid.append(guess)
                lives -= 1
                print("\nLetter was NOT in the word !")
                print(f"""
==========================
The word is: {displayword}
--------------------------
Correct letters guessed: {', '.join(guessedvalid)}
Incorrect letters guessed: {', '.join(guessedinvalid)}
--------------------------
Lives remaining: [{lives}]
==========================
""")

        # if word and correct
        elif guess in word and guess == word and len(guess) == len(word):
            print("The word is: "+word)
            displayword = word
        elif guess != word and len(guess) == len(word):  # if word and incorrect
            print("You lose! The word was "+word)
            return
        elif len(guess) > len(word) or len(guess) < len(word):  # if invalid size
            print(
                "Guess must be either a letter or a word with the lengh of "+str(len(word)))
    if lives > 0:
        print("Word was guessed correctly !")
    else:
        print("You lose! The word was "+word)


while True:
    try:
        game()
        invalid = True
        while invalid:
            playagain = input("Play again? [Yes/No]: ").lower()
            if playagain == "yes" or playagain == "no":
                invalid = False
                if playagain == "yes":
                    continue
                elif playagain == "no":
                    raise(KeyboardInterrupt)
            else:
                print("Please input either \"Yes\" or \"No\"...")
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
