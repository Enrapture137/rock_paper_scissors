import random

player_score = 0
computer_score = 0
game_count = 0

while game_count < 3:
    bank = ['rock','paper','scissors']
    computer_choice = random.choice(bank)
    player_choice = input("Rock, Paper, Scissors, S H O O T! " )
    player_choice.lower()
    game_count += 1
    
    if player_choice == computer_choice:
        game_count -= 1
        print("The computer chose " + computer_choice + "! It's a T I E! The score is still {} to {}".format(player_score, computer_score))
    elif player_choice == "rock":
        if computer_choice == "paper":
            computer_score += 1
            print("The computer chose " + computer_choice + "! They win! The score is now {} to {}".format(player_score, computer_score))
        else:
            player_score += 1
            print("The computer chose " + computer_choice + "! They lose! The score is now {} to {}".format(player_score, computer_score))
    elif player_choice == "paper":
        if computer_choice == "scissors":
            computer_score += 1
            print("The computer chose " + computer_choice + "! They win! The score is now {} to {}".format(player_score, computer_score))
        else:
            player_score += 1
            print("The computer chose " + computer_choice + "! They lose! The score is now {} to {}".format(player_score, computer_score))   
    elif player_choice == "scissors":
        if computer_choice == "rock":
            computer_score += 1
            print("The computer chose " + computer_choice + "! They win! The score is now {} to {}".format(player_score, computer_score))
        else:
            player_score += 1
            print("The computer chose " + computer_choice + "! They lose! The score is now {} to {}".format(player_score, computer_score))           
    else:
        print("That's not a rock, paper, OR scissors. TF.")

    
if player_score > computer_score:
    print("you are the winner! good job!")
else:
    print("The computer won. Sorry loser. ")