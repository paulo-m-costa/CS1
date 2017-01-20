# Paulo Costa - Lab 4 Section D Part 2

from Tkinter import *

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
    draw_square(c, 'red', 100, (50, 50))
    draw_square(c, 'green', 100, (750, 50))
    draw_square(c, 'blue', 100, (50, 750))
    draw_square(c, 'yellow', 100, (750, 750))
    root.mainloop()