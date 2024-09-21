import random

word = ['rainbow', 'computer', 'science', 'programming',
        'mathematics', 'player', 'condition',
        'reverse', 'water', 'board', 'geeks']

secret_word = random.choice(word).lower()
# print(f"The secret word is: {secret_word}")
display_word = ['_'] * len(secret_word)

guess_range = 0
guess_limit = 6
out_of_guess = False
guessed_letters = []

while ''.join(display_word) != secret_word and not out_of_guess:
    if guess_range < guess_limit:
        print(f"Current word: {' '.join(display_word)}")
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
        else:
            guessed_letters.append(guess)
            guess_range += 1

            if guess in secret_word:
                for idx, letter in enumerate(secret_word):
                    if letter == guess:
                        display_word[idx] = letter
                print(f"Good guess! {guess} is in the word.")
            else:
                print(f"Sorry, {guess} is not in the word.")

        print(f"Attempts left: {guess_limit - guess_range}")
    else:
        out_of_guess = True

if out_of_guess:
    print(f"You lose! The word was: {secret_word}")
else:
    print(f"Congratulations! You guessed the word: {secret_word}")
