# Single Quotes
print('This is a string')

# Double Quotes
print("This is a string")

# Apostraphe
print("Here's a string with an apostraphe")
print('Here\'s a string with an apostraphe')

# Double quotes inside string
print('The title is "At the Horizon" and it is a great book')
print("The title is \"At the Horizon\" and it is a great book")

# Convert Strings to Numbers
print(int('123')) # 123
print(type(int('123'))) # class 'int'

# Convert String to Float
print(float('123.456'))
print(type(float('123.456')))

# Convert Numeric to String
print(str(123))
print(type(str(123)))

# Indexing
print('Hello, World!'[0]) # H
print('Hello, World!'[8]) # o
print('Hello, World!'[0:5]) # Hello
print('Hello, World!'[0::2]) # Hlo ol!

# Input Function
print('Hello, ', input('Input Your Name: '))
print('Hello, ', input('Input Your Name:\n'))