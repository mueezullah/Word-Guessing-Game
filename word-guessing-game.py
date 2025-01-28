from random import randint

from fontTools.misc.cython import returns

# Open the words file and read all lines
file = open('words.txt', 'r')
words = file.readlines()
length = len(words)


# Function to get a random word from list
def get_Random_Word():
    random_no = randint(0, length - 1)
    word = words[random_no].strip()
    return word


# Function to handle game logic
def game_Play(random_word):
    chances = 10
    is_found = False
    guessed_letters = []
    print('\t' + '_ ' * len(random_word) + '\n')

    while chances > 0:
        guess = input('Guess the letter or the entire word: ')

        if guess == random_word:
            is_found = True
        else:
            if guess in guessed_letters:  # Check if the letter has already been guessed
                print(f"You have already guessed the letter '{guess}'. Try something else.\n")
                continue


            print('\t', end='')
            is_current_guess = False


            for letter in random_word:
                if letter == guess:
                    is_current_guess = True
                    guessed_letters.append(letter)
                    print(letter, end=' ')

                    if len(random_word) == len(guessed_letters):
                        is_found = True
                elif letter in guessed_letters:
                    print(letter, end=' ')
                else:
                    print('_', end=' ')
            print()

        if is_found:
            print(f"Congrats! Your guess was correct, the word was '{random_word}'.\n")
            break

        if not is_current_guess:
            print(f"'{guess}' is not in the word.")
            chances -= 1
            print(f'You have {chances} chances remaining.\n')

    if not is_found:
        print(f"\nSorry, your guesses were wrong. The word was '{random_word}'.\n")


# Main function to start the game
def main():
    print(" Word Guessing Game ".center(60, '-'))
    while True:
        random_word = get_Random_Word()
        game_Play(random_word)

        # Ask the user if they want to play again
        choice = input("If you want to play more, type 'yes' or 'YES'. Otherwise, type 'NO' or 'no' to quit: ")
        if choice in ['NO', 'no']:
            print("Thank you for playing! Goodbye!")
            break
        elif choice in ['yes', 'YES']:
            print("Great! Let's continue playing!")


# Entry point of the program
if __name__ == '__main__':
    main()
