#Y ou are given string (A) and you have to print the reverse order of words.

A = input() 
words = A.split()
reversed_words = words[::-1]
result = ' '.join(reversed_words)
print(result)
