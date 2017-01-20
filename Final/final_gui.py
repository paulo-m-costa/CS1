# Name: Paulo Costa
# CMS cluster login name: pcosta

'''
final_gui.py: The CS 1 final exam, part 2.
'''

import sys, copy, time
from Tkinter import *
from final import *

class ColorGameGUI(ColorGame):
    def __init__(self):
        '''
        Initialize the game.

        Arguments: none
        Return value: none
        '''
        # Supplied to the students.  DO NOT MODIFY!

        # Call the superclass constructor on this object.
        ColorGame.__init__(self)
        
        # Tkinter code for display.
        # Nominal starting size of 100x100 pixels.
        self.root = Tk()
        self.root.geometry('100x100')
        self.canvas = Canvas(self.root, width=100, height=100)
        self.canvas.pack(fill='both', expand=True)

    def displayBoard(self):
        '''
        Update a Tkinter canvas showing the board contents.

        Arguments: none
        Return value: none
        '''
        dct = {'.' : 'red', 'a' : 'green', 'b' : 'blue', 'c' : 'yellow',
               'd' : 'orange', 'e' : 'purple'}
        self.canvas.config(width = 25 * self.ncols, height = 25 * self.nrows)
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.canvas.create_rectangle(25 * i,  25 * (i + 1) , 25 * j, 
                                             25 * (j + 1), fill = dct[1], 
                                             outline = dct[1])
        self.canvas.delete('all')

    def printBoard(self, board, nmoves, file=sys.stdout):
        '''
        Print a board to a file. 

        Arguments:
          board  -- the board to print
          nmoves -- the number of moves leading up to this board
          file   -- the file to print to (default stdout)

        Return value: none
        '''
        ColorGame.printBoard(self, board, moves, file=sys.stdout)
        self.displayBoard()

    def makeMove(self, row, col, color):
        '''
        Make a move on the  board by changing the color of the square at (row,
        col) to 'color'.  Raise a MoveError exception if the move is invalid.

        Arguments:
          row   -- the row on the board
          col   -- the column on the board
          color -- the desired color (a letter from a-e or '.')

        Return value: none
        '''
        if color in 'abcde.' and self.isLegalMove(row, col, color) == True:
            self.updateGameHistory(row, col, color)
            original = self.board[row][col]
            self.board[row][col] = color
            self.nmoves += 1
            for (a, b) in self.adjacentLocations(row, col):
                if self.board[a][b] == original:
                    time.sleep(0.1)
                    self.makeMove(a, b, color)
                    self.nmoves -= 1
                    self.history.pop()
        else:
            raise MoveError('Invalid move: ' + str((row, col, color)))                    
        x = self.history.pop()
        self.history += [(x[0], copy.deepcopy(self.board))]
        
if __name__ == '__main__':
    game = ColorGameGUI()
    game.play()