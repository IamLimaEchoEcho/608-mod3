#Lee Jones
#roll a 6 sided die 10 times
import random
import statistics
import math

#set up roll_list
roll_list = []

# 10 die rolls
for roll in range(10): 
    face = random.randrange(1, 7)
    roll_list.append(face)

#hardcode roll_list
#roll_list = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

print("Rolling the dice 10 times")
print (f'Dice rolls: {roll_list}')
print (f'pvariance: {statistics.pvariance(roll_list)}')
print (f'pstdev: {statistics.pstdev(roll_list)}')
print (f'math.sqrt of pvariance: {math.sqrt(statistics.pvariance(roll_list))}')

print("Lee Jones")