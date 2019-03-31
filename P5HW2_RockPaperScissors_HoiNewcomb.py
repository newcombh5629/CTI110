# write a program game for user to Rock, Paper, Scissors against the computer. 
# 3/31/2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Hoi Newcomb

def main():
    # allow to use random module
    import random
    # the game moves guideline
    print('Rock = r, , Paper = p, Scissors = s')
    # winning rules
    message1 = "rock smashes scissors"
    message2 = "scissors cuts paper"
    message3 = "paper wraps rock"

    # get user make a choice
    user_move = input("Enter choice of rock(r), paper(p) or scissors(s): ")
    
    # get computer generate random number and make a choice
    comp_num = random.randint(1,3)
    if comp_num == 1:
        comp_move = "r"
    elif comp_num == 2:
        comp_move = "p"
    else:
         comp_move = "s"
    print("Computer choice of move is: ", comp_move)

    # display the winning results
    if user_move == "r" and comp_move == "s":
         print('User wins,', message1)
    elif comp_move == "r" and user_move == "s":
         print('Computer wins,', message1)
    elif user_move == "s" and comp_move == "p":
         print('User wins,', message2)
    elif comp_move == "s" and user_move == "p":
         print('Computer wins,', message2)
    elif user_move == "p" and comp_move == "r":
         print('User wins,', message3)
    elif comp_move == "p" and user_move == "r":
         print('Computer wins,', message3)
         
    elif user_move == comp_move:
         print("Same move, play again!")

    # set play again loop
    play_again = 'true'
    while play_again == 'true':
        if user_move == comp_move:
           main()
           
# call the funciton
main()
  
