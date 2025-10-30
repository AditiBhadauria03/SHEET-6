#Write a program to input T strings (S) from user and print 1 if it is palindrome otherwise print 0.

T = int(input())

for i in range(T):
    S = input().strip()
    
    if S == S[::-1]:
        print(1)
    else:
        print(0)

