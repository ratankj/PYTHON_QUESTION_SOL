"""
1. largest number of the list
2. smallest number of the list

"""


print("This program will find the largest number from the list ")
len_list = int(input("enter the length of list: "))
num_list = []
for i in range(1,len_list+1):
    enter_num = int(input("enter a number : "))
    num_list.append(enter_num)
print(f"the list list is: {num_list}")

lar_num=num_list[0]

for i in num_list:

    if lar_num < i:
        lar_num = i



print(f"The largest number is : {lar_num}")


print("=========================================    END OF PROGRAM  =============================================")


# 2. smallest number of the list


print("This program will find the Smallest number from the list ")
len_list = int(input("enter the length of list: "))
num_list = []
for i in range(1, len_list + 1):
    enter_num = int(input("enter a number : "))
    num_list.append(enter_num)
print(f"the list list is: {num_list}")

smallest_num = num_list[0]

for i in num_list:

    if smallest_num > i:
        smallest_num = i

print(f"The smallest number is : {smallest_num}")


print("=========================================    END OF PROGRAM  =============================================")

# avg of given list

list_new = [2,4,6,8]
add = 0
count=0
for i in list_new:
    add = add+i
    count = count+1
print(f"add : {add}")
print(f"count : {count}")

avg = add/count
print(f"avg is {avg}")



print("=========================================    END OF PROGRAM  =============================================")


"""

Sum of elements
"""
new_list = []
summation = 0
add = int(input(" enter the length of list: "))

for i in range(1,add+1):
    num = int(input("enter a number to add in the list : "))
    new_list.append(num)
print(f"mew list is:  {new_list}")

for i in new_list:
    summation = summation + i
print(f"sum of all number in the list is : {summation}")


print("=========================================    END OF PROGRAM  =============================================")


"""

Mulitply of elements

"""

list_ = [2,4,6,2,7]
mult = 1
for i in list_:
    mult = i * mult

print(f"multiplication of number in list is : {mult}")


print("=========================================    END OF PROGRAM  =============================================")


# -----------------------------------------------------------------------------------------

"""

Sort elements in increasing order

"""
l = [3, 12, 5, 14, 1, 19]
new_list = []

print(f"The given list is: {l}")

while l:
    max_num = l[0]
    for i in l:
        if i > max_num:
            max_num = i
    new_list.append(max_num)
    l.remove(max_num)

print(f"The new list in descending order is: {new_list}")

# ------------------------------------  2nd way ---------------------------------------------

#  this is not correct
new_list = []

l = [3,12,5,14,1,19]

print(f"the given list is: {l}")
#max = l[0]
print(f"currently maxium number in the list : {max}")

for i in range(len(l)):
    max = l[0]
    if i > max:
        max = i
        for j in l:
            if max < j:
                max = j
        new_list.append(max)
        l.remove(max)
    else:
        print(f"i is : {i} , and max is : {max}")
print(f"the new lsit is : {new_list}")




print("=========================================    END OF PROGRAM  =============================================")

"""

Remove duplicates

"""


l_duplicate = [1,2,4,2,5,10,20,5,20]
print(f"older duplicate list : {l_duplicate}")
l_new = []
for i in l_duplicate:
    if i not in l_new:
        #l_new.append(i)
        l_new += [i]
        #print(l_new)
print(f"new list without duplicates: {l_new}")



print("=========================================    END OF PROGRAM  =============================================")

"""

Check list is empty or not

"""


l_empty = [1,2,4,2,5,10,20,5,20]
count=0
for i in l_empty:
    count = count + 1
    if count > 0:
        break


print("list is not empty")




print("=========================================    END OF PROGRAM  =============================================")

"""

Words that are longer than any element

"""
l_count =[]
l_words = ["ratann","kumar","jha"]
#count = 0
for i in l_words:
    count =0
    for j in i:
        count= count + 1
    l_count.append(count)
print(l_count)
new_dict = dict(zip(l_words,l_count))
print(new_dict)

max=l_count[0]
inddex=0
for i in range(len(l_count)):
    if max<l_count[i]:
        max = l_count[i]
        ind=i

print(f"Words that are longer than any element  :{l_words[inddex],max}")


print("=========================================    END OF PROGRAM  =============================================")

"""

Find common element from 2 lists

"""

list_a = [1, 4, 2, 5, 2, 9]
list_b = [2, 4, 2, 9, 6, 5]
new_list = []

for i in list_a:
    for j in list_b:
        if i == j:
            new_list += [i]
            # print(f"new _list is {new_list}")
            list_b.remove(i)

print(f"new list is  {new_list}")





print("=========================================    END OF PROGRAM  =============================================")


"""

Remove specified index from list and print

"""

l = [2, 3, 4, 5, 2, 6]
new_l = []
print(f"order list is {l}")
user_input = int(input("which index item u want ot remove: "))

for i in range(len(l)):
    if i !=user_input:
        new_l.append(l[i])

print(f"new list after removing the index:  {new_l}")



print("=========================================    END OF PROGRAM  =============================================")



"""

Remove even elements and print list

"""

l = [12,3,49,9,6,2]
new_l = []
for i in l:
    if i % 2 != 0:
        new_l =new_l + [i]
print(new_l)

print("=========================================    END OF PROGRAM  =============================================")



"""
Shuffle list and print
"""
import numpy as np
a= [2,3,4,1,5]
np.random.shuffle(a)
print(a)


print("=========================================    END OF PROGRAM  =============================================")


"""

Difference betweeen 2 lists
"""

l1 = [2,3,5,2]
l2 = [5,1,2,5]
l3=[]
for i in range(len(l1)):
    l3.append(l1[i]-l2[i])

