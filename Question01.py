#Write a program to input T strings (S) from user and print count of vowels and consonants in it.

T = int(input())

for i in range(T):
    S = input().strip()  
    
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for ch in S:
        if ch.isalpha(): 
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    print(v_count, c_count)
