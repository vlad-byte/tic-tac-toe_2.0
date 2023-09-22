from flask import Flask, render_template
import random
# -*- coding: utf-8 -*-


def dell(board):
    t = 0
    for i in range(len(board)):
        if board[i] == 'O':
            board = board[:i] + 'X' + board[i + 1:]
            if not is_winner(board, 'X'):
                best_move = i
                t = 1
            board = board[:i] + 'O' + board[i + 1:]
    if t == 0:
        valid_moves = [r for r in range(len(board)) if board[r] == 'O']
        row = random.choice(valid_moves)
        best_move = row
    return best_move


def dob(board):
    t = 0
    for i in range(len(board)):
        if board[i] == ' ':
            board = board[:i] + 'X' + board[i + 1:]
            if is_winner(board, 'X'):
                best_move = i
                t = 1
            board = board[:i] + 'O' + board[i + 1:]
            if is_winner(board, 'O'):
                best_move = i
                t = 1
            board = board[:i] + ' ' + board[i + 1:]
    if t == 0:
        valid_moves = [r for r in range(len(board)) if board[r] == ' ']
        row = random.choice(valid_moves)
        best_move = row
    return best_move


def is_winner(boa, player):
    size = int(len(boa)**0.5)
    board = [[' ' for _ in range(size)] for _ in range(size)]
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i][j] = boa[0]
            boa = boa[1:]
    for r1 in range(1, size - 1):
        for c1 in range(1, size - 1):
            if (board[r1][c1] == board[r1 - 1][c1 - 1] == board[r1 + 1][c1 + 1] == player) or (
                    board[r1][c1] == board[r1 - 1][c1 + 1] == board[r1 + 1][c1 - 1] == player):
                return True
    for r1 in range(size):
        for c1 in range(1, size - 1):
            if board[r1][c1] == board[r1][c1 - 1] == board[r1][c1 + 1] == player:
                return True
    for r1 in range(1, size - 1):
        for c1 in range(size):
            if board[r1][c1] == board[r1 - 1][c1] == board[r1 + 1][c1] == player:
                return True
    return False


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('lobby.html')


@app.route('/play3/<string:board>/<string:command>/<string:status>', methods=['GET', 'POST'])
def play3(board, command, status):
    pl1m = 3 - board.count('X')
    pl2m = 3 - board.count('O')
    if command == '0':
        obstacles = []
        for i in range(2):
            rr = random.randint(0, 4)
            while rr in obstacles:
                rr = random.randint(0, 4)
            obstacles.append(rr)
        for p in obstacles:
            board = board[:p] + '#' + board[p + 1:]
        return render_template('back3.html', board=board, command=command, status=status)
    com = int(command) - 1
    if status == 'Вы победили' or status == 'Компьютер победил':
        return render_template('back3.html', board=board, command=command, status=status)
    if board[com] == ' ' and pl1m > 0:
        board = board[:com] + 'X' + board[com + 1:]
        pl1m -= 1
        if is_winner(board, 'X'):
            return render_template('back3.html', board=board, command=command, status='Вы победили')
    elif board[com] == 'X':
        board = board[:com] + ' ' + board[com + 1:]
        pl1m += 1
    else:
        return render_template('back3.html', board=board, command=command, status='Выберите другое поле')
    if pl2m != 0:
        best = dob(board)
        row = best
        board = board[:row] + 'O' + board[row + 1:]
        pl2m -= 1
        if is_winner(board, 'O'):
            return render_template('back3.html', board=board, command=command, status='Компьютер победил')
    else:
        best = dell(board)
        row = best
        board = board[:row] + ' ' + board[row + 1:]
        pl2m += 1
    status = 'Ходов осталось: ' + str(pl1m)
    return render_template('back3.html', board=board, command=command, status=status)
# list = [["O","X"],["#"," "]], command = [0, 0], status = "&nbsp;"


@app.route('/play4/<string:board>/<string:command>/<string:status>', methods=['GET', 'POST'])
def play4(board, command, status):
    pl1m = 5 - board.count('X')
    pl2m = 5 - board.count('O')
    if command == '0':
        obstacles = []
        for i in range(4):
            rr = random.randint(0, 16)
            while rr in obstacles:
                rr = random.randint(0, 16)
            obstacles.append(rr)
        for p in obstacles:
            board = board[:p] + '#' + board[p + 1:]
        return render_template('back4.html', board=board, command=command, status=status)
    com = int(command) - 1
    if status == 'Вы победили' or status == 'Компьютер победил':
        return render_template('back4.html', board=board, command=command, status=status)
    if board[com] == ' ' and pl1m > 0:
        board = board[:com] + 'X' + board[com + 1:]
        pl1m -= 1
        if is_winner(board, 'X'):
            return render_template('back4.html', board=board, command=command, status='Вы победили')
    elif board[com] == 'X':
        board = board[:com] + ' ' + board[com + 1:]
        pl1m += 1
    else:
        return render_template('back4.html', board=board, command=command, status='Выберите другое поле')
    if pl2m != 0:
        best = dob(board)
        row = best
        board = board[:row] + 'O' + board[row + 1:]
        pl2m -= 1
        if is_winner(board, 'O'):
            return render_template('back4.html', board=board, command=command, status='Компьютер победил')
    else:
        best = dell(board)
        row = best
        board = board[:row] + ' ' + board[row + 1:]
        pl2m += 1
    status = 'Ходов осталось: ' + str(pl1m)
    return render_template('back4.html', board=board, command=command, status=status)


@app.route('/play5/<string:board>/<string:command>/<string:status>', methods=['GET', 'POST'])
def play5(board, command, status):
    pl1m = 7 - board.count('X')
    pl2m = 7 - board.count('O')
    if command == '0':
        obstacles = []
        for i in range(8):
            rr = random.randint(0, 25)
            while rr in obstacles:
                rr = random.randint(0, 25)
            obstacles.append(rr)
        for p in obstacles:
            board = board[:p] + '#' + board[p + 1:]
        return render_template('back5.html', board=board, command=command, status=status)
    com = int(command) - 1
    if status == 'Вы победили' or status == 'Компьютер победил':
        return render_template('back5.html', board=board, command=command, status=status)
    if board[com] == ' ' and pl1m > 0:
        board = board[:com] + 'X' + board[com + 1:]
        pl1m -= 1
        if is_winner(board, 'X'):
            return render_template('back5.html', board=board, command=command, status='Вы победили')
    elif board[com] == 'X':
        board = board[:com] + ' ' + board[com + 1:]
        pl1m += 1
    else:
        return render_template('back5.html', board=board, command=command, status='Выберите другое поле')
    if pl2m != 0:
        best = dob(board)
        row = best
        board = board[:row] + 'O' + board[row + 1:]
        pl2m -= 1
        if is_winner(board, 'O'):
            return render_template('back5.html', board=board, command=command, status='Компьютер победил')
    else:
        best = dell(board)
        row = best
        board = board[:row] + ' ' + board[row + 1:]
        pl2m += 1
    status = 'Ходов осталось: ' + str(pl1m)
    return render_template('back5.html', board=board, command=command, status=status)


if __name__ == '__main__':
    app.run()
