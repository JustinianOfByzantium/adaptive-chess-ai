import numpy as np
from game_logic import *

def full_game():
    print("\n\n---Running test full_game--- \n ")

    active_game = Game([])

    white_a_pawn = Pawn(active_game, white, 2, a)
    white_b_pawn = Pawn(active_game, white, 2, b)
    white_c_pawn = Pawn(active_game, white, 2, c)
    white_d_pawn = Pawn(active_game, white, 2, d)
    white_e_pawn = Pawn(active_game, white, 2, e)
    white_f_pawn = Pawn(active_game, white, 2, f)
    white_g_pawn = Pawn(active_game, white, 2, g)
    white_h_pawn = Pawn(active_game, white, 2, h)
    white_queenside_rook = Rook(active_game, white, 1, a)
    white_kingside_rook = Rook(active_game, white, 1, h)
    white_queenside_knight = Knight(active_game, white, 1, b)
    white_kingside_knight = Knight(active_game, white, 1, g)
    white_dark_square_bishop = Bishop(active_game, white, 1, c)
    white_light_square_bishop = Bishop(active_game, white, 1, f)
    white_queen = Queen(active_game, white, 1, d)
    white_king = King(active_game, white, 1, e)


    black_a_pawn = Pawn(active_game, black, 7, a)
    black_b_pawn = Pawn(active_game, black, 7, b)
    black_c_pawn = Pawn(active_game, black, 7, c)
    black_d_pawn = Pawn(active_game, black, 7, d)
    black_e_pawn = Pawn(active_game, black, 7, e)
    black_f_pawn = Pawn(active_game, black, 7, f)
    black_g_pawn = Pawn(active_game, black, 7, g)
    black_h_pawn = Pawn(active_game, black, 7, h)
    black_queenside_rook = Rook(active_game, black, 8, a)
    black_kingside_rook = Rook(active_game, black, 8, h)
    black_queenside_knight = Knight(active_game, black, 8, b)
    black_kingside_knight = Knight(active_game, black, 8, g)
    black_light_square_bishop = Bishop(active_game, black, 8, c)
    black_dark_square_bishop = Bishop(active_game, black, 8, f)
    black_queen = Queen(active_game, black, 8, d)
    black_king = King(active_game, black, 8, e)


    chess_board = np.full([8,8], dtype = Chess_Piece, fill_value=None)
    chess_board[7] = [black_queenside_rook, black_queenside_knight, black_light_square_bishop, black_queen, black_king, black_dark_square_bishop, black_kingside_knight, black_kingside_rook]
    chess_board[6] = [black_a_pawn, black_b_pawn, black_c_pawn, black_d_pawn, black_e_pawn, black_f_pawn, black_g_pawn, black_h_pawn]
    chess_board[1] = [white_a_pawn, white_b_pawn, white_c_pawn, white_d_pawn, white_e_pawn, white_f_pawn, white_g_pawn, white_h_pawn]
    chess_board[0] = [white_queenside_rook, white_queenside_knight, white_light_square_bishop, white_queen, white_king, white_dark_square_bishop, white_kingside_knight, white_kingside_rook]

    active_game.board = chess_board
    print_board(chess_board)

def rook_basic_moves():
    print("\n ---Running test rook_basic_moves--- \n")
    active_game = Game([])
    chess_board = np.full([8,8], dtype = Chess_Piece, fill_value=None)

    white_kingside_rook = Rook(active_game, white, 4, e)
    chess_board[3, e] = white_kingside_rook

    active_game.board = chess_board

    print_board(chess_board)

    print("Testing horizontal moves")

    print("Moving rook from e4 to h4")
    white_kingside_rook.try_move(h, 4)
    print_board(chess_board)

    print("Moving rook from h4 to b4")
    white_kingside_rook.try_move(b, 4)
    print_board(chess_board)

    print("Testing vertical moves")

    print("Moving rook from b4 to b7")
    white_kingside_rook.try_move(b, 7)
    print_board(chess_board)

    print("Moving rook from b7 to b2")
    white_kingside_rook.try_move(b, 2)
    print_board(chess_board)

    print("Testing invalid moves")

    print("Moving rook from b7 to h3")
    white_kingside_rook.try_move(h, 3)
    print_board(chess_board)

    print("Moving rook from b7 to c6")
    white_kingside_rook.try_move(c, 6)
    print_board(chess_board)

