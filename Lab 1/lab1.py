# Paulo Costa - Lab 1

# Ex C.1.1: 9 - 3 --> 6
# Ex C.1.2: 8 * 2.5 --> 20.0
# Ex C.1.3: 9 / 2 --> 4
# Ex C.1.4: 9 / -2 --> -5
# Ex C.1.5: 9 % 2 --> 1
# Ex C.1.6: 9 % -2 --> -1
# Ex C.1.7: -9 % 2 --> 1
# Ex C.1.8: 9 / -2.0 --> -4.5
# Ex C.1.9: 4 + 3 * 5 --> 19
# Ex C.1.10: (4 + 3) * 5 --> 35
# Ex C.2.1: x = 100 --> 100
# Ex C.2.2: x = x + 10 --> 110
# Ex C.2.3: x += 20 --> 130
# Ex C.2.4: x = x - 40 --> 90
# Ex C.2.5: x -= 50 --> 40
# Ex C.2.6: x *= 3 --> 120
# Ex C.2.7: x /= 5 --> 24
# Ex C.2.8: x %= 3 --> 0
# Ex C.3: 
# We first assign x = 3. When Python evaluates the statement x += x - x, it is
# adding the value of (x - x) to x, which means it is adding 0 to 3. Hence, the
# new value of x is still 3.
# Ex C.4a.1: 1j + 2.4j --> 3.4j
# Ex C.4a.2: 4j * 4j --> (-16+0j)
# Ex C.4a.3: (1+2j) / (3+4j) --> (0.44+0.08j)
# Ex C.4b.1: (1+2j) * (1+2j) --> (-3+4j)
# Ex C.4b.2: 1+2j * 1+2j --> (1+4j)
# The previous two answers are different because in the second case, Python
# prioritizes the operation * over + and thus evaluates 2j * 1 before it adds
# the terms 1 and 2j to give (1+4j). This means that unless the terms are
# bracketed, Python interprets the real and imaginary components of complex
# numbers separately.
# Ex C.5.1: cmath.sin(-1.0+2.0j) --> (-3.165778513216168+1.959601041421606j)
# Ex C.5.2: cmath.log(-1.0+3.4j) --> (1.2652585805200263+1.856847768512215j)
# Ex C.5.3: cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)
# Writing
import math
import cmath
# rather than
from math import *
from cmath import *
# allows you to use functions from both modules by adding the respective prefix,
# 'math' or 'cmath'. In the latter case, you would only be able to use the cmath
# functions as the functions imported by the second command would overwrite
# those imported by the first.
# Ex C.6.1: "foo" + 'bar' --> 'foobar'
# Ex C.6.2: "foo" 'bar' --> 'foobar'
# Ex C.6.3: a = 'foo'; b = "bar"; a + b --> 'foobar'
# Ex C.6.4: a = 'foo'; b = "bar"; a b --> invalid syntax:<string>, line 1, pos 3
# Ex C.7: 'A\nB\nC' is an equivalent expression.
# Ex C.8: '-' * 80 --> generates a string of 80 '-' characters.
# Ex C.9: 'first line\nsecond line\nthird line' gives this result when printed.
# Ex C.10: 
x = 3
y = 12.5
# Ex C.10.1:
print('The rabbit is %d.' % x)
# Ex C.10.2:
print('The rabbit is %d years old.' % x)
# Ex C.10.3:
print('%g is average.' % y)
# Ex C.10.4:
print('%g * %d' % (y,x))
# Ex C.10.5:
print('%g * %d is %g.' % (y,x,x * y))
# Ex C.11:
num = float(raw_input('Enter a number: '))
print(num)
# Ex C.12:
def quadratic(a,b,c,x):
    return a * x ** 2 + b * x + c
# Ex C.13:
def GC_content(DNA):
    '''This function takes a string representing a DNA sequence as input and 
    outputs the proportion of characters that are either G's or C's. We assume
    that there are only A, C, G, or T bases and thus tally up the number of G's
    and C's and then divide this number by the length of the entire string.'''
    GC = float(DNA.count('G') + DNA.count('C'))
    total = float(len(DNA))
    return GC / total