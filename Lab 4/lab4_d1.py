# Paulo Costa - Lab 4 Section D Part 1

from Tkinter import *
root = Tk()
root.geometry('800x800')
c = Canvas(root, width = 800, height = 800)
c.pack()
r1 = c.create_rectangle(0, 0, 100, 100, fill = 'red', outline = 'red')
r2 = c.create_rectangle(700, 0, 800, 100, fill = 'green', outline = 'green')
r3 = c.create_rectangle(0, 700, 100, 800, fill = 'blue', outline = 'blue')
r4 = c.create_rectangle(700, 700, 800, 800, fill = 'yellow', outline = 'yellow')
root.mainloop()