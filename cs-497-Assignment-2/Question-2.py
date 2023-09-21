#Question 2
#Kth Largest element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Not that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

import heapq

nums = [3, 2, 1, 5, 6, 4]
k = 2

minHeap = []
for i in nums:
    heapq.heappush(minHeap, i)
    if len(minHeap) > k:
        heapq.heappop(minHeap)
print(minHeap[0])
