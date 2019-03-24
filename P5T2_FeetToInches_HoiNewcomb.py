# Write a function named feet_to_inches converts feet to inches
# 3/21/2019
# CTI-110 P5T2_FeetToInches
# Hoi Newcomb
# 

# conversion rule
inches_per_foot = 12

# main function
def main():
    feet = int(input('Enter a number for feet: '))
    # conversion
    print(feet, 'equal to', feet_to_inches(feet), 'inches.')

# feet_to_inches function
def feet_to_inches(feet):
    return feet * inches_per_foot

# call the main function
main()
