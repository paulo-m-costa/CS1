# Name: Paulo Costa
# CMS cluster login name: pcosta

import random
import sys

# Problem 1.1
# 1) The for loop statement should be followed by ":", not ";".
# 2) The docstring needs to be enclosed with triple quotes.
# 3) The first elif statement should have two "="s.
# 4) The elif statements need to be as indented as the if statement. Otherwise,
# they won't be nested in the for loop.
# 5) The lists in the tuple being returned should be separated by commas.

# Problem 1.2
# 1) In the factorial function, the line "n -= 1" should be as indented as 
# "result *= n". Otherwise, the while loop would repeat indefinitely.
# 2) The constant "tiny" should be defined with one "=" sign, not two.
# 3) The factorial function only takes raw input, yet the sin function calls it
# with an argument.
# 4) There needs to be a break after the if statement in the sin function.
# 5) The sin function should return rather than print "result" so that a usable
# value is returned instead of a useless string being printed.

# Problem 1.3
# 1) [BAD_NAMES]: the function's name and argument are not descriptive enough.
# 2) [COMMENT_FULL_SENTENCES]: the comments are not full sentences.
# 3) [COMMENT_GRAMMATICAL]: the comments have several spelling/grammar issues.
# 4) [INDENT_CONSISTENT]: the indentations in the for loop are not consistent.
# 5) [OPERATOR_SPACE]: there should be single spaces around every operator.

# Problem 2.1
def random_walk(n, m):
    '''This function simulates a random walk and takes two positive integer 
    arguments. n is the threshold while m is the number of times the simulation 
    is repeated. Each round of the simulation will go like this: the position 
    of the walker will start at position 0 and then there will be a series of 
    steps, each of which is -1 or +1 (with equal probability). The simulation
    ends once the absolute value of the position exceeds n and the number of
    steps taken is recorded. The function the returns the average number of
    steps taken per simulation. The results seem to indicate that the average 
    number of steps required tends to be around the square of the threshold.'''
    position = 0
    steps = 0
    i = 1
    while i <= m:
        while abs(position) <= n:
            position += random.choice([-1, 1])
            steps += 1
        i += 1
        position = 0
    return float(steps) / float(m)

# Problem 2.2
def draw_box(n, p):
    '''This function takes two arguments: an integer n asserted to be positive,
    and a probability value p asserted to be between 0.0 and 1.0. It will draw 
    a box made up of '+' characters (the corners), '-' characters (the top and 
    bottom edges), and '|' characters (the left and right edges). The interior
    of the box will be made up of blank characters (' ') and 'O' (capital O) 
    characters. The interior of the box will be n by n characters. Inside the 
    box, the probability of having a capital O character in any given location
    will be p, meaning that the smaller p is, the emptier the box will look.'''
    assert n >= 0
    assert 0.0 <= p <= 1.0
    write = sys.stdout.write
    x = 1
    y = 1
    top = 1
    bottom = 1
    write('+')
    while top <= n:
        write('-')
        top += 1
    write('+\n')
    while y <= n:
        write('|')
        while x <= n:
            if random.random() < p:
                write('O')
            else:
                write (' ')
            x += 1
        write('|\n')
        x = 1
        y += 1
    write('+')
    while bottom <= n:  
        write('-')
        bottom += 1
    write('+')   

# Problem 2.3
def initial_value_count(lst):
    '''This function takes a non-empty list of integers as an argument. It 
    returns a tuple with two elements, where first element is the first value 
    in the argument list and the second element is the number of times the 
    first value is consecutively repeated starting at the beginning.'''
    a = lst[0]
    b = 1
    for el in range(len(lst) - 1):
        if lst[el] == lst[el + 1]:
            b += 1
        else: break            
    return (a, b)

def run_length_encode(lst):
    '''This function takes a (possibly empty) list of integers as an argument.
    It returns a list of tuples of length 2, where each tuple is a 
    (value, count) pair like in the previous function. The list of tuples is a 
    run-length encoded version of the original list.'''
    tuple_lst = []
    for el in range(len(lst)):
        tuple_lst += [initial_value_count(lst)]
        (a, b) = initial_value_count(lst)
        lst.remove(a)
    b_lst = [x[1] for x in tuple_lst]
    final_lst = tuple_lst[0:1]
    for el in range(len(b_lst) - 1):
        if b_lst[el] <= b_lst[el + 1]:
            final_lst.append(tuple_lst[el + 1])
    return final_lst