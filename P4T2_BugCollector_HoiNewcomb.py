# Write a program that keeps a running total number of bugs collected during the five days.
# 3/19/2019
# CTI-110 P4T2 Bug Collector
# Hoi Newcomb
# Pseduecode
#1. get the accumllator
#2. get the bugs collect for each day
#3. display the total bugs


total = 0
for day in range(1, 6):
    print('Enter the bugs collected on day', day)
   # input the number of bugs 
    bugs = int(input())
    total += bugs
print ('You collected a total of', total, 'bugs.')
    

