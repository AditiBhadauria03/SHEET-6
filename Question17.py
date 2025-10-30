# Akash likes playing with strings. One day he thought of applying following operations on the
# string in the given order:
# Concatenate the string with itself.
# Delete all the uppercase letters.
# Replace each vowel with '#'.
# Y ou are given a string A of size N consisting of lowercase and uppercase alphabets. Return the
# resultant string after applying the above operations.

A=input("Enter a string:")
A=A+A
B=" "
for ch in A:
    if not ch.isupper():
        B=B+ch
result=" "
for ch in B:
    if ch in "aeiou":
        result+="#"
    else:
        result+=ch
print(result)