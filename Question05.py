#You are given a character string A. Y ou to trim leading asterisk characters('*') in the string and print the resultant string.

A = input().strip() 
result = A.lstrip('*')
print(result)
