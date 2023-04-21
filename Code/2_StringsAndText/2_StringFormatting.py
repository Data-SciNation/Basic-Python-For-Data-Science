# General .format syntax
print('{}, {}'.format('First String', 'Second String'))

# Ordered formatted printing
print('{0}, {1}'.format('First String', 'Second String'))
print('{0}, {0}'.format('First String', 'First String'))
print('{1}, {0}'.format('Second String', 'First String'))


# Aligning the text in your strings
print('{:<29}'.format('This string is left aligned'))
print('{:>29}'.format('This string is right aligned'))
print('{:^29}'.format('This string is centered'))
# We can fill these spaces with 
# a specified character.
print('{:$^29}'.format('This string is centered'))

# Format data with a comma thousands separator
print('{:,}'.format(1350642978))

# Show the +/- sign on values
print('{:+f}, {:+f}'.format(5.0, -5.0))
# Only show the - sign
print('{:f}, {:f}'.format(5.0, -5.0))

# Convert float to percentage with 2 decimal places
print('{:.2%}'.format(5 / 12))