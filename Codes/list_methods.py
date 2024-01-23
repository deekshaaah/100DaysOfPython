# list methods

print("Orignal list : ")
lst = [4, 7, 2, 9, 4]
print(lst)

print("Appended list : ")
lst.append(1)
print(lst)

print("Sorted list : ")
lst.sort()
print(lst)

print("Descending order : ")
lst.sort(reverse = True)
print(lst)

print("Reversing the list : ")
lst.reverse()
print(lst)

print("First index of an element : ")
print(lst.index(4))

print("Number of occurence of an element : ")
print(lst.count(7))

print("To create the exact same list from an existing list : ")
m = lst.copy()
print(m)

print("To replace an element from a particular index: ")
lst.insert(2, 143)
print(lst)

print("To extend a list by adding the elements of other list at the end : ")
a = [100, 200, 300]
lst.extend(a)
print(lst)

print("To concatenate / To create a new list without changing the orignal list : ")
k = a + lst
print(k)

