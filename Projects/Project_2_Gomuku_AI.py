"""Gomoku starter code 
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 28, 2022 

***must not use global variables***
***computer plays black stones; computer always moves first***

"""

def is_empty(board): 
    #check and stop once there's stone on the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                return False
    return True
    
def is_bounded(board, y_end, x_end, length, d_y, d_x): 
#analyses the sequence of length length that ends at location (y end, x end). The function returns "OPEN" if the sequence is open, "SEMIOPEN" if the sequence if semi-open, and "CLOSED" if the sequence is closed.

#assume that the sequence is complete and valid, and contains stones of only one colour

    # bool = True
    # 
    # for i in range(length):
    #     if board[y_end][x_end] != board[y_end - d_y * i][x_end - d_x * i]:
    #         bool = False
    # return bool

    #1. check if previous spot is empty
    if is_seq_in_board(board, y_end - d_y * (length), x_end - d_x * (length)):
        if board[y_end - d_y * (length)][x_end - d_x * (length)] == " ":
            if is_seq_in_board(board, y_end + d_y, x_end + d_x):                    
                if board[y_end + d_y][x_end + d_x] == " ":
                    return "OPEN"
    
    if is_seq_in_board(board, y_end - d_y * (length), x_end - d_x * (length)) or is_seq_in_board(board, y_end + d_y, x_end + d_x):
        if board[y_end - d_y * (length)][x_end - d_x * (length)] == " " or board[y_end + d_y][x_end + d_x] == " ":
            return "SEMIOPEN"
        
    if board[y_end - d_y * (length)][x_end - d_x * (length)] != board[y_end][x_end] or is_seq_in_board(board, y_end - d_y * (length + 1), x_end - d_x * (length)) or is_seq_in_board(board, y_end + d_y, x_end + d_x):
        return "CLOSED"
        
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
#The function returns a tuple whose first element is the number of open sequences of colour col of length length in the row R, and whose second element is the number of semi-open sequences of colour col of length length in the row R. 
#Assume that (y start,x start) is located on the edge of the board. Only complete sequences count.
#assume length is an integer greater or equal to 2

    open_seq_count = 0
    semi_open_seq_count = 0
    
    seq_start = []
    seq_end = []
    
    for a in range(len(board) - length + 1):
        # print("a:", a)
        state = True
        if is_seq_in_board(board, y_start + d_y * a, x_start + d_x * a):
            if board[y_start + d_y * a][x_start + d_x * a] == col:
                
                #check diagonal case:
                if d_y == 1 and d_x == -1 or d_y == 1 and d_x == 1:
                    if a >= len(board) - length:
                        # print("diagonal case")
                        break
                
                #check if any stone is different:
                if length == 2:
                    for b in range (length - 1):
                        # print("b:", b)
                        if board[y_start + d_y * (a + b)][x_start + d_x * (a + b)] != col:
                            # print("different")
                            state = False
    
                        if b == 0:
                            if is_seq_in_board(board, y_start + d_y * (a + 1), x_start + d_x * (a + 1)):
                                if board[y_start + d_y * (a + 1)][x_start + d_x * (a + 1)] != col or board[y_start + d_y * (a)][x_start + d_x * (a)] != col:
                                    # print("different")
                                    state = False
                        
                        if d_y == 1 and d_x == -1 or d_y == 1 and d_x == 1:
                            # print("sssssssssssssss")
                            if a > (len(board) - length - y_start):
                                # print("impossible")
                                state = False
                            if b - a + 1 != length:
                                if length == 2:
                                    # print("mismatch length")
                                    break
                                else:
                                    # print("length mismatch")
                                    state = False
                else:
                    for b in range (length):
                        # print("b:", b)
                        
                        if is_seq_in_board(board, y_start + d_y * (a + b), x_start + d_x * (a + b)):
                            if board[y_start + d_y * (a + b)][x_start + d_x * (a + b)] != col:
                                # print("different")
                                state = False
    
                        if b == 0:
                            if is_seq_in_board(board, y_start + d_y * (a + 1), x_start + d_x * (a + 1)):
                                if not d_y == 1 and d_x == -1:
                                    if board[y_start + d_y * (a + 1)][x_start + d_x * (a + 1)] != col or board[y_start + d_y * (a)][x_start + d_x * (a)] != col:
                                        # print("different")
                                        state = False
                        
                        if d_y == 1 and d_x == -1 or d_y == 1 and d_x == 1:
                            # print("diagonal")
                            if a > (len(board) - length - y_start):
                                # print("impossible")
                                state = False
                            if b - a + 1 != length:
                                if length == 2:
                                    # print("mismatch length")
                                    break
                                elif b + a - 1 == length:
                                    state = True
                                else:
                                    # print("length mismatch")
                                    state = False        
                        
                        if d_y == 1 and d_x == -1:
                            if is_seq_in_board(board, y_start + d_y * (a), x_start + d_x * (a)):
                                if board[y_start + d_y * (a)][x_start + d_x * (a)] != col:
                                    # print("a is", a, "b is", b)
                                    # print("different")
                                    state = False
                            elif is_seq_in_board(board, y_start + d_y * (a + b), x_start + d_x * (a + b)):
                                if board[y_start + d_y * (a + b)][x_start + d_x * (a + b)] != col:
                                    # print("a is", a, "b is", b)
                                    # print("different")
                                    state = False   
                                    
                            elif is_seq_in_board(board, y_start + d_y * (a + 1), x_start + d_x * (a + 1)):
                                if board[y_start + d_y * (a + 1)][x_start + d_x * (a + 1)] != col:
                                    # print("a is", a, "b is", b)
                                    # print("different")
                                    state = False   
                                
                #check if the previous stone is related
                if is_seq_in_board(board, y_start + d_y * (a - 1), x_start + d_x * (a - 1)):
                    if board[y_start + d_y * (a - 1)][x_start + d_x * (a - 1)] == col:
                        # print("previous")
                        state = False
                        
                #check if the next stone is related
                if is_seq_in_board(board, y_start + d_y * (a + length), x_start + d_x * (a + length)):
                    if board[y_start + d_y * (a + length)][x_start + d_x * (a + length)] == col:
                        # print("next")
                        state = False
                    
                if state:
                    if a == 0:
                        # print(a, length + a - 1)
                        seq_start.append(a)
                        seq_end.append(length - 1)
                    else:
                        # print(a, length + a - 1)
                        seq_start.append(a)
                        seq_end.append(length + a - 1)
                    
    for c in range(len(seq_start)):
        if is_bounded(board, y_start + d_y * seq_end[c], x_start + d_x * seq_end[c], length, d_y, d_x) == "OPEN":
            open_seq_count += 1
            c += 1
        else:
            if is_bounded(board, y_start + d_y * seq_end[c], x_start + d_x * seq_end[c], length, d_y, d_x) == "SEMIOPEN":
                semi_open_seq_count += 1
                c += 1
                    
        
    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length): 
