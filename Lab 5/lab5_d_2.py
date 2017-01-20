# Paulo Costa - Lab 5 Section D Part 2

from Tkinter import *
import random
import math

# Graphics commands.

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

def draw_line(p1, p2):
    '''This function takes two points and draws a colored line between them.'''
    (x1, y1) = p1
    (x2, y2) = p2
    line = canvas.create_line(x1, y1, x2, y2, fill = color)
    return line

def draw_star(x_center, y_center):
    '''This function draws an N-pointed star centered at the inputted 
    coordinates using identical lines of random length and color. The center 
    point of the star points vertically upward. It returns a list of the
    handles of all the lines drawn.'''
    rad = random.randint(50, 100)
    angle = 0.0
    lst = []
    star = []
    for end in range(N):
        x_end = rad * math.cos(angle)
        y_end = rad * math.sin(angle)
        new_x_end = y_end + x_center
        new_y_end = - x_end + y_center
        lst.append((new_x_end, new_y_end))
        angle += 2 * math.pi / N
    for i, el in enumerate(lst):
        line = draw_line(el, lst[(i + (N - 1) / 2) % N])
        star.append(line)
    return star

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global lines
    global color
    global N
    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'c':
        color = random_color()
    elif key == 'x':
        for line in lines:
            canvas.delete(line)
        lines = []   
    elif key == 'plus':
        N += 2
    elif key == 'minus':
        if N != 5:
            N -= 2

def button_handler(event):
    '''Handle left mouse button click events.'''
    draw_star(event.x, event.y)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width = 800, height = 800)
    canvas.pack()
    lines = []
    color = random_color()
    N = 5

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()