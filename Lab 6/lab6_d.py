# Paulo Costa - Lab 6 Section D

'''
This module simulates balls bouncing around a canvas.
'''

import math
import random
from Tkinter import *

class BouncingBall:
    '''Objects of this class represent balls which bounce on a canvas.'''
    def __init__(self, canvas, center, radius, color, direction, speed):
        '''Create a new ball at center of the given radius and color, 
        moving at a given direction and speed.'''

        x, y = center
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        self.handle = canvas.create_oval(x1, y1, x2, y2,
                        fill = color, outline = color)
        self.canvas = canvas
        self.xmax   = int(canvas.cget('width')) - 1
        self.ymax   = int(canvas.cget('height')) - 1
        self.center = center
        self.radius = radius
        self.color  = color

        # The direction is represented as an angle in degrees
        # (range 0-360), which we convert to radians here.
        # The angle is with respect to the positive x axis,
        # going clockwise around the origin.
        if direction < 0.0 or direction > 360.0:
            raise ValueError('Invalid direction; must be in range [0.0, 360.0]')
        dir_radians = direction * math.pi / 180.0
        # Separate the direction into its x and y coordinates.
        # Flip the sign of the y coordinate because the y coordinate
        # grows downward, not upward.
        self.dirx = math.cos(dir_radians)
        self.diry = -math.sin(dir_radians)

        # Speed is represented as a single non-negative float.
        if speed < 0.0: 
            raise ValueError('Invalid speed; must be positive')
        self.speed = speed

    def step(self):
        '''Move this ball in its current direction with its
        current speed.  Change direction if the edge of the
        canvas is reached.'''
        v_x = round(self.speed * self.dirx)
        v_y = round(self.speed * self.diry)
        (c_x, c_y) = self.center
        x_displacement = self.displacement(c_x, v_x, self.xmax)
        y_displacement = self.displacement(c_y, v_y, self.ymax)
        if x_displacement != v_x:
            self.dirx *= -1
        if y_displacement != v_y:
            self.diry *= -1
        self.canvas.move(self.handle, x_displacement, y_displacement)
        self.center = (c_x + x_displacement, c_y + y_displacement)

    def displacement(self, c, d, cmax):
        '''Compute the actual displacement along the x or y dimension,
        taking reflections off the edge into account.  'c' is the
        center of the ball (x or y coordinate); 'cmax' is the largest 
        value in that direction, and 'd' is the desired displacement
        in that direction.'''
        if c + d + self.radius > cmax:
            return (cmax - c - self.radius) - (d - (cmax - c - self.radius))
        elif c + d - self.radius < 0:
            return (self.radius - c) + (self.radius - c - d)
        else:
            return d

    def scale_speed(self, scale):
        '''Scale the speed of this object by a factor 'scale'.'''
        self.speed *= scale

    def delete(self):
        '''Remove this object from the canvas.'''
        self.canvas.delete(self.handle)

def random_ball(canvas, rmin, rmax, smin, smax, xmax, ymax):
    '''
    Create and return a ball with a random color, starting position,
    size, direction, and velocity.
    rmin: minimum radius (pixels)
    rmax: maximum radius (pixels)
    smin: minimum speed
    smax: maximum speed
    xmax: maximum x dimension of canvas
    ymax: maximum y dimension of canvas
    '''
    radius = random.randint(rmin, rmax)
    speed = random.randint(smin, smax)
    direction = random.randint(0, 360)
    c_x = random.randint(radius, xmax - radius)
    c_y = random.randint(radius, ymax - radius)
    color = '#'
    for i in range(6):
        color += random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                'a', 'b', 'c', 'd', 'e', 'f'])
    return BouncingBall(canvas, (c_x, c_y), radius, color, direction, speed)

def key_handler(event):
    '''Handle key presses.'''
    global bouncing_balls
    global done
    key = event.keysym
    if key == 'q': 
        done = True
    elif key == 'plus':  # add a ball
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))
    elif key == 'minus':  # remove a ball
        if len(bouncing_balls) > 0:
            b = bouncing_balls.pop(0)
            b.delete()
    elif key == 'u':  # speed Up all bouncing_balls by factor of 1.2
        for ball in bouncing_balls:
            ball.scale_speed(1.2)
    elif key == 'd':  # slow Down all bouncing_balls by factor of 1.2
        for ball in bouncing_balls:
            ball.scale_speed(1 / 1.2)
    elif key == 'x':  # delete all bouncing_balls
        for ball in bouncing_balls:
            ball.delete()
        bouncing_balls = []

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, width = 800, height = 600)
    canvas.pack()
    done = False

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    
    # Set up some bouncing balls.
    bouncing_balls = []
    for i in range(5):
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))

    # Start the event loop.
    while not done:
        for ball in bouncing_balls:
            ball.step()
        root.update()