inp = list('         ') # input())
board = [[inp[0], inp[1], inp[2]], [inp[3], inp[4], inp[5]], [inp[6], inp[7], inp[8]]]
finished = False


def draw_board():
    print('---------')
    row = '| ' + board[0][0] + ' ' + board[0][1] + ' ' + board[0][2] + ' |'
    print(row)
    row = '| ' + board[1][0] + ' ' + board[1][1] + ' ' + board[1][2] + ' |'
    print(row)
    row = '| ' + board[2][0] + ' ' + board[2][1] + ' ' + board[2][2] + ' |'
    print(row)
    print('---------')


def evaluate():
    x_count = 0
    o_count = 0
    for i in inp:
        if i == 'X':
            x_count += 1
        if i == 'O':
            o_count += 1
    input_matrix = [''.join([board[0][0],board[0][1],board[0][2]]),''.join([board[1][0],board[1][1],board[1][2]]),''.join([board[2][0],board[2][1],board[2][2]])]
    input_matrix.append(''.join([board[0][0],board[1][0],board[2][0]]))
    input_matrix.append(''.join([board[0][1],board[1][1],board[2][1]]))
    input_matrix.append(''.join([board[0][2],board[1][2],board[2][2]]))
    input_matrix.append(''.join([board[0][0],board[1][1],board[2][2]]))
    input_matrix.append(''.join([board[2][0],board[1][1],board[0][2]]))
    x_win=False
    o_win=False
    has_empty=False
    mess = 'Error'
    if '_' in inp or ' ' in inp:
        has_empty=True
    if 'XXX' in input_matrix:
        x_win=True
    if 'OOO' in input_matrix:
        o_win=True
    if (x_win and o_win) or abs(x_count-o_count)>1:
        mess = 'Impossible'
    elif not x_win and not o_win and has_empty:
        return False
    elif not x_win and not o_win and not has_empty:
        mess = 'Draw'
    elif x_win and not o_win:
        mess = 'X wins'
    elif not x_win and o_win:
        mess = 'O wins'
    print(mess)
    return True


def get_coords():
    valid_input=False
    coord = ''
    coords = []
    while not valid_input:
        coord = input('?')
        coords = [i for i in coord.split()]
        if len(coords) == 2 and (coords[0] in ['0','1','2','3','4','5','6','7','8','9']) and (coords[1] in ['0','1','2','3','4','5','6','7','8','9']):
            coords = [int(i) for i in coord.split()]
            if coords[0] in [1,2,3] and coords[1] in [1,2,3]:
                target = board[3 - coords[1]][coords[0] -1]
                if target.lower() in ["x","o"]:
                    print("This cell is occupied! Choose another one!")
                else:
                    valid_input = True
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

    return coords


def make_move(coords):
    board[3 - coords[1]][coords[0] - 1] = "X"
    draw_board()

while not finished:
    draw_board()
    finished = evaluate()
    coords = get_coords()
    make_move(coords)
