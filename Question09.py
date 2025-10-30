#Write a program to reverse the words present in a string. Check example input/output.

A = input()
words = A.split()
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
result = ' '.join(reversed_words)
print(result)
