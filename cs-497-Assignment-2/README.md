# cs497-Assignment-2

## Question 1
For this problem, I used a for loop that would loop through the nums list  
The first if statement would check if the element in the list matches the  
majority element. If not, then we would move on to the next if statement  
which checks if the count is equal to zero. If the count is equal to zero then  
we would set the majority element as the i element and the count to zero.  
Since the if statement is executed we would repeat the for loop to check if the next  
element of the list matches the majority element. If so, increment count.  
If the ith element in the list does not match the majority element, then we  
would reach the third if statement which would decrement count until a new  
majority element is found.
Time Complexity = O(n) since we search the entire nums list once.

## Question 2
In order to solve this, I started with importing heapq to implement a  
minHeap method of finding the kth largest element. I created an empty list  
and used a for loop to search the nums list. I pushed the ith element of  
nums list to minHeap list. If the length of minHeap is greater than k  
then pop the smallest element from the minHeap list with the use of  
heappop function which will always leave minHeap with a single integer.  
After the for loop is completed and every smallest element is popped  
from minHeap, minHeap should be left with the kth largest element.  
Time Complexity = O(n) since we loop through the nums list once.

## Question 3
To begin my solution I created a maxGap variable to store the maximum gap.  
I then used the built-in sort function in python to sort the list.  
After that I used a for loop to iterate through the nums list, subtracting  
by one since we start at the zero index. Then I use the max() function to find the  
largest item of the two parameters, the first parameter being the current maximum  
gap and the second being index + 1 minus index of the list. 
Time Complexity = Linear time.

## Question 4
Create a stack to build the string that removes all duplicate letters.  
Store the index of the previous character in a dictionary called "lookup"  
so that we can compare it to the next index. Create a set list that keeps track  
of all duplicate characters. Create a for loop to store the current index of  
the character to the dictionary, then use another for loop to iterate through the string  
and check if the character in the string is in the duplicate set. If not, then  
while the stack is not empty and the current character is smaller than the last  
index of the stack and has more indexes in the string, remove the last index  
of the stack. Then, append the current character to the stack and add it  
to the set of duplicate letters that can no longer be added to the stack.
Time Complexity = O(n), because each iteration is only as long as the string.

## Question 5



