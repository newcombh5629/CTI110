# Write a program that asks for the length and width og two rectangles.
# 2/25/2019
# CTI-110 P3T1 - Area of Rectangles
# Hoi Newcomb
# Pseudocode -
#1. Input the length and width of rectangle 1
#2. Input the length and width of rectangle 2
#3. Calculate the area of rectangle 1
#4. Calculate the area of rectangle 2
#5. Dispay the answer

length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))
area1 = length1 * width1
area2 = length2 * width2
if area1 > area2:
    print('Recttangle 1 has the greater area.')
else:
    if area2 > area1:
        print('Rectangle 2 has the greater area.')
    else:
        print('Both have the same area.')
            
