# Paulo Costa - Lab 7 Sections B and C

# Ex B.1:
def union(set1, set2):
    '''This function takes two sets as arguments and returns their union.'''
    superset = set()
    for i in set1:
        superset.add(i)
    for i in set2:
        superset.add(i)
    return superset
   
def intersection(set1, set2):
    '''This function takes two sets and returns their intersection.'''
    subset = set()
    for i in set1:
        if i in set2:
            subset.add(i)
    return subset

# Ex B.2:
def mySum(*x):
    '''This function takes an arbitray number of arguments, all of which should
    be integers greater than zero, and returns their sum. If an argument isn't 
    an integer, a TypeError is raised with a message. If an argument is less 
    than or equal to zero, a ValueError is raised with a message.'''
    total = 0
    for i in x:
        if not isinstance(i, int):
            raise TypeError('all arguments must be integers')
        elif i <= 0:
            raise ValueError('all arguments must be greater than 0')
        else:
            total += i
    return total

# Ex B.3:
def myNewSum(*x):
    '''This function takes a single list of positive integers as its argument 
    and returns the sum of the list. It can also take an arbitrary number of 
    individual values (positive integers), but it won't accept both individual 
    values and a list, nor will it take multiple lists (it will raise a 
    TypeError in either case). It will also raise a TypeError if the list's 
    elements are not integers and a ValueError if any is smaller than 1.'''
    total = 0
    if len(x) == 0:
        return total
    elif isinstance(x[0], list) and len(x) == 1:
        values = x[0]
    else:
        values = x
    for i in values:
        if not isinstance(i, int):
            raise TypeError('all arguments must be integers')
        elif i < 1:
            raise ValueError('all arguments must be at least 1')
        else:
            total += i
    return total

# Ex B.4:
def myOpReduce(lst, **op):
    '''This function takes one required argument (a list of integers) and one 
    keyword argument called op, whose value is a string. If op is '+', then the
    function sums the integers; if op is '*', then it multiplies them together.
    If op is 'max', it returns the largest integer. If there is no keyword 
    argument, more than one keyword argument, or no valid keyword argument 
    (i.e. if op is not the key, or if the value of the keyword is not one of 
    the three allowed strings), then a ValueError is raised. If there is a 
    keyword argument of a non-string type, a TypeError is raised.'''
    if len(op) == 0:
        raise ValueError('no keyword argument')
    elif len(op) > 1:
        raise ValueError('too many keyword arguments')
    elif 'op' not in op:
        raise ValueError('invalid keyword argument: key must be "op"')    
    elif not isinstance(op['op'], str):
        raise TypeError('value for keyword argument "op" must be a string')
    elif op['op'] not in ['+', '*', 'max']:
        raise ValueError('invalid keyword argument: not "+", "*", or "max"')
    elif op['op'] == '+':
        total = 0
        for c in lst:
            total += c
        return total
    elif op['op'] == '*':
        product = 1
        for c in lst:
            product *= c
        return product
    elif op['op'] == 'max':
        maximum = 0
        for c in lst:
            if c > maximum:
                maximum = c
        return maximum

# Ex C.1:
# Upon catching the exception, the function should raise the error along with a
# helpful message. The original function simply exits the system.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:
        raise KeyError('key not found in dictionary')

# Ex C.2:
# The original function does not show the location of the error.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:
        raise KeyError('key not found in dictionary')
  
# Ex C.3:
# The original function does not have a helpful error message.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:
        raise KeyError('key not found in dictionary')

# Ex C.4:
# The code used for the previous problems is much more concise and efficient
# than the original code used here; we needn't check the values individually. 
# Also, the object e should have been printed and accompanied with a message.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:
        raise KeyError('key not found in dictionary')

# Ex C.5:
# Once the ValueError is raised, the rest of the code is ignored, meaning that
# no error message is displayed in the original function.
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0') 
    elif n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Ex C.6:
# We can just have the error message accompany the ValueError when it is raised
# rather than having to import a module and add an extra line.
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:    
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Ex C.7:
# The original function does not account for when x = 0, which results in 
# division by 0. The error must be raised when x is less than or equal to 0.
from math import exp

def exp_x_over_x1(x):
    '''Return the value of e**x / x, for x > 0 and e as the base of ln.'''
    if x <= 0:
        raise TypeError('x must be > 0.0')
    return (exp(x) / x)

# Ex C.8:
# The original function does not distinguish between TypeError and ValueError;
# it treats them both as Exceptions and thus is not as specific or helpful.
from math import exp

def exp_x_over_x(x):
    '''Return the value of e**x / x, for x > 0 and e as the base of ln.'''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)