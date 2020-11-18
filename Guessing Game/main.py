secret_word = "Light"
users_word = ""
count = 0


while users_word != secret_word:
        users_word = input("Guess the secret word: ")

        if count == 2 or users_word == "Quit" or users_word == "quit" :
            print("Bye for now")
            break

        if users_word == secret_word:
            print("Congratulations you are right 🎉")
    
        else:
            count += 1
            print("Try again and you have " + str(3 - count) + " guesses left" )