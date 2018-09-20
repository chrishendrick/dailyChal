# dailycodingproblem.com 9/16/18
#
#Good morning! Here's your coding interview problem for today.

#This problem was asked by Stripe.

#Given an array of integers, find the first missing positive integer in
#linear time and constant space. In other words, find the lowest positive
#integer that does not exist in the array. The array can contain duplicates
#and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
#should give 3.

#You can modify the input array in-place.

import random

num1 = int(random.randint(-5,5))
num2 = int(random.randint(-5,5))
num3 = int(random.randint(-5,5))
num4 = int(random.randint(-5,5))
num5 = int(random.randint(-5,5))

nums = [num1,num2,num3,num4,num5]

print("Here is the list of numbers:")
for x in nums:
    print(x)

nums.sort()
print("Now sorted:")
for x in nums:
    print(x)

# I think this is some elegant stuff

min = 1

for x in nums:
    if x < min:
        continue
    elif x == min:
        min = min+1
        continue
    else:
        break

print("The lowest missing positive integer is " + str(min))
