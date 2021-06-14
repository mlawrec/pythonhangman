import time
import random

file1 = open('catflowers.txt', 'r')
content_list1 = file1.readlines()
file2 = open('catmovies.txt', 'r')
content_list2 = file2.readlines()
file3 = open('catsuperheroes.txt', 'r')
content_list3 = file3.readlines()

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_again
    global score
    category = input("Choose category: \n F - flowers.txt, \n M - movies.txt, \n S - superheroes.txt, \n X - exit")
    secret_word = random.choice(category)
    playGame = True
    continueGame = "Y"
    while True:
        if category.upper() == 'F':
            secret_word = random.choice(open('catflowers.txt', 'r'))
            break
        elif category.upper() == 'M':
            secret_word = random.choice(open('catmovies.txt', 'r'))
            break
        elif category.upper() == 'S':
            secret_word = random.choice(open('catsuperheroes.txt', 'r'))
            break
        else:
            if category.upper() == 'X':
                print("Bye. See you next time!")
                playGame = False
                break
            if playGame:
                secret_word = category
                word = random.choice(secret_word)
                length = len(word)
                count = 0
                display = '_' * length
                already_guessed = []
                play_again = ""



def again_play():
    global score
    play_again = input("Do You want to play again? 1 = yes, 2 = no \n")
    while play_again not in ["1", "2"]:
        play_again = input("Do You want to play again? 1 = yes, 2 = no \n")
    if play_again == "1":
        main()
        hangman()
    elif play_again == "2":
        score()
        time.sleep(2)
        exit()


def hangman():
    global already_guessed
    global count
    games_lost = 0
    games_won = 0
    category = input()
    secret_word = (category)
    word = random.choice(secret_word)
    length = len(word)
    display = '_' * length
    limit = 5
    guess = input("The word is: " + display + " Enter your guess: \n").lower()
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Enter only one letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("You have already guessed this letter. Try another letter\n")

    else:
        count += 1

        if count == 1:
            print("Wrong choice. " + str(limit - count) + " guess remaining\n")
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif count == 2:
            print("Wrong choice. " + str(limit - count) + " guess remaining\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif count == 3:
            print("Wrong choice. \n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 4:
            print("Wrong choice.\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |       \n"
                  "__|__\n")
        elif count == 5:
            print("Wrong choice. You are hanged\n")
            games_lost += 1
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            again_play()

    if word == '*' * length:
        print("Congrats! You have guessed it successfully...")
        games_won += 1
        again_play()

    elif count != limit:
        hangman()
        main()

        def score():
            print(" ")
            print("  Score")
            print("  -----")
            print("  Won: " + str(games_won) + "    Lost: " + str(games_lost))

        hangman()
        main()
        def scoreboard():
         scoreboard = open('scoreboard.txt', 'a')
         scoreboard.write(name + str(games_won))
         scoreboard.close()

        hangman()

name = input("What is your name?: ")
print("Welcome to hangman " + name + "! Good luck!")
time.sleep(1)
print("You can choose each letter more than once. Good luck!")
time.sleep(2)
print("The game begins now...\n")
time.sleep(2)

main()

