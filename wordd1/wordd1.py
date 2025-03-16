import random

words = ["Looma", "Ratas", "Käige", "Sõber", "Laine", "Pagar", "Roosa", "Tunne", "Kalur", "Hinge"]
randomword = random.choice(words)
length = len(randomword)
print('''
         RULES!
You have to guess the word.
You must enter letters from the alphabet.
You have 6 tries!
''')
print(f"The word has {length} letters. Try to guess it!")
attempts = 6  
while attempts > 0:
    try:
        user = input("Your guess: ")

        if len(user) > length:
            print("Your word is too long!")
        elif len(user) < length:
            print("Your word is too short!")
        elif user.isalpha() == False:
            print("Please enter only letters!")
        elif user == randomword:
            print("Congratulations! You guessed the word!")
            break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        if attempts == 0:
            print(f"Game over! The word was: {randomword}")

    except ValueError:
        print("Error")
