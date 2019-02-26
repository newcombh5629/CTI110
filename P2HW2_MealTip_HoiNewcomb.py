# Creat a program that calculates the amount of the tip percentages.
# 2/12/2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Hoi Newcomb
# Pseudocode
# 1. Give the meal charge 
# 2. tip 15% = meal charge times 0.15
# 3. tip 18% = meal charge times 0.18
# 4. tip 20% = meal charge times 0.20
# 5. display the different tips amount

meal_charge = float(input('Enter the total cost of meal $: '))
t15 = meal_charge * 0.15
t18 = meal_charge * 0.18
t20 = meal_charge * 0.20
print('Tip 15% is $: ', format(t15, '.2f'))
print('Tip 18% is $: ', format(t18, '.2f'))
print('Tip 20% is $: ', format(t20, '.2f'))
