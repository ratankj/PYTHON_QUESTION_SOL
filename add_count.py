"""
Convert a pair of values into a sorted unique array

Original List:  [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
Sorted Unique Data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""




num=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
print(num)
new_l= []
for i in num:
    #print(i)
    for j in i:
        if j not in new_l:
            new_l=new_l+[j]
print(new_l)































numbers = list(range(1, 21))
groups = []

for i in range(0, len(numbers), 5):
    #print(i)
    group = numbers[i:i+5]
    groups.append(group)


#print(groups)








