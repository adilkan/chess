from pieces import *


class Board:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]  # Создаем пустую доску 8x8
        self.count_move = 1
        self.sub_move = 0
        self.turn = WHITE
        self.valid_moves = {}

    def update_valid_moves_for_turn(self):
        result = {}
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if not piece or piece.color != self.turn:
                    continue

                current_position = (row, col)
                piece_valid_moves = piece.get_valid_moves(current_position, self.board)
                if piece_valid_moves:
                    result[current_position] = piece_valid_moves

        self.valid_moves = result

    def count_moves(self):
        self.sub_move += 1

        if self.sub_move == 2:
            self.count_move += 1
            self.sub_move = 0

    def move(self, current_position: tuple, target_position: tuple) -> bool:
        '''TO DO save all move and allow to see prev moves and treis of moves etc and make a converter'''

        if target_position not in self.valid_moves.get(current_position, []):
            return False
        current_row, current_col = current_position
        piece = self.board[current_row][current_col]
        piece.move(current_position, target_position, None, piece, self.board)

        self.count_moves()
        self.turn = self.sub_move

        self.update_valid_moves_for_turn()

        return True

    def print_board(self):
        for i in self.board:
            print(i)

    def set_default_board(self):
        '''to do  make more clean'''
        self.board[7][0] = rook_w
        self.board[7][1] = knight_w
        self.board[7][2] = bishop_w
        self.board[7][3] = queen_w
        self.board[7][4] = king_w
        self.board[7][5] = bishop_w
        self.board[7][6] = knight_w
        self.board[7][7] = rook_w
        self.board[6] = [pawn_w] * 8

        self.board[0][0] = rook_b
        self.board[0][1] = knight_b
        self.board[0][2] = bishop_b
        self.board[0][3] = queen_b
        self.board[0][4] = king_b
        self.board[0][5] = bishop_b
        self.board[0][6] = knight_b
        self.board[0][7] = rook_b
        self.board[1] = [pawn_b] * 8

    def play(self):
        '''просто чтоб можно было потыкаться'''
        '''
            чтобы играть надо писать индексы фигуры которую хочешь подвинуть и  куда через пробел
            пример:
            6 0 5 0
        '''

        while True:
            self.update_valid_moves_for_turn()
            print(self.turn)
            self.print_board()

            c_row, c_col, t_row, t_col = map(int, input().split())

            self.move((c_row, c_col), (t_row, t_col))

board = Board()
board.set_default_board()
board.play()
