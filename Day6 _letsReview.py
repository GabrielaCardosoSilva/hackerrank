n = int(input())

for c in range (n):
    even = ""
    odd = ""
    s = input()
    for i in range(0, len(s)):
        if (i % 2 == 0):
            even += s[i]
        else: 
            odd += s[i]
    print(even, odd)
