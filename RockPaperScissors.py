import random
user_input = ""

while user_input not in ('n', 'no'):
    user_input= input("Hello! Would you like to play rock paper scissors with me?")
    user_input = user_input.lower()

    if user_input in ('y','yes'):
        print("Excellent! Best 2 out of 3 wins!")
    elif user_input in ('n', 'no'):
        print("Boo. Okay. Have a nice day poopy pants.")
    else:
        print("That's not a yes or no sir.")

          