# Question 4
# Remove duplicate letters

# Given a string s, remove duplicate letters 
# so that every letter appears once and only once.
# You must make sure your result is the smallest 
# lexicographical order among all possible results

s = "bcabc"

stack = []
lookup = {}
duplicate = set()

for i in range(len(s)):
    lookup[s[i]] = i

for i in range(len(s)):
    if s[i] in duplicate: continue
    while stack and s[i] < stack[-1] and lookup[stack[-1]] > i:
        duplicate.remove(stack.pop())
    stack.append(s[i])
    duplicate.add(s[i])
print("".join(stack))