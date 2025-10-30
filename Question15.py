#  Y ou are given two character strings A and B.
# Y ou have to find the first occurrence of string B in string A, as a substring, and return the starting
# position of first occurrence.
# A substring is a contiguous sequence of characters within a string. For e.g "at" is a substring in
# "catalogue".

A = "aabababaa"
B = "ba"

n = len(A)
m = len(B)
position = -1

for i in range(n - m + 1):
    if A[i:i+m] == B:
        position = i
        break

print(position)
