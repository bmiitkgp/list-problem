# Take input and sum of the elements using try and except

st = input()
s = 0
for i in st:
    print(i)
    try:
        s = s + int(i)
        print(s)
    except:
        print(s)
print('Sum = ', s)
        
