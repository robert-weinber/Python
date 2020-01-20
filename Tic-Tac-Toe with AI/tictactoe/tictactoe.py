import random
import copy
import sys

players = []
finished = False
inp = list('         ') # empty board
board = [[inp[0], inp[1], inp[2]], [inp[3], inp[4], inp[5]], [inp[6], inp[7], inp[8]]]
next_symbol = 'X' # X starts

def get_params(): # Gets starting commands
    while True:
        start_params = list(input('Input command:').split(' '))
        if start_params[0] == 'exit':
            sys.exit()
        if start_params[1] in ['user', 'easy', 'medium', 'hard'] and start_params[2] in ['user', 'easy', 'medium', 'hard'] and len(start_params) == 3:
            players = ['','']
            players[0] = start_params[1]
            players[1] = start_params[2]
            return players
        print('Bad parameters!')


def draw_board(target_board): # Draws the board on the console
    print('---------')
    row = '| ' + target_board[0][0] + ' ' + target_board[0][1] + ' ' + target_board[0][2] + ' |'
    print(row)
    row = '| ' + target_board[1][0] + ' ' + target_board[1][1] + ' ' + target_board[1][2] + ' |'
    print(row)
    row = '| ' + target_board[2][0] + ' ' + target_board[2][1] + ' ' + target_board[2][2] + ' |'
    print(row)
    print('---------')


def evaluate(target_board, calculating=False, hard=False): # evaluates the result of the step (Win, Lose, Draw, Continue)
    x_count = 0
    o_count = 0
    for part in target_board:
        for item in part:
            if item == 'X':
                x_count += 1
            if item == 'O':
                o_count += 1
    input_matrix = [''.join([target_board[0][0], target_board[0][1], target_board[0][2]]), ''.join([target_board[1][0], target_board[1][1], target_board[1][2]]),
                    ''.join([target_board[2][0], target_board[2][1], target_board[2][2]]), ''.join([target_board[0][0], target_board[1][0], target_board[2][0]]),
                    ''.join([target_board[0][1], target_board[1][1], target_board[2][1]]), ''.join([target_board[0][2], target_board[1][2], target_board[2][2]]),
                    ''.join([target_board[0][0], target_board[1][1], target_board[2][2]]), ''.join([target_board[2][0], target_board[1][1], target_board[0][2]])]
    x_win = False
    o_win = False
    has_empty = False
    mess = 'Error'
    for part in target_board:
        for item in part:
            if item in ['_', ' ']:
                has_empty = True
    if 'XXX' in input_matrix:
        x_win = True
    if 'OOO' in input_matrix:
        o_win = True
    if (x_win and o_win) or (abs(x_count - o_count) > 1 and not calculating) or (abs(x_count - o_count) > 1 and hard):
        mess = 'Impossible'
    elif not x_win and not o_win and has_empty:
        return False
        # mess = 'Game not finished'
    elif not x_win and not o_win and not has_empty:
        mess = 'Draw'
    elif x_win and not o_win:
        mess = 'X wins'
    elif not x_win and o_win:
        mess = 'O wins'
    if not calculating:
        print(mess)
    return mess