#This function analyses the board board. The function returns a tuple, whose first element is the number of open sequences of colour col of length length on the entire board, and whose second element is the number of semi-open sequences of colour col of length length on the entire board.

#Only complete sequences count. For example, Fig. 1 is considered to contain one open row of length 3, and no other rows.
#Assume length is an integer greater or equal to 2.

    open_seq_count = 0
    semi_open_seq_count = 0
            
    #Rows
    for a in range(len(board)):
        # print("rows:", a)
        result = detect_row(board, col, a, 0, length, 0, 1)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]

    #Columns
    for b in range(len(board)):
        # print("columns:", b)
        result = detect_row(board, col, 0, b, length, 1, 0)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]

    #Diagonal (1, 1)
    for c in range(len(board) - length - 1):
        # print("1, 1 diagonal:", c)
        result = detect_row(board, col, 0, c, length, 1, 1)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]

    #Diagonal (1, -1)
    for d in range(len(board) - length - 1):
        # print("1, -1 diagonal:", d)
        result = detect_row(board, col, 0, d, length, 1, -1)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]
    
    for e in range(len(board) - length):
        # print("1, -1 diagonal bottom part:", e)
        result = detect_row(board, col, e, len(board) - 1, length, 1, -1)
        open_seq_count += result[0]
        semi_open_seq_count += result[1]

    return open_seq_count, semi_open_seq_count
    
def search_max(board): 
#uses the function score() to find the optimal move for black 
#finds the location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes the score of the board as calculated by score().
#The function returns a tuple (y, x) such that putting a black stone in coordinates (y, x) maximizes the potential score (if there are several such tuples, you can return any one of them). After the function returns, the contents of board must remain the same
                   
    import random
    move_y = int(random.random() * 10)
    move_x = int(random.random() * 10)
    max_score = score(board)
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                board[i][j] = "b"
                current_score = score(board)
                if current_score >= max_score:
                    max_score = current_score
                    move_y = i
                    move_x = j
                board[i][j] = " "

    return move_y, move_x
    
def score(board): 
#computes and returns the score for the position of the board
#assumes black has just moved
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board): # This function determines the current status of the game, and returns one of["White won", "Black won", "Draw", "Continue playing"]
                   #The only situation where "Draw" is returned is when board is full.
    for i in range(len(board)):
        for j in range(len(board)):
            if detect_rows(board, "w", 5)[0] or detect_rows(board, "w", 5)[1] >= 1:
                return "White Won"
            elif detect_rows(board, "b", 5)[0] or detect_rows(board, "b", 5)[1] >= 1:
                return "Black Won"
            elif board[i][j] != " ":
                return "Draw"
            else:
                return "Continue playing"


def print_board(board): #prints out the Gomoku board
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
            

def analysis(board): #analyses the position of the board by computing the number of open and semi-open sequences of both colours.
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
def play_gomoku(board_size): 
#allows the user to play against computer on a board of size board size × board size
#interacts with the AI engine by calling the function searchMax()
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
def is_seq_in_board(board, y, x):
    if y >= 0 and y <= len(board) - 1 and x >= 0 and x <= len(board) - 1:
        return True
    return False
    
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    # if not is_seq_in_board(board, y, x):
    #     return False
    # if board[y][x] != col:
    #     return False
    # for i in range(length):
    #     if board[y][x] == col:
    #         y += d_y
    #         x += d_x
    #     else:
    #         return False
    # return True
    
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    play_gomoku(8)
    