print(l3)



print("=========================================    END OF PROGRAM  =============================================")

"""

To access index of list
"""

l = [2,3,4,2,7]

user_input = int(input("which index do u want to fetch: "))

for i in range(len(l)):
    if i == user_input:
        print(f"accessing the index- item,  given by the user:  {l[i]}")


print("=========================================    END OF PROGRAM  =============================================")

"""

Finding index of an item in specified list
"""

a= [2,4,1,5,7]
user_input = int(input("enter the item for which u want to get the index no.:  "))
ind=0
for i in range(len(a)):
    if a[i]== user_input:
        ind = i
        print(f"Number is :  {a[i]} and the index is: {ind}")


print("=========================================    END OF PROGRAM  =============================================")


"""

Append a list to second list
"""


l1=[1,2,3,4]
l2=[]
for i in l1:
    l2=l2+[i]

print(f"l2 :  {l2}")


print("=========================================    END OF PROGRAM  =============================================")

"""

Select an item randomly

"""

import random

my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)

print(random_item)



print("=========================================    END OF PROGRAM  =============================================")

"""

Finding a second largest number

"""


l = [10,12,4,5,19]
print(f"given list : {l}")
new_l = []

while l:
    max = l[0]
    for i in l:
        if i > max:
            max=i
    new_l.append(max)
    l.remove(max)
print(new_l)

for i in range(len(new_l)):
    if i == 1:
        print(f"the second largest number is  :{new_l[1]}")


print("=========================================    END OF PROGRAM  =============================================")



"""

Finding a second smallest number

"""


l = [10,12,4,5,19]
print(f"given list : {l}")
new_l = []

while l:
    min = l[0]
    for i in l:
        if i < min:
            min=i
    new_l.append(min)
    l.remove(min)
print(new_l)

for i in range(len(new_l)):
    if i == 1:
        print(f"the second largest number is  :{new_l[1]}")



print("=========================================    END OF PROGRAM  =============================================")

"""

Get unique values  

"""


lst = [2,3,5,1,6,2,3,4,2,68,24]
lst2=[]
for i in lst:
    if i not in lst2:
        lst2 =lst2 + [i]

print(lst2)


print("=========================================    END OF PROGRAM  =============================================")


"""

Frequency of elements
"""


lst = [2,3,5,1,6,2,3,4,2,68,68,24]
lst_new=[]
for i in lst:
    if i not in lst_new:
        lst_new=lst_new + [i]

#lst_new =set(lst)
print(lst_new)
for i in lst_new:
    count = 0
    for j in lst:
        if i == j:
            count = count+1
    print(f"number is : {i}, count is : {count}")




print("=========================================    END OF PROGRAM  =============================================")

"""

Insert an element before each element of a list
"""


l=[1,2,3]
print(f"older list is  : {l}")
new_l= []
for i in l:
    a=int(input("enter a num to insert before the element:  "))
    new_l=new_l+[a] + [i]
print(new_l)



print("=========================================    END OF PROGRAM  =============================================")


"""
Finding common items from two lists
"""

l1 = [2,3,4,5,6,10]
l2 = [5,2,8,9,0,10]
new_l = []
for i in l1:
    for j in l2:
        if i == j:
            new_l=new_l + [i]

print(f"new list is :  {new_l}")


print("=========================================    END OF PROGRAM  =============================================")



"""
Create a list by concatenating a given list which range goes from 1 to n
"""



my_list = ['p', 'q']
n = 4
new_list = []

for y in range(1, n+1):
    for x in my_list:
        new_list.append('{}{}'.format(x, y))

print(new_list)



print("=========================================    END OF PROGRAM  =============================================")

"""
fibonacci series
"""

fibonacci = int(input("enter a number for fibonacci series:  "))
a = 0
b = 1
print(a,end='  ')
print(b,end='  ')
for i in range(2,fibonacci):
    c=a+b
    a=b
    b=c
    print(c,end='  ')

print("=========================================    END OF PROGRAM  =============================================")

"""
swap

"""

l=[2,3,5,2,7]
print(f"older l {l}")
for i in range(len(l)-1):
    l[i],l[i+1]=l[i+1],l[i]


print(f"newer l {l}")




print("=========================================    END OF PROGRAM  =============================================")




"""

Split a list based on first character of word

"""




a= ['ratan','vikas','banana','apple']
a_l =[]
for i in a:
    for j in i:
        a_l =a_l + [j]
        break

print(a_l)
a_k=dict(zip(a_l,a))
print(a_k)


print("=========================================    END OF PROGRAM  =============================================")


"""

Replace the last element in a list with another list

"""

l1=[2,3,4,5]
l2=[43,5,7]
count=0
for i in range(len(l1)):
    count=count+1

replacing_last_with_other_list= l1[:l1[count-2]] + l2
print(f"final list is : {replacing_last_with_other_list}")



print("=========================================    END OF PROGRAM  =============================================")

"""
Insert an element before each element of a list
"""
l=[2,3,5,2]
new_l=[]
for i in l:
    a=int(input("enter a new number: "))
    new_l =new_l+[a]
    new_l=new_l+[i]


print(new_l)


print("=========================================    END OF PROGRAM  =============================================")




"""
Convert a string to a list
"""
new_l =[]
lst="ratankumarjha"
for i in lst:
    new_l=new_l+[i]
print(new_l)




print("=========================================    END OF PROGRAM  =============================================")



"""
Generate group of five consecutive numbers in a list
"""



n=list(range(1,21))
print(n)

new_l =[]

for i in range(0,len(n),5):
    #print(i)
    print(n[i:i+5])



print("=========================================    END OF PROGRAM  =============================================")



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
