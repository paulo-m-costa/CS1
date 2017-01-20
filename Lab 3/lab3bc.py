# Paulo Costa - Lab 3 Sections B and C

# Ex B.1:
def list_reverse(lst):
    '''This function takes a list as input and outputs its reverse without
    changing the original list using the reverse method.'''
    new_lst = lst[:]    
    new_lst.reverse()
    return new_lst
# Ex B.2:
def list_reverse2(lst):
    '''This function takes a list as input and outputs its reverse without
    changing the original list using the range function and a for loop.'''
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])
    return new_lst
# Ex B.3:
def file_info(file_name):
    '''This function takes a string representing the name of a text file as
    input and outputs the number of lines, words, and characters in the file in
    that order as a triple.'''
    fil = open(file_name, 'r')
    lines = 0
    words = 0
    characters = 0
    for line in fil:
        lines += 1
        words += len(line.split())
        characters += len(line)
    fil.close()
    return (lines, words, characters)
# Ex B.4:
def file_info2(file_name):
    '''This function takes a string representing the name of a text file as
    input and outputs a dictionary containing the line, word, and character 
    count using the keys 'lines', 'words', and 'characters' respectively.'''
    (l, w, c) = file_info(file_name)
    return {'lines': l, 'words': w, 'characters': c}
# Ex B.5:
def longest_line(file_name):
    '''This function takes a string representing the name of a text file as
    input and outputs the length of the longest line in the file as well as 
    the line itself as a double.'''
    fil = open(file_name, 'r')
    a = 0
    for line in fil:
        if len(line) > a:
            (a, b) = (len(line), line)
    fil.close()
    return (a, b)
# Ex B.6:
def sort_words(string):
    '''This function takes a string as input and uses the split method to 
    separate it into a list of words which it then sorts and ouputs.'''
    lst = string.split()
    lst_temp = lst.sort()
    return lst
# Ex B.7:
# 11011010 = 128 + 64 + 0 + 16 + 8 + 0 + 2 + 0 = 218
# The largest eight-digit binary number is 11111111 = 2^8 - 1 = 255.
# Ex B.8:
def binaryToDecimal(lst):
    '''This function takes a list of 0's and 1's representing a binary number
    as input and outputs the value of the decimal equivalent.'''  
    dec = 0
    for el in range(len(lst)):
        dec += lst[el]*2**(len(lst) - el - 1)
    return dec
    
# Ex C.2.1: The function name should be clearer [BAD_NAMES], there should be 
# single spaces after each comma [COMMA_SPACE], and there should be single 
# spaces around every operator [OPERATOR_SPACE].
def sum_of_cubes(a, b, c):
    return a * a * a + b * b * b + c * c * c
# Ex C.2.2: The function's name and arguments are too wordy [BAD_NAMES], the 
# comment is poorly written [COMMENT_FULL_SENTENCES] + [COMMENT_GRAMMATICAL], 
# and the last line is far too long [LINE_LENGTH].
def sum_of_cubes(a, b, c, d):
    # Returns the sum of the cubes of arguments a, b, c, and d.
    return a * a * a + b * b * b + c * c * c + d * d * d
# Ex C.2.3: The indentations should be consistent across both functions 
# [INDENT_CONSISTENT], and the functions should be separated by an empty line
# [BLANK_LINES].
def sum_of_squares(x, y):
    return x * x + y * y

def sum_of_three_cubes(x, y, z):
    return x * x * x + y * y * y + z * z * z