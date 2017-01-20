# Paulo Costa - Lab 7 Section D - Interactive Sudoku

'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        '''This method creates the board and stores it as a field of the Sudoku 
        object. The board is a list of lists of numbers that represents the 
        9x9 grid used in standard Sudoku. An empty square is represented by the
        number 0. The Sudoku instances have a field representing a list of
        moves, which is initially empty and initialized in this method.'''
        lst = []
        for i in range(9):
            lst.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board = lst[:]
        self.list_of_moves = []

    def load(self, filename):
        '''This method takes one argument (a filename) and loads the contents 
        of the file into the object's board representation. If the file exists,
        but it has the wrong number of lines, or the lines are not exactly 9 
        characters long, or the lines have characters other than the digits 0 
        to 9, then an IOError exception with an appropriate error message is 
        raised. No error is caught in this method. If the file is ok, then all 
        the digits in the file get copied into the board representation. The 
        list of moves is also cleared, since a new game is started.'''
        file = open(filename, 'r')
        lst = []
        line_count = 0
        for line in file:
            line_count += 1
            if len(line) - 1 != 9:
                raise IOError('The lines must all be 9 characters long.')
            lst2 = []
            for c in line[0:9]:
                if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    raise IOError('The characters must be 0 to 9.')
                lst2.append(int(c))
            lst.append(lst2)
        file.close()
        if line_count != 9:
            raise IOError('The number of lines must be equal to 9.')
        self.board = lst
        self.list_of_moves = []

    def save(self, filename):
        '''The save method takes one argument (the name of the file to save the 
        board representation to) and writes the board representation to the 
        file with the given name.'''
        file = open(filename, 'w')
        for i, j in enumerate(self.board):
            for x, y in enumerate(j):
                file.write(str(y))
            file.write('\n')

    def show(self):
        '''Pretty-print the current board representation.'''
        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print 
        print '  +-----+-----+-----+'
        print

    def move(self, row, col, val):
        '''The move method takes three arguments: the row, the column, and the 
        number to place at the resultant location, all of which range from 1-9
        inclusive. This method has several responsibilities:
        1. It checks that the inputs are valid coordinates,
        2. It checks that the move is a valid move on the board, 
        3. It makes the move by writing into the board representation, and 
        4. It appends the move into the list of moves stored in the object.'''
        valid_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if row not in valid_int:
            raise SudokuMoveError('The row coordinate is not valid.')
        elif col not in valid_int:
            raise SudokuMoveError('The column coordinate is not valid.')
        elif val not in valid_int:
            raise SudokuMoveError('The value is not valid.')
        elif self.board[row - 1][col - 1] != 0:
            raise SudokuMoveError('That space is already occupied.')
        elif val in self.board[row - 1]:
            raise SudokuMoveError('That value is already in this row.')
        col_values = []
        for i in self.board:
            col_values.append(i[col - 1])
        if val in col_values:
            raise SudokuMoveError('That value is already in this column.')
        if col in range(1, 4):
            first_col = 0
            last_col = 3
        elif col in range(4, 7):
            first_col = 3
            last_col = 6
        elif col in range(7, 10):
            first_col = 6
            last_col = 9        
        if row in range(1, 4):
            first_row = 0
            last_row = 3
        elif row in range(4, 7):
            first_row = 3
            last_row = 6
        elif row in range(7, 10):
            first_row = 6
            last_row = 9
        box_lst = []
        for i in range(first_row, last_row):
            for j in range(first_col, last_col):
                box_lst.append(self.board[i][j])
        if val in box_lst:
            raise SudokuMoveError('That value is already in this box.')
        self.board[row - 1][col - 1] = val
        self.list_of_moves.append((row, col, val))

    def undo(self):
        '''This method removes the last entry in the stored list of moves and 
        erases the contents of the board at the coordinates of the last move.'''
        x = self.list_of_moves.pop()
        self.board[x[0] - 1][x[1] - 1] = 0

    def solve(self):
        '''This method handles user interaction. It runs an infinite loop in 
        which it asks the user for a command using raw_input, executes the
        command by calling one of the other methods, and then asks for another
        command. It understands the quit 'q' command, a three-digit sequence, 
        the undo 'u' command, and the save to file 's <filename>' command. Any 
        other command is treated as an error, and the solve method also raises
        a SudokuCommandError exception, giving the  bad command as an argument 
        to the exception. After every new move or undo command, the board is 
        printed via a call to the show method. The two kinds of exceptions that
        can be raised are also printed out along with an encouraging message.'''
        good = '123456789'
        while True:
            try:
                a = raw_input('Enter a command: ')
                if a == 'q':
                    print 'Thanks for playing! Hope you had fun.'
                    return
                elif a == 'u':
                    self.undo()
                    print 'The last move has been undone.'
                elif a[0] == 's' and len(a) > 2:
                    if a[1] == ' ':
                        self.save(a[2:])
                        print 'The board has been saved as ' + a[2:]
                elif a[0] in good and a[1] in good and a[2] in good:
                    self.move(int(a[0]), int(a[1]), int(a[2]))
                else:
                    raise SudokuCommandError(a)
                self.show()
            except SudokuCommandError, e:
                print str(e) + ' is not a valid command.'
            except SudokuMoveError, e:
                print str(e) + ' Please try again, you can do it!'

if __name__ == '__main__':
    s = Sudoku()
    while True:
        filename = raw_input('Enter the Sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e
    s.show()
    s.solve()