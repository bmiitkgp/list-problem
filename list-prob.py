# Remove common numbers from multiple lists

l1 = [1,2,3,4]
l2 = [1,2,8,7]

# Solution 1

l = l1+l2
l3 = []
for i in l:
    if l.count(i)==1:
        l3.append(i)
print(l3)

# Solution 2

l = l1+l2
l3 = []
[l3.append(v) if l.count(v)==1 else "" for v in l]
print(l3)



