list_a = []
print(list_a)
print(type(list_a))

# Lists are Ordered
list_a = [1, 2, 3, 4, 5]
list_b = [5, 4, 3, 2, 1]

print(list_a == list_b)

# Different data types in one list
list_a = ['apple', 1, 'banana', 2, 3.5]
print(list_a)

# Nested Lists
list_a = [[1, 2, 3], [4, 5, 6]]
print(list_a)

# Indexing Arrays
list_a = [1, 2, 3, 4, 5]
print(list_a[0]) # 1

# Length of a List
list_length = len(list_a)
print('The length of list_a is: ', list_length)
print(list_a[0:list_length])

# Lists are mutable
list_a[2] = 10
print(list_a)

# Appending and Prepending Data to a List
list_a = [1, 2, 3, 4, 5]
list_a += [25, 30, 100]
list_a = [150, 200] + list_a

# Tuples
tuple_a = (2)
print(type(tuple_a))

tuple_a = (2,)
print(type(tuple_a))
print(tuple_a)

tuple_a[0] = 10 # Error

(var1, var2, var3, var4) = tuple_a
print(var1, var2, var3, var4)