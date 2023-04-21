grocery_list = ['Apples', 'Oats', 'Almonds', 'Blueberries', 'Spinach']

for g in grocery_list:
    print(g)

for g in grocery_list:
    if g == 'Blueberries':
        break
    print(g)

for g in grocery_list:
    if g == 'Blueberries':
        continue
    print(g)

# Range Functionality
print(range(3))

for i in range(3):
    print(i, i + 1)

# While Loop
a = 5

while a < 5:
    print(a)
    a += 1 # a = a + 1