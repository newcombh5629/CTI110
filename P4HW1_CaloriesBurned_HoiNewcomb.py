# Create a program that calculates the amount of calories burned when running on a treadmil.
# 3/19/2019
# CTI-110 P4HW1 - Calories Burned
# Hoi Newcomb
# Pseudocode 
#1. get calories burned per minute
#2. calculate calories_burned = time * calories_per_min
#3. times in minutes
#4. display calories burned after 20,35,45 mins


calories_per_min = 5

for time in [20, 35, 45]:
    calories_burned = time * 5   
    print('You will burn', calories_burned, 'calores in', time, 'minutes')
