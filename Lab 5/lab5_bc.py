# Paulo Costa - Lab 5 Sections B and C

import math

# Ex B.1:
class Point:
    '''This class represents a point in three-dimensional Euclidean space with
    real-valued coordinates.'''
    
    def __init__(self, x, y, z):
        '''This method takes the coordinates of the point x, y, and z as its
        inputs and stores them in the object.'''
        self.x = x
        self.y = y
        self.z = z
        
    def distanceTo(self, other):
        '''This method takes another point as its input and computes the 
        distance between that point and the point being acted on using the 
        Euclidean distance formula.'''
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + 
                (other.z - self.z) ** 2) ** 0.5

# Ex B.2:
class Triangle:
    '''Instances of this class contain three points describing a triangle.'''
    
    def __init__(self, p1, p2, p3):
        '''This method takes three points and stores them in the object.'''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def area(self):
        '''This method computes the area of the triangle represented using
        Heron's formula.'''
        a = self.p1.distanceTo(self.p2)
        b = self.p1.distanceTo(self.p3)
        c = self.p2.distanceTo(self.p3)
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** (0.5)
    
# Ex B.3:
class Averager:
    '''The purpose of this class is to store a list of numbers and perform
    various operations on it.'''
    
    def __init__(self):
        '''Constructor which initializes the fields.'''
        self.nums = []
        self.total = 0.0
        self.n = 0
        
    def getNums(self):
        '''Returns a copy of the list of numbers stored so far.'''
        return self.nums[:]
    
    def append(self, num):
        '''Appends a new number to the list.'''
        self.nums.append(num)
        self.total += num
        self.n += 1
        
    def extend(self, num_lst):
        '''Appends an additional list of numbers to the existing list.'''
        self.nums.extend(num_lst)
        self.total += sum(num_lst)
        self.n += len(num_lst)
            
    def average(self):
        '''Computes the average of the stored list. If the list is empty, 
        returns 0.0. Always returns a floating-point value.'''
        if self.n == 0:
            return 0.0
        return self.total / self.n
        
    def limits(self):
        '''Computes the minimum and maximum of the stored list. If the list is 
        empty, returns the tuple (0, 0).'''
        if self.n > 0:
            minimum = min(self.nums)
            maximum = max(self.nums)
            return (minimum, maximum)
        return (0, 0)
        
# Ex C.1:
# The else statement is unnecessary; we can return the Boolean value of the
# statement "x > 0" instead.
def is_positive(x):
    '''Returns True if x is positive and False otherwise.'''
    return x > 0

# Ex C. 2:
# The variables "found" and "location" are unnecessary. If the item is not
# found, -1 will be returned. If it is found, we can just return "i" as the 
# location of the object. The "else" is also unnecessary because if the item
# is found, the function will stop.
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise. Assume
    that x is found at most once in the list.'''
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1

# Ex. C.3:
# This function is inefficient. For any given of x, it checks each of the four
# "if" statements. Since the categories do not overlap, we can instead use 
# "elif" after the first "if". Additionally, since the four categories cover
# all possibilities, the final "if" can be changed to an "else" statement.
def categorize(x):
    '''Return a string categorizing 'x', which should be an integer.'''
    if x < 0:
        category = 'negative'
    elif x == 0:
        category = 'zero'
    elif x > 0 and x < 10:
        category = 'small'
    else:
        category = 'large'
    return category

# Ex C.4:
# This function is immensely inefficient. We do not need separate cases for
# lists of specific lengths. Instead, we can just set "total" to initially be 0
# and return "total" at the end of the function, thus satisfying that 0 is
# returned if the list is empty. If the list is not empty, all we need is a
# "for" statement to add every item in the list to "total".
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    total = 0
    for item in lst:
        total += item
    return total