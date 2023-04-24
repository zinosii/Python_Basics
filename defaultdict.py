from collections import defaultdict

numbers=[1,4,5,1,3,10,8,4,1,1]
numbers_defaultdict=defaultdict(int)

for i in numbers:
    numbers_defaultdict[i]+=1

print(numbers_defaultdict)
