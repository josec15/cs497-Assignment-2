# Question 3
# Maximum Gap

# Given an integer array nums, return the maximum difference 
# between two successive elements in its sorted form.
# If the array contains less than two elements, return 0.
# You must write an algorithm that runs in linear time 
# and uses linear extra space.

nums = [3, 6, 9, 1]

maxGap = 0
nums.sort()
for i in range(len(nums)-1):
    maxGap = max(maxGap, (nums[i+1])-nums[i])
print(maxGap)