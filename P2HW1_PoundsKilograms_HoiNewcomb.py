# Write a program that converts pounds to Kilograms.
# 2/12/2019
# CTI-110 P2HW1- Pounds to Kilogramms Converter
# Hoi Newcomb
# Pseudocode
#1. Get Pound as x
#2. use formule to convert to Kilo
#3. display the answer in kilo


pound = float(input('Enter pounds to convert into Kg: '))
converter = pound / 2.2046
print('The Kg is:', format(converter, '.2f'))
