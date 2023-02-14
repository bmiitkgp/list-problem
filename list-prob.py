# Remove common numbers from multiple lists

l1 = [1,1,2,3,4]
l2 = [2,8,7]

# Solution 1

l = l1+l2

l3 = []
for i in l:
    print('i = ', i)
    print('l count: ',l.count(i))
    if l.count(i)==1:
        print('before append', l3)
        l3.append(i)
        print('After append', l3)
print(l3)





