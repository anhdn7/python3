a = [1,2,3,1,4,8,5]
l = [1]*len(a)
print(l)
for i, b in enumerate(a, 1):
    for j, c in enumerate(a[:i]):
        if b > c:
            l[i-1] = max(l[i-1], l[j] + 1)
print(max(l))
