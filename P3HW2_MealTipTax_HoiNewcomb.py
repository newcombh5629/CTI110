# Create a new program build on P2HW2 Meal tip assignment
# CTI-110
# P3HW2 - Meal Tip Tax
# Hoi Newcomb
# 2/25/2019
# Pseudocode
#1. Give the meal charge
#2. Give the tip percentage 15% or 18% or 20% or error
#3. Calculate the tip, 7% sales tax and total cost
#4. Display all charges (tip, tax and total)
#

meal_charge = float(input('Enter the meal charge $: '))
tips = input('Enter the tip percentage you are consider: ')
if tips == '15' or tips == '18' or tips == '20':
   tip_amt = meal_charge * float(tips) / 100
   tax = meal_charge * 0.07
   total_cost = meal_charge + tax + tip_amt
   print('Tip amount is $: ', format(tip_amt, '.2f'))
   print('Tax is $: ', format(tax, '.2f'))
   print('Total cost is $: ', format(total_cost, '.2f'))
else:
   print('Error!')



