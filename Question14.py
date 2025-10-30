#Y ou are given a character string A, having length N and an integer ASCII code B. Y ou have to tell the leftmost occurrence of the character having ASCII code equal to B, in A or report that it does not exist.

A = input() 
B = int(input())  

ch = chr(B)
pos = -1

for i in range(len(A)):
    if A[i] == ch:
        pos = i + 1  
        break
if pos != -1:
    print(pos)
else:
    print("Character not found")