def get_coords(): # Gets user input for next step
    valid_input = False
    coords = []
    while not valid_input:
        coord = input('Enter the coordinates:')
        coords = [i for i in coord.split()]
        if len(coords) == 2 and (coords[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) and (coords[1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            coords = [int(i) for i in coord.split()]
            if coords[0] in [1, 2, 3] and coords[1] in [1, 2, 3]:
                target = board[3 - coords[1]][coords[0] - 1]
                if target.lower() in ["x", "o"]:
                    print("This cell is occupied! Choose another one!")
                else:
                    valid_input = True
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
    return [3 - coords[1],coords[0] - 1]


def get_bot_coords_easy(messaging = True): # Random steps on an empty cell
    if messaging:
        print('Making move level "easy"')
    valid_input = False
    coords = []
    while not valid_input:
        coords = [random.randint(0, 2), random.randint(0, 2)]
        target = board[coords[0]][coords[1]]
        if target.lower() not in ["x", "o"]:
            valid_input = True
    return coords


def get_bot_coords_medium(symbol): # Wins if can in 1 step and stop opponent from the same
    print('Making move level "medium"')
    my_symbol = symbol
    if symbol == 'X':
        enemy_symbol = 'O'
    if symbol == 'O':
        enemy_symbol = 'X'
    for i in range(3):
        for j in range(3):
            board_simulation = copy.deepcopy(board)
            if board_simulation[i][j] in ['_',' ']:
                board_simulation[i][j] = my_symbol
                if evaluate(board_simulation, True) == my_symbol + ' wins':
                    return [i, j]
                board_simulation[i][j] = enemy_symbol
                if evaluate(board_simulation, True) == enemy_symbol + ' wins':
                    return [i, j]

    return get_bot_coords_easy(False)


def get_bot_coords_hard(symbol): # Searching for the best possible action with minmax recursive
    print('Making move level "hard"')
    my_symbol = symbol
    if symbol == 'X':
        enemy_symbol = 'O'
    if symbol == 'O':
        enemy_symbol = 'X'
    result = []
    value_of_choice = []
    best_result = []
    best_value_of_choice = -10000
    for i in range(3):
        for j in range(3):
            if board[i][j] in [' ', '_']:
                board_simulation = copy.deepcopy(board)
                board_simulation[i][j] = my_symbol
                this_choice = minmax(board_simulation, my_symbol, my_symbol, 1)
                # print(this_choice)
                if this_choice > best_value_of_choice:
                    best_value_of_choice = this_choice
                    best_result = [i, j]
                value_of_choice.append(this_choice)
                result.append([i, j])
    if best_result == []:
        max_val = max(value_of_choice)
        max_val_index = value_of_choice.index(max_val)
        best_result = result[max_val_index]
    return best_result


def minmax(brd, my_symbol, curr_symbol, level): # Recursive search for the best action.
    if my_symbol == 'X':
        enemy_symbol = 'O'
    else:
        enemy_symbol = 'X'
    if curr_symbol == 'X':
        curr_symbol = 'O'
    else:
        curr_symbol = 'X'
    value_of_choice = 0
    eval = evaluate(brd, True, True)
    if eval == 'Impossible':
        return 0
    elif eval == my_symbol + ' wins':
        return 1000 / level ** level
    elif eval == enemy_symbol + ' wins':
        return -1000 / level ** level
    else:
       # value_of_choice += 0 / level
        for i in range(3):
            for j in range(3):
                if brd[i][j] in [' ', '_']:
                    board_simulation = copy.deepcopy(brd)
                    board_simulation[i][j] = curr_symbol
                    value_of_choice += minmax(board_simulation, my_symbol, curr_symbol, level + 1)
        return value_of_choice


def make_move(coords): # Changes the board and draws it
    board[coords[0]][coords[1]] = next_symbol
    draw_board(board)


players = get_params()
draw_board(board)
while True: # Game loop
    next_symbol = 'X'
    if players[0] == 'user':
        make_move(get_coords())
    if players[0] == 'easy':
        make_move(get_bot_coords_easy())
    if players[0] == 'medium':
        make_move(get_bot_coords_medium(next_symbol))
    if players[0] == 'hard':
        make_move(get_bot_coords_hard(next_symbol))
    if evaluate(board): # True if game over
        break
    next_symbol = 'O'
    if players[1] == 'user':
        make_move(get_coords())
    if players[1] == 'easy':
        make_move(get_bot_coords_easy())
    if players[1] == 'medium':
        make_move(get_bot_coords_medium(next_symbol))
    if players[1] == 'hard':
        make_move(get_bot_coords_hard(next_symbol))
    if evaluate(board): # True if game over
        break
