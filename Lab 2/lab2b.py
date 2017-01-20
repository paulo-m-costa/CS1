# Paulo Costa - Lab 2 Part B

# Ex D.1:
def make_random_code():
    '''This function returns a string of four random characters from the list 
    'R','G','B','Y','O', and 'W'. Duplicate letters are allowed.'''
    import random
    code = ''
    for i in range(4):
        code += random.choice(['R', 'G', 'B', 'Y', 'O', 'W'])
    return code
# Ex D.2:
def count_exact_matches(s1, s2):
    '''This function takes two strings of length 4 as inputs and returns the 
    number of letters that are in the same locations in both strings.'''
    count = 0
    for i in range(4):
        if s1[i] == s2[i]:
            count += 1
    return count
# Ex D.3:
def count_letter_matches(s1, s2):
    '''This function takes two strings of length 4 as inputs and returns the 
    number of letters that are common between both strings.'''
    lst1 = list(s1)
    lst2 = list(s2)
    count = 0
    for i in range(len(lst1)):
        if lst1[i] in lst2:
            count += 1
            lst2.remove(lst1[i])
    return count         
# Ex D.4:
def compare_codes(code, guess):
    '''This function takes two strings of length 4 as inputs and returns a 
    string of length 4 consisting only of 'b', 'w', and '-' in that order. 
    'b' represents a black peg (exact match), 'w' represents a white peg 
    (correct letter, wrong location), and '-' represents a complete mismatch.'''
    b = count_exact_matches(code, guess)
    w = count_letter_matches(code, guess) - b
    blank = 4 - b - w
    s = ''
    for i in range(4):
        if b > 0:
            s += 'b'
            b -= 1
        elif w > 0:
            s += 'w'
            w -= 1
        else:
            s += '-'
            blank -= 1
    return s
# Ex D.5:
def run_game():
    '''This function uses the previous ones to generate a game of Mastermind
    and tells the user(s) how many moves it took for them to crack the code.'''
    print 'New game.'
    code = make_random_code()
    moves = 0
    while True:
        moves += 1
        guess = raw_input("Enter your guess: ")
        result_string = compare_codes(code, guess)
        print "Result: %s" % result_string
        if result_string == "bbbb":
            print "Congratulations! You cracked the code in %d moves!" %moves
            break