
import random
import sys

'''player_score = 0
computer_score = 0


print("Lets play rock, paper, scissors, best of 5 wins\n")
while player_score < 3 and computer_score < 3:
    player_choice = input("\nChoose 'r' for rock, 'p' for paper, 's' for scissors\n> ".lower())
    computer_choice =(['rock', 'paper', 'scissors'])
    print("Player Choice:", player_choice)
    print("Computer Choice:", computer_choice)


    if player_choice == 'rock' and computer_choice == 'scissors':
        player_score +=1

    elif computer_choice == 'rock' and player_choice == 'scissors':
        computer_score +=1
    
    elif  player_choice == 'scissors' and computer_choice == 'paper':
        player_score +=1
    
    elif computer_choice == 'scissors' and player_choice == 'paper':
        computer_score +=1

    elif player_choice == 'paper' and computer_choice == 'rock':
        player_score +=1

    elif computer_choice == 'paper' and player_choice == 'rock':
        computer_score +=1

    else:
        print("Tie")


    print("Player Score", player_score)
    print("Computer Score", computer_score)

    if player_score > computer_score:
        print("You win!!")
    else:
        print("You lose!!")'''

def play():    
    user = input("\nWhats your choice?\n 'r' for rock,\n'p' for paper,\n 's' for scissors\n 'e' for exit,\n ")
    computer = random.choice(['r', 'p', 's'])         
    
    if user == 'e':
        print('Thanks for playing')

    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You won!!"

        return "You lost!!"

                
def is_win(player, opponent):
            if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
                return True
            
                  
print(play())             
    

       
     
     