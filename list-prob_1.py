# Solution 2

l = l1+l2
l3 = []
[l3.append(v) if l.count(v)==1 else "" for v in l]
print(l3)
