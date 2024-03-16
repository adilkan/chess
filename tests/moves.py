from unittest import TestCase

from board import Board


class ChessTestCase(TestCase):
    def setup_board(self):
        board = Board()
        board.set_default_board()
        return board


class PiecesTestCase(ChessTestCase):

    def test_king(self):
        board = self.setup_board()
        board.update_valid_moves_for_turn()

        assert board.valid_moves.get((7, 4)) == None

        board.board[7][3] = None
        board.board[7][3] = None
        board.update_valid_moves_for_turn()

        assert board.valid_moves[(7, 4)] == [(7, 3)]


class MovesCleanBoardTestCase(ChessTestCase):

    def test_king(self):
        board = self.setup_board()
        board.update_valid_moves_for_turn()
