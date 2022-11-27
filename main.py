def main():
    import random

    print("H A N G M A N\n")

    games_won = 0
    games_lost = 0

    while True:
        game_start = input(
            'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: '
        )
        if game_start == "play":
            words = ["python", "java", "swift", "javascript"]
            random_word = random.choice(words)
            attempts = 8
            random_word_without_letters = "-" * len(random_word)
            print(random_word_without_letters)
            guessed = []
            while attempts != 0:
                guess_letter = input("Input a letter: ")
                # Check if input letter was single
                if len(guess_letter) > 1 or len(guess_letter) == 0:
                    print("Please, input a single letter.\n")
                    print(random_word_without_letters)
                    continue
                # Check if input letter is lower and in alphabet
                if not guess_letter.islower() or not guess_letter.isalpha():
                    print("Please, enter a lowercase letter from the English alphabet.\n")
                    print(random_word_without_letters)
                    continue
                # Check if the input letter from word that was already
                if guess_letter in guessed:
                    print("You've already guessed this letter.\n")
                    print(random_word_without_letters)
                    continue
                guessed.append(guess_letter)
                # Check if the input letter has already been entered
                if guess_letter in random_word:
                    for i in range(len(random_word)):
                        if guess_letter == random_word[i]:
                            # Code below replaces string in word
                            random_word_without_letters = random_word_without_letters[:i] + guess_letter + \
                                                          random_word_without_letters[i + 1:]
                else:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
                # checks if there are no extra characters left in the word
                if random_word_without_letters.isalpha():
                    print("You guessed the word", random_word_without_letters + "!")
                    print("You survived!")
                    games_won += 1
                    break
                print("")
                print(random_word_without_letters)
                if attempts == 0:
                    print("You lost!")
                    games_lost += 1
                    break
        elif game_start == "results":
            print("You won:", games_won, "times.")
            print("You lost:", games_lost, "times.")
        elif game_start == "exit":
            exit()


if __name__ == '__main__':
    main()
