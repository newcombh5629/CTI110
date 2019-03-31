# Write a program generates a random number range 1 to 100 and ask user to guess a number.
# 3/30/2019
# CTI-110 P5HW1 - Random Number
# Hoi Newcomb

def main():
      
      # allow to use import module
      import random

      # generate a random number
      computer_num = random.randint(1, 100)

      # variable to count the user's number of guesses
      count_guesses = 0

      # set to control the guessing loop
      keep_guessing = 'true'
      
      while keep_guessing == 'true':
          # get user guess a number
          guess_num = int(input("Guess a number: "))
          # counting the guesses
          count_guesses += 1
          # loop stop if user guess the random number 
          if guess_num == computer_num:
              print("Congratulations!")
              print("The number of guesses:", count_guesses)
              keep_guessing = 'false'
          else:
              # tell the user whether the guess number higher or lower  
              if guess_num < computer_num:
                  print("Too low: try again!")
              elif guess_num > computer_num:
                  print("Too high: try again!")

      # game restart            
      if keep_guessing == 'false':
            print('Guessing game start over.')
            main()


# calling function
main()
            



           





            

      
         


