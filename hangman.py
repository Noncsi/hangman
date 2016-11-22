import sys
import os
import random

file_with_words = 'hangman_word.txt'  # the file with the words

# os.system('cls' if os.name == 'nt' else 'clear') #clean the field


def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')  # clean the field
    welcome_text = "Greetings, fellow adventurer. You just entered a world where are only two options:\
    \nVictory or Death!\
    \nGuess the word what we gave by entering characters one by one.\
    \nIf you entered a letter that doesn't exist in the word,\
    \n...well...\
    \nLet's play!"
    print ('\n'.join('{:^150}'.format(s) for s in welcome_text.split('\n')))
    print (hanging_visual_process[0])

hanging_visual_process = ["               ____________\
                           \n               |         ||\
                           \n               |         ||\
                           \n               |         ||\
                           \n                         ||\
                           \n                         ||\
                           \n                         ||\
                           \n                         ||\
                           \n                        /||\ \
                           \n                    ============",
                          "               ____________\
                           \n               |         ||\
                           \n               |         ||\
                           \n               |         ||\
                           \n               O         ||\
                           \n                         ||\
                           \n                         ||\
                           \n                         ||\
                           \n                        /||\ \
                           \n                    ============",
                          "               ____________\
                           \n               |         ||\
                           \n               |         ||\
                           \n               |         ||\
                           \n               O         ||\
                           \n               |         ||\
                           \n               |         ||\
                           \n                         ||\
                           \n                        /||\ \
                           \n                    ============",
                          "               ____________\
                           \n               |         ||\
                           \n               |         ||\
                           \n               |         ||\
                           \n               O         ||\
                           \n              /|         ||\
                           \n               |         ||\
                           \n                         ||\
                           \n                        /||\ \
                           \n                    ============",
                          "               ____________\
                           \n               |         ||\
                           \n               |         ||\
                           \n               |         ||\
                           \n               O         ||\
                           \n              /|\        ||\
                           \n               |         ||\
                           \n                         ||\
                           \n                        /||\ \
                           \n                    ============",
                          "               ____________\
                           \n               |         ||\
                           \n               |         ||\
                           \n               |         ||\
                           \n               O         ||\
                           \n              /|\        ||\
                           \n               |         ||\
                           \n              /          ||\
                           \n                        /||\ \
                           \n                    ============",
                          "               ____________\
                           \n               |         ||\
                           \n               |         ||\
                           \n               |         ||\
                           \n               O         ||\
                           \n              /|\        ||\
                           \n               |         ||\
                           \n              / \        ||\
                           \n                        /||\ \
                           \n                    ============"]

# print('\n'.join('{:^0}'.format(s) for s in hanging_visual_process[0].split('\n')))


def return_random_word(file_name):  # returns a random word from the given .txt file
    global random_word
    with open(file_name, 'r') as f:
        list_of_lines = f.readlines()
        for l in range(len(list_of_lines)):
            list_of_lines[l] = (list_of_lines[l]).strip('\n')  # to ignore all the \n
            random_word = random.choice(list_of_lines)
        return random_word


def blank_lines():
    char_count = len(random_word)
    secret_word = (" _ " * char_count)
    print(secret_word)
    return secret_word


def game():
    hanging_process = 0
    while hanging_process < 6:
        inp_lett = input("\nEnter a letter: ")                      # do it until you 'die'
        if inp_lett.isalpha() and len(inp_lett) == 1:                   # if input is correct
            if inp_lett in random_word:                                     # if success
                print ("\nYou lucky bastard\n")
                for i in range(len(random_word)):
                    if inp_lett == random_word:
                        print("mkay")

            else:                                                           # if unsuccess
                hanging_process += 1
                print("\nShit happens mate...\n")
                print(blank_lines())
                print (hanging_visual_process[hanging_process])  # print the next stage of hanging

        else:                                                           # invalid input handling
            if not inp_lett.isalpha():                                      # for not letter
                print("\n%s is not a letter dumbass.\n" % inp_lett)

            elif len(inp_lett) > 1:                                         # for more than 1 letter
                print("\nJust ONE letter...bruhh...\n")
    end_game()


def end_game():
    choice = input("This is the end, mate...new game? (y/n): ")
    if choice == "y":
        welcome()
        return_random_word('hangman_word.txt')
        blank_lines()
        game()
    elif choice == "n":
        sys.exit()
    else:
        print("That wasn't an option...do you even read bro?")
        end_game()


welcome()
return_random_word('hangman_word.txt')
blank_lines()
game()
