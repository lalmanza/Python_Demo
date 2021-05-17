import random

comp_choice = random.choice(['scissors', 'rock', 'paper'])
user = input('Do you want - rock, paper, or scissors? \n')
if comp_choice == user:
    print('TIE')
elif user == 'rock' and comp_choice == 'scissors':
    print ("WIN")
elif user == 'paper' and comp_choice == 'rock':
    print ("WIN") 
elif user == 'scissors' and comp_choice == 'paper':
    print ("WIN")
else:
    print ('You lose :( Computer WINS :D')