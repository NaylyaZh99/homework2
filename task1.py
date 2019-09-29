S = input()
L = len(S)
for i in range(1, L + 1):
    if L % i == 0:
        if S[:i] * (L // i) == S:
            print(L // i)
            break


