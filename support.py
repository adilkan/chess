from enum import Enum

WHITE = 0
BLACK = 1


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (-1, 1)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)
    KNIGHT_MOVE_1 = (2, 1)
    KNIGHT_MOVE_2 = (1, 2)
    KNIGHT_MOVE_3 = (-1, 2)
    KNIGHT_MOVE_4 = (-2, 1)
    KNIGHT_MOVE_5 = (-2, -1)
    KNIGHT_MOVE_6 = (-1, -2)
    KNIGHT_MOVE_7 = (1, -2)
    KNIGHT_MOVE_8 = (2, -1)


class PieceType(Enum):
    KING = 'KING'
    PAWN = 'PAWN'
    KNIGHT = 'KNIGHT'
    BISHOP = 'BISHOP'
    ROOK = 'ROOK'
    QUEEN = 'QUEEN'


class PieceDirections(Enum):
    KING_MOVE = (Direction.UP.value, Direction.DOWN.value, Direction.LEFT.value, Direction.RIGHT.value,
                 Direction.UP_LEFT.value, Direction.UP_RIGHT.value, Direction.DOWN_LEFT.value,
                 Direction.DOWN_RIGHT.value)
    '''NOT FULL MOVES FOR PAWNS'''
    PAWN_WHITE_MOVE = (Direction.UP.value,)
    PAWN_BLACK_MOVE = (Direction.DOWN.value,)
    KNIGHT_MOVE = (Direction.KNIGHT_MOVE_1.value, Direction.KNIGHT_MOVE_2.value, Direction.KNIGHT_MOVE_3.value,
                   Direction.KNIGHT_MOVE_4.value, Direction.KNIGHT_MOVE_5.value, Direction.KNIGHT_MOVE_6.value,
                   Direction.KNIGHT_MOVE_7.value, Direction.KNIGHT_MOVE_8.value)
    BISHOP_MOVE = (Direction.UP_LEFT.value, Direction.UP_RIGHT.value, Direction.DOWN_LEFT.value,
                   Direction.DOWN_RIGHT.value)
    ROOK_MOVE = (Direction.UP.value, Direction.DOWN.value, Direction.LEFT.value, Direction.RIGHT.value)
    QUEEN_MOVE = KING_MOVE

