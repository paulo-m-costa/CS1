# Paulo Costa - Lab 2 Part A

# Ex B.1:
def str_comp(DNA):
    '''This function takes a string representing a DNA sequence as input and 
    outputs the complementary sequence. A's and T's are switched with one
    another and so are C's and G's. This is done character by character.'''
    comp = ''
    for ch in DNA:
        if ch == 'A':
            comp += 'T'
        elif ch == 'C':
            comp += 'G'
        elif ch == 'T':
            comp += 'A'
        else:
            comp += 'C'
    return comp
# Ex B.2:
def list_comp(DNA):
    '''This function takes a list representing a DNA sequence as input and 
    creates the complementary sequence. A's and T's are switched with one
    another and so are C's and G's. This is done element by element.'''
    for el in range(len(DNA)):
        if DNA[el] == 'A':
            DNA[el] = 'T'
        elif DNA[el] == 'C':
            DNA[el] = 'G'
        elif DNA[el] == 'T':
            DNA[el] = 'A'
        else:
            DNA[el] = 'C'
# Ex B.3:
def product(nums):
    '''This function takes a list of numbers as input and outputs their product.
    If the list is empty, the output is 1. This is done element by element.'''
    p = 1
    for el in nums:
        p *= el
    return p
# Ex B.4:
def factorial(int):
    '''This function takes an integer as input and ouputs the value of its 
    corresponding factorial.'''
    f = product(range(1, int + 1))
    return f
# Ex B.5:
def dice(m, n):
    '''This function takes the tuple (m, n) as input, where m represents the 
    number of sides on a die, and n the number of times it is rolled. It outputs
    a possible sum given these parameters using the random.choice function.
    We assume that the die is number from 1 to m.'''
    import random
    sum = 0
    for i in range(n):
        sum += random.choice(range(1, m + 1))
    return sum
# Ex B.6:
def remove_all(int_list, target):
    '''This function takes a list of integers and a target integer as inputs
    and removes all instances of the target from the list.'''
    while int_list.count(target) > 0:
        int_list.remove(target)
# Ex B.7:
def remove_all2(int_list, target):
    '''This function takes a list of integers and a target integer as inputs
    and removes all instances of the target from the list.'''
    for i in range(int_list.count(target)):
        int_list.remove(target)
def remove_all3(int_list, target):
    '''This function takes a list of integers and a target integer as inputs
    and removes all instances of the target from the list.'''   
    while target in int_list:
        int_list.remove(target)
# Ex B.8:
def any_in(list1, list2):
    '''This functions takes two lists as inputs. It outputs 'True' if the lists
    have at least one element in common and 'False' otherwise.'''
    for el in list1:
        if el in list2:
            return True
    return False

# Ex C.1a: 'a = 0' should be 'a == 0'. The "if" clause requires '==' to check if
# a condition has been met, whereas '=' is used for defining variables.
a = 20
# ... later in the program, test to see if a has become 0.
if a == 0:
      print 'a is zero!'
# Ex C.1b: There cannot be quotation marks around the input(s) of a function.
# Once these are removed, s is predefined as a string and the code works.
def add_suffix(s):
    '''This function adds the suffix '-Caltech' to the string s.'''
    return s + '-Caltech'
# Ex C.1c: Again, the quotation marks around s should be removed. Otherwise, 
# this code would output 's-Caltech' instead of using the input string.
def add_suffix(s):
    '''This function adds the suffix '-Caltech' to the string s.'''
    return s + '-Caltech'
# Ex C.1d: Only lists can be concatenated with one another. The string 'bam'
# needs to be changed to its list equivalent i.e. ['bam'].
lst = ['foo', 'bar', 'baz']
lst = lst + ['bam']
# Ex C.1e: The reverse function does not return a list, so we cannot set 
# lst2 = lst.reverse(). Instead, we can write lst.reverse() and lst.append(0)
# as separate lines to create the desired list.
def reverse_and_append_zero(lst):
    '''This function reverses a list of numbers and then
    appends the number 0 to the end of the list.'''
    lst.reverse()
    lst.append(0)
# Ex C.1f: 'list' is already a variable name, so it would conflict with the
# function 'list' used to convert a string to a list. The code can be debugged
# by assigning a different name to the inputted list. Note that we are assuming
# that the code was intended to append the converted string as a single element.
def append_string_letters_to_list(lst, str):
    '''This function converts a string 'str' to a list and appends
    the letters of the string to the list 'list'.'''
    letters = list(str)
    lst.append(letters)
# Ex C.2: Since the lines of code are evaluated sequentially, c takes on the
# value of the sum of the values of a (10) and b (20) defined beforehand. To get
# c to be 50, we can move the line a = 30 before c = b + a and remove the
# redundant line a = 10, like so:
b = 20
a = 30
c = b + a
# Ex C.3: n = 2 * add_and_double_2(1, 2, 3) asks for 2 to be multiplied by a
# nonexistent return, which is not logical and would cause an error. Printing a 
# result outputs a representation of the result to the terminal whereas 
# returning a result generates an actual value that can be used in further 
# functions. Thus, the first function is the way to go:
def add_and_double_1(x, y, z):
    result = 2 * (x + y + z)
    return result
# Ex C.4: n = 2 * sum_of_squares_2(2, 3) asks for 2 to be multiplied by a result
# that can only be calculated once the user interactively inputs them via 
# raw_input after the function is called, whereas passing a value as an 
# argument to a function allows for an immediate result when the function is 
# called. Again, we stick with the first function:
def sum_of_squares_1(x, y):
    result = x * x + y * y
    return result
# Ex C.5: Strings are immutable, so we must first convert the string to a list, 
# capitalize the first letter, and then concatenate the letters back to a string. 
def capitalize(s):
    '''This function capitalizes the first letter of the string 's'.'''
    lst = list(s)
    lst[0] = lst[0].upper()
    s = ''
    for c in lst:
        s += c
    return s
# Ex C.6: 'item' is temporary. After each run of the for loop, the designation
# of 'item' is replaced. We must instead specify a range to iterate through.
def double_list(lst):
    '''This function doubles each element in a list in-place.'''
    for el in range(len(lst)):
        lst[el] *= 2