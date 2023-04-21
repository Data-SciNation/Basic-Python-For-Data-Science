x = 1
y = 5
z = 1

print('x < y is', x < y) # True
print('x > y is', x > y) # False
print('x == z is', x == z) # True


print('A' == 'a') # False
print('A' < 'a') # True

# And/Or (&, |)
print((5 < 10) & (10 < 20)) # True
print((5 < 10) & (10 > 20)) # False
print((5 < 10) | (10 > 20)) # True