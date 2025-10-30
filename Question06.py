#Y ou are given a character string A. Y ou to trim trailing asterisk characters('*') in the string and print the resultant string.

A = "**h*e*l*lo*"

i = len(A) - 1
while i >= 0 and A[i] == '*':
    i -= 1
result = A[:i+1]

print(result)
