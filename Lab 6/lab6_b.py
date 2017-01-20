# Paulo Costa - Lab 6 Section B

# Ex B.1: Print a blank line to the terminal. Limit 5 characters.
# print

# Ex B.2: Add 10 to 'x', which contains a number. Limit 5 characters.
# x += 10

# Ex B.3: 'los' is a  list of strings. Join these into a single string, with
# each string separated from the next in the list by a single space character.
# Do this by calling a single method on strings. Limit 15 characters.
# s = ' '.join(los)

# Ex B.4: Same as before, but now the strings aren't separated by spaces.
# s = ''.join(los)

# Ex B.5: Same as before, but now the strings are separated by newlines.
# s = '\n'.join(los)

# Ex B.6: You have a list lst. Use it to create a list lst2 which is equal to 
# the first 5 elements of lst. Limit 12 characters.
# lst2 = lst[:5]

# Ex B.7: Write a boolean expression that tests whether or not a variable 'x' 
# containing a single-character string is a vowel. Limit 10 characters.
# x in 'aeiou'

# Ex B.8: 'grid' contains a list of lists of integers (a two-dimensional list).
# Write a Python expression that will retrieve the first element of the first 
# list in 'grid' and assign it to the variable 'first'. Limit 20 characters.
# first = grid[0][0]

# Ex B.9: Assign the number 42 to the first element of the first list in 'grid',
# which you can assume exists. Limit 15 characters.
# grid[0][0] = 42

# Ex B.10: Assume you have an open file object called f which corresponds to a 
# text file on your computer. Write two very short lines of Python code to read 
# all the lines of the file, capitalize them, and print them to the terminal. 
# Do not use the readlines method on files. Limit 20 characters per line.
# for l in open('f', 'r'):
#    print l.upper()

# Ex B.11: Assume you have a variable called 's' which contains a lowercase 
# string. Change 's' so that it's now uppercase and in reversed order. This can 
# be done in one line using just function calls, method calls, and assignments.
# s = s.upper()[::-1]