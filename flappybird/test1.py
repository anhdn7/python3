l0 = [int(x) for x in input().split(',')]
l1 = []
for i in range(l0[0]):
    l2=[]
    for j in range(l0[1]):
        l2.append(i*j)
    l1.append(l2)

print(l1)