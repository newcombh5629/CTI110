# Write a program with a loop that user enter a series of number and dispaly thesum. End the serier with a negative number.
# 3/19/2019
# CT1-110 P4HW3 - Sum of Numbers
# Hoi Newcomb
# Pseudocode
#1. get a series from the user
#2. get an accumulator variable
#3. end the series of number by enter a negative number
#4. add the series of number
#5. display the sum of the series of positive numbers


num = float(input('Enter a number: '))
total = 0

while num > -1:
    total = total + num
    num = float(input('Enter another number or negative number to quit: '))

print('The sum of all positive numbers are:', total)
    
