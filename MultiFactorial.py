# dailycodingchallenge.com 09/14/18
#Good morning! Here's your coding interview problem for today.
#
#This problem was asked by Uber.
#
print("Given an array of integers, return a new array such that each element")
print("at index i of the new array is the product of all the numbers in the")
print("original array except the one at i.")
print("For example, if our input was [1, 2, 3, 4, 5], the expected output")
print("would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the")
print("expected output would be [2, 3, 6].")
#
#Follow-up: what if you can't use division?

import random

num1 = int(random.randint(1,10))
num2 = int(random.randint(1,10))
num3 = int(random.randint(1,10))
num4 = int(random.randint(1,10))
num5 = int(random.randint(1,10))

nums = [num1,num2,num3,num4,num5]

multi = nums[0]*nums[1]*nums[2]*nums[3]*nums[4]

sums = [(multi/nums[0]),(multi/nums[1]),(multi/nums[2]),(multi/nums[3]),(multi/nums[4])]

print("Here are the 5 numbers:")
for x in nums:
    print(x)

print("Here are the multiplied values:")
for x in sums:
    print(int(x))

