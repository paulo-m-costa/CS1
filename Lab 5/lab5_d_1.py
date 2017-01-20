# Paulo Costa - Lab 5 Section D Part 1

from Tkinter import *
import random

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

def draw_circle(x, y, min_r, max_r):
    '''This function takes four arguments: x, y, a minimum radius, and a 
    maximum radius. It then draws a circle centered at (x,y) of a random 
    radius between the given limits and returns a corresponding number.'''
    r = random.randint(min_r, max_r)
    circle = canvas.create_oval(x - r, y - r, x + r, y + r,
                                outline = color, fill = color)
    return circle

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global color
    global circles
    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'c':
        color = random_color()
    elif key == 'x':
        for circle in circles:
            canvas.delete(circle)
        circles = []

def button_handler(event):
    '''Handle left mouse button click events.'''
    circle = draw_circle(event.x, event.y, 5, 25)
    circles.append(circle)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width = 800, height = 800)
    canvas.pack()
    circles = []
    color = random_color()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()