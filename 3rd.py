'''
Write a function, getX, that given an integer x and a list nums returns the Xth number
if the list was in sorted order. In other words, the Xth smallest number.
Input: An integer, x, and an unsorted list of integers nums that aren’t necessarily distinct.
Output: The integer corresponding to the Xth number in the sorted list.
Note that this assumes the first number is position 1, not 0.
If the input x is greater than the length of the list, or nums is empty, return 0.
'''

def getX(x, nums):

  sorted_nums = sorted(nums)
  if x > len(nums) or len(nums) == 0:
    return 0
  else:
    return sorted_nums[x-1]

print(getX(2, [6, 3, -1, 5]))
