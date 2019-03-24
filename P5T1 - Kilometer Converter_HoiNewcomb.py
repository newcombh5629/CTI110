# Write a program convert Kilometers in Miles.
# 3/21/2019
# CTI-110 P5T1_KilometerConverter
# Hoi Newcomb
# 

conversion_factor = 0.6214

# Get the distance for Kilometers
def main():
    kilometers = float(input('Enter the distance in kilometers: '))
    #convert distance to miles
    show_miles(kilometers)
    
def show_miles(km):
    # calculate
    miles = km * conversion_factor
    # display answer in miles
    print(km, 'Kilometers equals', format(miles, ',.4f'), 'Miles.')   

# Call the main function      
main()





    