def bishop_basic_moves():
    print("\n ---Running test bishop_basic_moves--- \n")
    active_game = Game([])
    chess_board = np.full([8,8], dtype = Chess_Piece, fill_value=None)

    white_bishop = Bishop(active_game, white, 4, e)
    chess_board[3, e] = white_bishop

    active_game.board = chess_board

    print_board(chess_board)

    print("Testing diagonal moves")

    print("Moving bishop from e4 to h7")
    white_bishop.try_move(h, 7)
    print_board(chess_board)

    print("Moving bishop from h7 to c2")
    white_bishop.try_move(c, 2)
    print_board(chess_board)

    print("Testing invalid moves")

    print("Moving bishop from c2 to b5")
    white_bishop.try_move(b, 5)
    print_board(chess_board)

    print("Moving bishop from c2 to c4")
    white_bishop.try_move(c, 4)
    print_board(chess_board)

def knight_basic_moves():
    print("\n ---Running test knight_basic_moves--- \n")
    active_game = Game([])
    chess_board = np.full([8,8], dtype = Chess_Piece, fill_value=None)

    white_knight = Knight(active_game, white, 4, e)
    chess_board[3, e] = white_knight

    active_game.board = chess_board

    print_board(chess_board)

    print("Testing L-shaped moves")

    print("Moving knight from e4 to f6")
    white_knight.try_move(f, 6)
    print_board(chess_board)

    print("Moving knight from f6 to d5")
    white_knight.try_move(d, 5)
    print_board(chess_board)

    print("Testing invalid moves")

    print("Moving knight from d5 to d7")
    white_knight.try_move(d, 7)
    print_board(chess_board)

    print("Moving knight from d5 to e5")
    white_knight.try_move(e, 5)
    print_board(chess_board)

def queen_basic_moves():
    print("\n ---Running test queen_basic_moves--- \n")
    active_game = Game([])
    chess_board = np.full([8,8], dtype = Chess_Piece, fill_value=None)

    white_queen = Queen(active_game, white, 4, e)
    chess_board[3, e] = white_queen

    active_game.board = chess_board

    print_board(chess_board)

    print("Testing diagonal moves")

    print("Moving queen from e4 to g6")
    white_queen.try_move(g, 6)
    print_board(chess_board)

    print("Moving queen from g6 to e8")
    white_queen.try_move(e, 8)
    print_board(chess_board)

    print("Testing straight moves")

    print("Moving queen from e8 to a8")
    white_queen.try_move(a, 8)
    print_board(chess_board)

    print("Moving queen from a8 to a1")
    white_queen.try_move(a, 1)
    print_board(chess_board)

    print("Testing invalid moves")

    print("Moving queen from a1 to g6")
    white_queen.try_move(g, 6)
    print_board(chess_board)

def king_basic_moves():
    print("\n ---Running test king_basic_moves--- \n")
    active_game = Game([])
    chess_board = np.full([8,8], dtype = Chess_Piece, fill_value=None)

    white_king = King(active_game, white, 4, e)
    chess_board[3, e] = white_king

    active_game.board = chess_board

    print_board(chess_board)

    print("Testing single square moves")

    print("Moving king from e4 to e5")
    white_king.try_move(e, 5)
    print_board(chess_board)

    print("Moving king from e5 to d5")
    white_king.try_move(d, 5)
    print_board(chess_board)

    print("Moving king from d5 to d4")
    white_king.try_move(d, 4)
    print_board(chess_board)

    print("Testing invalid moves")

    print("Moving king from d4 to f6")
    white_king.try_move(f, 6)
    print_board(chess_board)


def test_white_pawn_basic_moves(capsys):
    active_game = Game([])
    chess_board = np.full([8,8], dtype=Chess_Piece, fill_value=None)
    white_pawn = Pawn(active_game, white, 2, e)
    chess_board[1, e] = white_pawn
    active_game.board = chess_board

    # Test initial double move
    white_pawn.try_move(e, 4)
    assert active_game.board[3, e] == white_pawn
    assert active_game.board[1, e] is None

    # Test single move forward
    white_pawn.try_move(e, 5)
    assert active_game.board[4, e] == white_pawn
    assert active_game.board[3, e] is None

    # Test invalid move (moving sideways)
    white_pawn.try_move(f, 6)
    assert active_game.board[4, e] == white_pawn  # Should not move

