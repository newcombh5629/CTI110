# Write a program to enter the projected amount of total sales and displays the profit that will be made.
# 2/12/2019
# CTI-110 P2T1 - Sales Prediction
# Hoi Newcomb
#
project_total_amount = float( input('Enter the projected amount of total sales:'))
profit = project_total_amount * 0.23
print('The profit is $', \
       format(profit, '.2f'))
