# Design a program to display the secondary color from mixing 2 out of 3 primary color
# P3HW1 - Color Mixer
# Hoi Newcomb
# 2/25/2019
# Psuedocode
#1. Get the primary color 1
#2. Get the primary color 2
#3. Mix the primary color red & blue, red & yellow, blue & yellow and display the secondary color 
#4. Display error message if primary color is not red, blue or yellow

primary_color1 = input('Enter primary color1: ')
primary_color2 = input('Enter primary color2: ')

if primary_color1 == 'red' and primary_color2 == 'blue':
    print('When you mix red and blue, you get purple.')
elif primary_color1 == 'blue' and primary_color2 == 'red':
    print('When you mix red and blue, you get purple.')
elif primary_color1 == 'red' and primary_color2 == 'yellow':
    print('When you mix red and yellow, you get orange.')
elif primary_color1 == 'yellow' and primary_color2 == 'red':
    print('When you mix red and yellow, you get orange.')
elif primary_color1 == 'blue' and primary_color2 == 'yellow':
    print('When you mix blue and yellow, you get green.')
elif primary_color1 == 'yellow' and primary_color2 == 'blue':
    print('When you mix blue and yellow, you get green.')
else:
    print('Error')










