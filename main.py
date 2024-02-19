from wonderwords import RandomWord
import hangman_art

print(hangman_art.logo)

r = RandomWord()

# Randomly generates a word from wonderwords and assigns it to a variable called chosen_word.
chosen_word = r.word()

# Empty list called display. For each letter in chosen_word, adds a "_" to 'display' list.
# represents each letter to guess.
display = []
for i in range(0, len(chosen_word)):
    display.append("_")

lives = 6

words_used = []

exit_game = True

# While loop to let the user guess again. The loop should stop once the user has guessed all the letter in the
# chosen_word and 'display' has no more blanks.
while exit_game:
    # Asks the user to guess a letter and assign their answer to a variable called guess. Also makes it lower case.
    guess = input("Guess a letter: ").lower()
    words_used.append(guess)

    # Check if the letter the user guessed is one of the letter in the chosen_word. If that letter in the display.
    # matches "guess"  then reveals that letter in the display at that position.
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]

    # if guess is not a letter in the chosen_word. The reduce lives by 1.
    # if lives goes down to 0 then the game should end.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            exit_game = False
            print(f"You lose! The word was {chosen_word}.")

    # Converts list into string.
    print(f"{' '.join(display)}")

    # check for winning clauses
    if "_" not in display:
        exit_game = True
        print("You win!")

    print(f"Words used {words_used}")

    print(hangman_art.stages[lives])
