import numpy as np
from macros import *
from game_logic import *
import game_logic_tests
from game_text import *

def init():
    active_game = Game()
    active_pieces = []

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

    active_pieces.extend(chess_board[7])
    active_pieces.extend(chess_board[6])
    active_pieces.extend(chess_board[1])
    active_pieces.extend(chess_board[0])
    active_game.active_pieces = np.array(active_pieces, dtype = Chess_Piece)
    active_game.board = chess_board
    print_board(chess_board)

    print("Testing basic moves")

    white_e_pawn.try_move(e, 4)
    black_c_pawn.try_move(c, 5)
    white_kingside_knight.try_move(f, 3)
    black_d_pawn.try_move(d, 6)
    white_d_pawn.try_move(d, 4)
    black_c_pawn.try_move(d, 4)
    white_kingside_knight.try_move(d, 4)
    black_kingside_knight.try_move(f, 6)
    white_kingside_knight.try_move(c, 3)
    black_g_pawn.try_move(g, 6)
    white_dark_square_bishop.try_move(e, 3)
    black_dark_square_bishop.try_move(g, 7)
    white_queen.try_move(d, 2)
    black_king.try_move(g, 8)
    white_king.try_move(c, 1)
    black_kingside_rook.try_move(e,8)


    print_board(chess_board)






if __name__ == "__main__":
    print("hello")
    # init()
    # game_logic_tests.rook_basic_moves()

    # game_logic_tests.bishop_basic_moves()
    # game_logic_tests.queen_basic_moves()
    # game_logic_tests.king_basic_moves()
    # game_logic_tests.pawn_basic_moves()
    # game_logic_tests.knight_basic_moves()
    # game_logic_tests.test_black_pawn_basic_moves()
    # game_logic_tests.test_white_pawn_basic_moves()
    # game_logic_tests.test_collisions()
    # game_logic_tests.test_white_pawn_en_passant()
    # game_logic_tests.test_castling_after_king_moves()
    # game_logic_tests.test_castling_after_rook_moves()
    # game_logic_tests.test_castling_blocked()
    # game_logic_tests.test_white_kingside_castling()
    # game_logic_tests.test_white_queenside_castling()
    # game_logic_tests.test_check()
    # game_logic_tests.test_knight_check()
    # game_logic_tests.test_castling_through_check()
    
    
    play_game()

    # test_move_str1 = "e4!!"
    # print(remove_annotations(test_move_str1))

    # test_move_str2 = "O-O-O?!"
    # print(remove_annotations(test_move_str2))

    # test_move_str3 = "a6#"
    # print(remove_annotations(test_move_str3))



