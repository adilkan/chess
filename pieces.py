from support import PieceDirections, PieceType, WHITE, BLACK


class Piece:
    def __init__(self, directions: tuple[int], piece_type: PieceType, color: int):
        self.directions = directions
        self.piece_type = piece_type
        self.color = color

    def get_under_attack(self, current_position, board):
        result = []
        '''TO DO save turn to optimize it and clean'''
        for row, col in self.directions:
            target_row, target_col = current_position
            while 0 <= target_row < 8 and 0 <= target_col < 8:
                target_row, target_col = target_row + row, target_col + col

                if 0 > target_row or target_row >= 8 or 0 > target_col or target_col >= 8:
                    break

                piece = board[target_row][target_col]
                if piece and piece.color == self.color:
                    break

                result.append((target_row, target_col))

                if piece and piece.piece_type != self.color:
                    break

                if self.piece_type == PieceType.KING or self.piece_type == PieceType.KNIGHT:
                    break

        return result

    def is_check_for_me(self, board):
        '''TO DO optimize it'''
        for row in range(8):
            for col in range(8):
                piece = board[row][col]

                if not piece or piece.color == self.color:
                    continue

                piece_under_attack = piece.get_under_attack((row, col), board)
                for attack_row, attack_col in piece_under_attack:
                    attacked_piece = board[attack_row][attack_col]
                    if (attacked_piece and attacked_piece.color == self.color and
                            attacked_piece.piece_type == PieceType.KING):
                        return True
        return False

    def move(self, current_position, target_position, current_value, target_value, board):
        cur_row, cur_col = current_position
        target_row, target_col = target_position
        board[cur_row][cur_col] = current_value
        board[target_row][target_col] = target_value
        return board

    def get_valid_moves(self, current_position, board):
        under_attack = self.get_under_attack(current_position, board)
        result = []

        for target_position in under_attack:

            target_row, target_col = target_position
            prev_val = board[target_row][target_col]

            self.move(current_position, target_position, None, self, board)

            check_after_move = self.is_check_for_me(board)

            self.move(target_position, current_position, prev_val, self, board)

            if not check_after_move:
                result.append(target_position)

        return result

    def __str__(self):
        return self.piece_type.value

    def __repr__(self):
        return self.__str__()


class King(Piece):
    def __init__(self, color: int):
        super().__init__(PieceDirections.KING_MOVE.value, PieceType.KING, color)


class Queen(Piece):
    def __init__(self, color: int):
        super().__init__(PieceDirections.QUEEN_MOVE.value, PieceType.QUEEN, color)


class Rook(Piece):
    def __init__(self, color: int):
        super().__init__(PieceDirections.ROOK_MOVE.value, PieceType.ROOK, color)


class Bishop(Piece):
    def __init__(self, color: int):
        super().__init__(PieceDirections.BISHOP_MOVE.value, PieceType.BISHOP, color)


class Knight(Piece):
    def __init__(self, color: int):
        super().__init__(PieceDirections.KNIGHT_MOVE.value, PieceType.KNIGHT, color)


class Pawn(Piece):
    def __init__(self, color: int):
        super().__init__(PieceDirections.PAWN_WHITE_MOVE.value, PieceType.PAWN, color)
        '''TO DO full pawn functionality'''


king_w = King(WHITE)
king_b = King(BLACK)

queen_w = Queen(WHITE)
queen_b = Queen(BLACK)

bishop_w = Bishop(WHITE)
bishop_b = Bishop(BLACK)

knight_w = Knight(WHITE)
knight_b = Knight(BLACK)

rook_w = Rook(WHITE)
rook_b = Rook(BLACK)

pawn_w = Pawn(WHITE)
pawn_b = Pawn(BLACK)
