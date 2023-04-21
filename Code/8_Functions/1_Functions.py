def add_numbers(a, b):
    return a + b

print(add_numbers(5, 10))

def automated_greeting(name, age):
    if age >= 30:
        print('Hello, {}! You don\'t look a day over 20!'.format(name))
    else:
        print('Hello, {}! Have a great day!'.format(name))

automated_greeting('Matt', 31)
automated_greeting('Matt', 20)