def test_black_pawn_basic_moves(capsys):
    active_game = Game([])
    chess_board = np.full([8,8], dtype=Chess_Piece, fill_value=None)
    black_pawn = Pawn(active_game, black, 7, d)
    chess_board[6, d] = black_pawn
    active_game.board = chess_board

    # Test initial double move
    black_pawn.try_move(d, 5)
    assert active_game.board[4, d] == black_pawn
    assert active_game.board[6, d] is None

    # Test single move forward
    black_pawn.try_move(d, 4)
    assert active_game.board[3, d] == black_pawn
    assert active_game.board[4, d] is None

    # Test invalid move (moving sideways)
    black_pawn.try_move(c, 3)
    assert active_game.board[3, d] == black_pawn  # Should not move

def test_white_pawn_basic_moves():
    active_game = Game([])
    chess_board = np.full([8,8], dtype=Chess_Piece, fill_value=None)
    white_pawn = Pawn(active_game, white, 2, e)
    chess_board[1, e] = white_pawn
    active_game.board = chess_board

    print_board(chess_board)


    # Test initial double move
    white_pawn.try_move(e, 4)
    assert active_game.board[3, e] == white_pawn
    assert active_game.board[1, e] is None

    print_board(chess_board)

    # Test single move forward
    white_pawn.try_move(e, 5)
    assert active_game.board[4, e] == white_pawn
    assert active_game.board[3, e] is None

    print_board(chess_board)

    


    # Test invalid move (moving sideways)
    white_pawn.try_move(f, 6)
    assert active_game.board[4, e] == white_pawn  # Should not move

    print_board(chess_board)

    # Test invalid move (moving twice after first move)
    white_pawn.try_move(e, 7)

    print_board(chess_board)


def test_black_pawn_basic_moves():
    active_game = Game([])
    chess_board = np.full([8,8], dtype=Chess_Piece, fill_value=None)
    black_pawn = Pawn(active_game, black, 7, d)
    chess_board[6, d] = black_pawn
    active_game.board = chess_board

    print_board(chess_board)


    # Test initial double move
    black_pawn.try_move(d, 5)
    assert active_game.board[4, d] == black_pawn
    assert active_game.board[6, d] is None

    print_board(chess_board)

    # Test single move forward
    black_pawn.try_move(d, 4)
    assert active_game.board[3, d] == black_pawn
    assert active_game.board[4, d] is None

    print_board(chess_board)

    # Test invalid move (moving sideways)
    black_pawn.try_move(c, 3)
    assert active_game.board[3, d] == black_pawn  # Should not move

    print_board(chess_board)

def test_collisions():
    print("\n ---Running test queen_basic_moves--- \n")
    active_game = Game([])
    chess_board = np.full([8,8], dtype = Chess_Piece, fill_value=None)

    white_queen = Queen(active_game, white, 4, e)
    white_rook = Rook(active_game, white, 6, e)
    black_rook = Rook(active_game, black, 2, e)
    white_pawn = Pawn(active_game, white, 5, d)
    black_pawn = Pawn(active_game, black, 7, h)
    chess_board[3, e] = white_queen
    chess_board[5, e] = white_rook
    chess_board[1, e] = black_rook
    chess_board[4, d] = white_pawn
    chess_board[6, h] = black_pawn

    active_game.board = chess_board

    print_board(chess_board)

    # print("Trying to move queen from e4 to e1 (invalid move)")
    # white_queen.try_move(e, 1)
    
    # print_board(chess_board)

    # print("Trying to move queen from e4 to e6 (invalid move)")
    # white_queen.try_move(e, 6)

    # print_board(chess_board)

    print("Trying to move queen from e4 to c6 (invalid move)")
    white_queen.try_move(c, 6)

    print_board(chess_board)

    print("Trying to capture black piece on h7 (valid move)")
    white_queen.try_move(h, 7)
    print_board(chess_board)