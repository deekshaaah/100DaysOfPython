# list comprehension is used to create lists in python

lst = [i for i in range(10)]
print(lst)

lst1 = [i*i for i in range(10)]
print(lst1)

# giving a condition within the list that is to be made

ls = [i for i in range(10) if i%2 == 0]
print(ls)
