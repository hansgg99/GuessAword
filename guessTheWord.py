from random_words import RandomWords 
# The Libary I used to choose words from

name = input("What is your name? ")
#asks user for his name


print("Good Luck", name, "! You have 12 attemps to guess the word")


words = RandomWords()
word = words.random_word()
# Func that choose random word

print("Guess The Characters ")

guesses = ' '

turns = 12
#number of turns

while turns > 0:
    #count the failed attempts 
    failed_attemps = 0

    #declaring for loop in order to check user's input one at a time
    for i in word:
        
        #check if user's char is in guesses(word)
        if i in guesses:
            print(i)

        #for every failure fails increases by one    
        else:
            print(" _ ")
            failed_attemps+=1

    # Check when/if player wins and stop current round
    if failed_attemps == 0:
        print(name, " You Won!")
        print("The word is: ", word)
        break


    guess = input("Guess the next character: ")
    
    #placeholder for user guess will be stored in guesses
    guesses += guess

    #check if user input char is in that word
    if guess not in word:
        
        turns -= 1
        # If the char wont match, let the user know he's wrong
        # and how many tries he's left
        if turns in range(5,13):

            print("Wrong Guess")
            print("You have ", turns, " turns left")
        if turns in range(1,4):
            print("Wrong Guess")
            print("Be Careful You Have ", turns, "turns left")

        #check if user is out of turns and let him know he sucked :)
        if turns == 0:
            print("You Suck. The Word was: ", word)




