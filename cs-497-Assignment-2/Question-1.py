# Question 1
# Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than [n / 2] times.
# You may assume that the majority element always exists in the array.
# Solve this problem in Linear time: O(n).

nums = [3, 2, 3]

majority = 0
count = 0

for i in nums:
    if majority == i:
        count += 1
    elif count == 0:
        majority = i
        count = 1
    else:
        count -= 1
print(majority)


