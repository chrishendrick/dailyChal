# 09/13/18
#
#Good morning! Here's your coding interview problem for today.
#
#This problem was recently asked by Google.
#
#Given a list of numbers and a number k, return whether any two numbers from
#the list add up to k.
#
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
#Bonus: Can you do this in one pass?

import random

num1 = int(random.randint(1,20))
num2 = int(random.randint(1,20))
num3 = int(random.randint(1,20))
num4 = int(random.randint(1,20))
num5 = int(random.randint(1,20))

nums = [num1,num2,num3,num4,num5]
sums = [(nums[0]+nums[1]),(nums[0]+nums[2]),(nums[0]+nums[3]),(nums[0]+nums[4]),(nums[1]+nums[2]),(nums[1]+nums[3]),(nums[1]+nums[4]),(nums[2]+nums[3]),(nums[2]+nums[4]),(nums[3]+nums[4])]

print("Guess a number to see if it's a sum of any two numbers from the list below.")
print("Here are the 5 numbers:")
for x in nums:
    print(x)

#print("Here are the sums:")
#for x in sums:
#    print(x)

guess = input("Give me a number between 1 and 40: ").strip()
guess = int(guess)

for x in sums:
    if guess == x:
        outcome = True
        break
    else:
        outcome = False

print(outcome)


           
