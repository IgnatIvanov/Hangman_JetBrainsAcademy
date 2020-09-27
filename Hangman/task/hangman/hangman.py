# Write your code here
import random

print("H A N G M A N")
while True:
    player_command = input('Type "play" to play the game, "exit" to quit: ')
    if player_command == "exit":
        break
    elif player_command == "play":
        tries = 8
        vocabulary = tuple(['python', 'java', 'kotlin', 'javascript'])
        computer_word = vocabulary[random.randint(0, 3)]
        player_letters = set()
        current_state_word = ""
        while tries > 0:
            print("")
            for i in range(len(computer_word)):
                if computer_word[i] in player_letters:
                    current_state_word += computer_word[i]
                else:
                    current_state_word += "-"
            print(current_state_word)
            if "-" not in current_state_word:
                break
            while True:
                user_input = input("Input a letter: ")
                if len(user_input) != 1 or user_input == " ":
                    print("You should input a single letter")
                    print()
                    print(current_state_word)
                elif user_input not in "abcdefghijklmnopqrstuvwxyz":
                    print("It is not an ASCII lowercase letter")
                    print()
                    print(current_state_word)
                elif user_input in player_letters:
                    print("You already typed this letter")
                    print()
                    print(current_state_word)
                else:
                    break

            current_state_word = ""

            if user_input not in set(computer_word):
                print("No such letter in the word")
                tries -= 1
            player_letters.add(user_input)

        if tries == 0:
            print("You lost!")
        else:
            print("You guessed the word!")
            print("You survived!")
        print()
