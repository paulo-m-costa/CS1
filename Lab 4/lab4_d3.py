# Paulo Costa - Lab 4 Section D Part 3

from Tkinter import *
import random

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

def random_position(max_x, max_y):
    '''This function takes two non-negative integers called max_x and max_y as
    inputs and returns a random (x,y) tuple where 0 <= x <= max_x and 
    0 <= y <= max_y.'''
    assert max_x >= 0
    assert max_y >= 0
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)

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

def draw_square(canvas, color, length, center):
    canvas.pack()
    '''This function draws a square using four input arguments: 1. the canvas 
    on which it will be drawn, 2. its color, 3. the length of each of its sides,
    and 4. the position of the center of the square, represented as a tuple of 
    two integers. The function will both draw the square and return the square 
    that was drawn.'''
    x = float(center[0])
    y = float(center[1])
    length = float(length)
    r = canvas.create_rectangle(x - length / 2, y - length / 2, x + length / 2,
                                y + length / 2, fill = color, outline = color)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width = 800, height = 800)  
    for i in range(50):
        draw_square(c, random_color(), random_size(20, 150),
                    random_position(800, 800))
    root.bind('<q>', quit)
    root.mainloop()