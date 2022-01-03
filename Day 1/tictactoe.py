def main():
    moves = 0
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    print_board(board)
    while True:
        print('Player 1:')
        move = get_move(board)
        board[move[1]][move[0]] = 'X'
        moves += 1
        print_board(board)
        if moves == 9:
            print('Draw!')
            break
        if check_win(board, 'X'):
            print('Player 1 wins!')
            break
        print('Player 2:')
        move = get_move(board)
        board[move[1]][move[0]] = 'O'
        moves += 1
        print_board(board)
        if moves == 9:
            print('Draw!')
            break
        if check_win(board, 'O'):
            print('Player 2 wins!')
            break

def print_board(board):
    print('+ 0 1 2')
    for iteration, row in enumerate(board):
        print(str(iteration) + ' ' + ' '.join(row))

def get_move(board):
    while True:
        try:
            x = int(input('Enter horizontal number: '))
            y = int(input('Enter vertical number: '))
            if x < 0 or x > 2 or y < 0 or y > 2:
                print('Invalid move!')
            else:
                if board[y][x] != '-':
                    print("That space is already taken!")
                else:
                    return (x, y)
        except ValueError:
            print('Invalid move!')

def check_win(board, player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return Trueay 
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

main()
