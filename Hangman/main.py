import random
import hangman_wordlist
import hangman_art

end_of_game = False
word = random.choice(hangman_wordlist.word_list)
word_length = len(word)
lives = 6
print(hangman_art.logo)

display = []
for letter in word:
    display += "_"

while not end_of_game:
    print(hangman_art.stages[lives])
    print(display)
    user_guess = input("\nGuess a letter: ").lower()
    if user_guess in display:
        print(f"You've already guessed {user_guess}, try a different letter. ")
    for position in range(word_length):
        letter = word[position]
        if letter == user_guess:
            display[position] = letter
    if user_guess not in word:
        print(f"{user_guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print(hangman_art.stages[0])
            end_of_game = True
            print("You lose. ")
    if "_" not in display:
        end_of_game = True
        print("You win. ")

















