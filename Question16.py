#Find the number of occurrences of bob in string A consisting of lowercase English alphabets.

A = "abobc"
B = "bob"
count = 0

for i in range(len(A) - len(B) + 1):
    if A[i:i+len(B)] == B:
        count += 1

print(count)
