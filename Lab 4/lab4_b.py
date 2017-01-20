# Paulo Costa - Lab 4 Section B

import random
# Ex B.1:
def random_size(small_e_int,big_e_int):
    '''This function takes two non-negative even integers as inputs, the first
    one smaller than the second, and returns a random even integer between the 
    two inclusive. It checks that the inputs meet these criteria and that the
    output is even as well.'''
    assert small_e_int >= 0 
    assert big_e_int >= 0
    assert small_e_int % 2 == 0
    assert big_e_int % 2 == 0
    assert small_e_int < big_e_int    
    mid_e_int = 2 * random.randint(small_e_int / 2, big_e_int / 2)
    assert mid_e_int % 2 == 0
    return mid_e_int
# Ex B.2:
def random_position(max_x, max_y):
    '''This function takes two non-negative integers called max_x and max_y as
    inputs and returns a random (x,y) tuple where 0 <= x <= max_x and 
    0 <= y <= max_y.'''
    assert max_x >= 0
    assert max_y >= 0
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)
# Ex B.3:
def random_color():
    '''This function generates random color values in the format recognized by 
    the Tkinter graphics package, which are strings of the form '#RRGGBB'. Each
    pair of identical letters represents a hexadecimal number (00 to ff or 0 to 
    255 in decimal) that indicates the relative intensities of red, green, and
    blue respectively, that constitute the final color.'''
    string = '#'
    for i in range(6):
        string += random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                 'a', 'b', 'c', 'd', 'e', 'f'])
    return string
# Ex B.4:
def count_values(dictionary):
    '''This function takes a dictionary as input and returns the number of 
    distinct values it contains.'''
    count = 0
    lst = []
    for entry in dictionary:
        if dictionary[entry] not in lst:
            count += 1
            lst.append(dictionary[entry])
    return count
# Ex B.5:
def remove_value(dictionary, value):
    '''This function takes a dictionary and an arbitrary item which could be a 
    value in the dictionary as inputs. It removes (via del) all the key/value
    pairs from the dictionary which have that value. If the value is not in the 
    dictionary, it does nothing. It returns nothing.'''
    lst = []
    for entry in dictionary:
        if dictionary[entry] == value:
            lst.append(entry)
    for entry in lst:
        del dictionary[entry]
# Ex B.6:
def split_dict(dictionary):
    '''This function takes a dictionary which uses strings as keys as input and
    returns a tuple of two dictionaries whose key/value pairs are from the 
    original dictionary: those whose keys start with the letters a-m and those 
    whose keys start with the letters n-z regardless of capitalization. The
    original dictionary is not altered.'''
    dictionary_am = {}
    dictionary_nz = {}
    for entry in dictionary:
        if 'a' <= entry[0].lower() <= 'm':
            dictionary_am[entry] = dictionary[entry]
        if 'n' <= entry[0].lower() <= 'z':
            dictionary_nz[entry] = dictionary[entry]
    return dictionary_am, dictionary_nz
# Ex B.7:
def count_duplicates(dictionary):
    '''This function takes a dictionary as input and returns the number of 
    values that appear two or more times.'''
    lst = []
    for entry in dictionary:
        lst.append(dictionary[entry])
    count_d = 0
    for entry in lst:
        if lst.count(entry) >= 2:
            count_d += 1
            while lst.count(entry) > 1:
                lst.remove(entry)
    return count_d