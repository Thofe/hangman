#Blake Mitrick
#Hangman project 10/20/2016

import os
import random

def show_start_screen():
    print("""
                                                      
  /\  /\  __ _  _ __    __ _  _ __ ___    __ _  _ __  
 / /_/ / / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \ 
/ __  / | (_| || | | || (_| || | | | | || (_| || | | |
\/ /_/   \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_|
                       |___/
                       """)                                                                

def show_credits():
    print("""
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\                /::\    \        
       /::::\    \              /::::\    \              /::::|   |               /::::\    \       
      /::::::\    \            /::::::\    \            /:::::|   |              /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /::::\   \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \  
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \  /:::/\:::\   \:::\    \ 
/:::/____/  ___\:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\/:::/__\:::\   \:::\____\

\:::\    \ /\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /
 \:::\    /::\ \::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    /  \:::\   \:::\   \/____/ 
  \:::\   \:::\ \/____/            \::::::/    /               /:::/    /    \:::\   \:::\    \     
   \:::\   \:::\____\               \::::/    /               /:::/    /      \:::\   \:::\____\    
    \:::\  /:::/    /               /:::/    /               /:::/    /        \:::\   \::/    /    
     \:::\/:::/    /               /:::/    /               /:::/    /          \:::\   \/____/     
      \::::::/    /               /:::/    /               /:::/    /            \:::\    \         
       \::::/    /               /:::/    /               /:::/    /              \:::\____\        
        \::/____/                \::/    /                \::/    /                \::/    /        
                                  \/____/                  \/____/                  \/____/         
                                                                                                    
""")                                                                                                                                                                                                        
    print("""
         _______                   _____                    _____                    _____          
        /::\    \                 /\    \                  /\    \                  /\    \         
       /::::\    \               /::\____\                /::\    \                /::\    \        
      /::::::\    \             /:::/    /               /::::\    \              /::::\    \       
     /::::::::\    \           /:::/    /               /::::::\    \            /::::::\    \      
    /:::/~~\:::\    \         /:::/    /               /:::/\:::\    \          /:::/\:::\    \     
   /:::/    \:::\    \       /:::/____/               /:::/__\:::\    \        /:::/__\:::\    \    
  /:::/    / \:::\    \      |::|    |               /::::\   \:::\    \      /::::\   \:::\    \   
 /:::/____/   \:::\____\     |::|    |     _____    /::::::\   \:::\    \    /::::::\   \:::\    \  
|:::|    |     |:::|    |    |::|    |    /\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
|:::|____|     |:::|    |    |::|    |   /::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |
 \:::\    \   /:::/    /     |::|    |  /:::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|
  \:::\    \ /:::/    /      |::|    | /:::/    /  \:::\   \:::\   \/____/  \/____|:::::\/:::/    / 
   \:::\    /:::/    /       |::|____|/:::/    /    \:::\   \:::\    \            |:::::::::/    /  
    \:::\__/:::/    /        |:::::::::::/    /      \:::\   \:::\____\           |::|\::::/    /   
     \::::::::/    /         \::::::::::/____/        \:::\   \::/    /           |::| \::/____/    
      \::::::/    /           ~~~~~~~~~~               \:::\   \/____/            |::|  ~|          
       \::::/    /                                      \:::\    \                |::|   |          
        \::/____/                                        \:::\____\               \::|   |          
         ~~                                               \::/    /                \:|   |          
                                                           \/____/                  \|___|          
                                                                                                      
""")


def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        full_path = path + "/" + f 
        with open(full_path, 'r') as file:
            print(str(i + 1) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice) - 1 

    return path + "/" + files[choice]

def get_puzzle(file):
    #words = ["patriots", "soccer", "french fries", "larry the lobster"]

    with open(file, 'r') as f:
        words = f.read().splitlines()
        
    return random.choice(words[1:])

def check(word, solved, guesses):
    for i in range(len(word)):
        if word[i].lower() in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() == True and len(guess)==1:
            return guess.lower()
        else:
            print("Please input a single letter")

def display_board(solved, strikes, wrong_guesses):

    if strikes == 0:
        print("""
____________.._______
| .__________||______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||    
| |          ||    
| |          ||   
| |         
| |     
| |     
| |         
| |          
| |          
| |          
| |           
| |           

         """)
    elif strikes == 1:
        print("""
____________.._______
| .__________||______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||    
| |          ||    
| |          ||   
| |         .-`---.
| |         |     |
| |          |   | 
| |          |   |
| |          |___|   
| |          
| |          
| |           
| |           

         """)
    elif strikes == 2:
         print("""
____________.._______
| .__________||______|
| | / /      ||
| |/ /       ||
| | /        ||.---.
| |/         |/     |
| |          |      |
| |          |\    /
| |         .-`---.
| |         |     |
| |          |   | 
| |          |   |
| |          |___|   
| |          
| |          
| |           
| |           

         """)
    elif strikes == 3:
        print("""
____________.._______
| .__________||______|
| | / /      ||
| |/ /       ||
| | /        ||.---.
| |/         |/     |
| |          |      |
| |          |\    /
| |         .-`---.
| |        //     |
| |       // |   | 
| |      //  |   |
| |          |___|   
| |          
| |          
| |           
| |           

         """)
    elif strikes == 4:
        print("""
____________.._______
| .__________||______|
| | / /      ||
| |/ /       ||
| | /        ||.---.
| |/         |/     |
| |          |      |
| |          |\    /
| |         .-`---.
| |        //     \\
| |       // |   | \\
| |      //  |   |  \\
| |          |___|   
| |          
| |          
| |           
| |           

         """)
    elif strikes == 5:
        print("""
____________.._______
| .__________||______|
| | / /      ||
| |/ /       ||
| | /        ||.---.
| |/         |/     |
| |          |      |
| |          |\    /
| |         .-`---.
| |        //     \\
| |       // |   | \\
| |      //  |   |  \\
| |          | __|   
| |          || 
| |          ||
| |          || 
| |          || 

         """)
    elif strikes == 6:
        print("""
____________.._______
| .__________||______|
| | / /      ||
| |/ /       ||
| | /        ||.---.
| |/         |/     |
| |          |      |
| |          |\    /
| |         .-`---.
| |        //     \\
| |       // |   | \\
| |      //  |   |  \\
| |          |   |   
| |          || ||
| |          || ||
| |          || ||
| |          || ||

         """)
              

    

    
    print(solved + "[Guesses:" + str(wrong_guesses) + "]" )

def play_again():
    while True:
        answer = input("Would you like to play again?")
        
        if answer.lower() == 'no' or answer.lower() == 'n':
            return False
        elif answer.lower() == 'yes' or answer.lower() == 'y':
            return True

        print("What are u dum?!?!?!?!?!? " + answer +" is neither yes nor no")

def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)

    guesses = ""
    wrong_guesses = ""
    strikes = 0
    limit = 6
    
    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word.lower():
            strikes += 1
            wrong_guesses += letter
            
        guesses += letter
        
        
        solved = check(word, solved, guesses)
        display_board(solved, strikes, wrong_guesses)

    if word == solved:
        print("You win!")
    else:
        print("You are dumb. The correct answer was " + word + ".")


def main():
    show_start_screen()

    playing = True

    while playing:
        play()
        playing = play_again()


    show_credits()


# code execution begins here
if __name__ == "__main__":
    main()
