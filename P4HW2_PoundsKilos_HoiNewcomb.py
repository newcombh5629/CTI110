# Create a program that displays a table of pounds and their equivalent kilograms.
# 3/19/2019
# CT1-110 P4HW2 - Pounds to Kilos Table
# Hoi Newcomb
# Pseudocode
#1. get beginning weight
#2. get end weight
#3. value of 10 as increment
#4. conversion formula
#5. Table heading
#5. display pounds too Kilos

beginning_weight = 100
end_weight = 301
increment = 10
conversion_factor = 2.2046

print('Pound\tKilograms')
print('-----------------')
for pound in range(beginning_weight, end_weight, increment):
    kilograms = pound / conversion_factor
    print(pound, '\t', format(kilograms, '.2f'))


