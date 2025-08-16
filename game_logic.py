import numpy as np
from macros import *

# Static Functions 

"""
Returns the first piece encounter along rank
Gets called with rank1 = starting rank, rank2 = destination rank
:param direction: 1 = Going right, 0 = Going left
"""
def scan_rank(board, rank, old_file, new_file, direction: int, include_ends = False, target_piece_type = None, target_piece_color = black):
    range_dir = 1 if direction else -1
    displ = abs(new_file - old_file)

    start = old_file + range_dir - (include_ends * range_dir)
    end = new_file + (include_ends * range_dir)
    print(start, end)
    for file in range(start, end, range_dir):
        if file < 0 or file > 7:
            return None
        
        candidate_piece = board[rank, file]
        if candidate_piece is not None:
            # print(rank, file)
            # print(target_piece_type)
            # print(type(candidate_piece))
            # print("---")
            # print(target_piece_color)
            # print(candidate_piece.color)
            if target_piece_type is None or (type(candidate_piece) == target_piece_type and candidate_piece.color == target_piece_color):
                return candidate_piece
    return None

"""
Checks if pieces block squares in between self and final destination along rank
Gets called with rank1 = starting rank, rank2 = destination rank
:param direction: 1 = Going up, 0 = Going down, -1 = scan entire file
"""
def scan_file(board, old_rank, new_rank, file, direction: int, include_ends = False, target_piece_type = None, target_piece_color = black):
    range_dir = 1 if direction == 1 else -1

    displ = abs(new_rank - old_rank)

    start = old_rank + range_dir - (include_ends * range_dir)
    end = new_rank + (include_ends * range_dir)
    for rank in range(start, end, range_dir):
        if rank < 0 or rank > 7:
            return None
        
        candidate_piece = board[rank, file]
        if candidate_piece is not None:
            # print(rank, file)
            # print(target_piece_type)
            # print(type(candidate_piece))
            # print("---")
            # print(target_piece_color)
            # print(candidate_piece.color)
            if target_piece_type is None or (type(candidate_piece) == target_piece_type and candidate_piece.color == target_piece_color):
                return candidate_piece
    return None

"""
:param file_dir: 1 = Going up, 0 = Going down
:param rank_dir: 1 = Going right, 0 = Going left

"""
def scan_diag(board, old_rank, old_file, step: int, file_dir: int, rank_dir, include_ends = False, target_piece_type = None, target_piece_color = black):
    file_range_dir = 1 if file_dir else -1
    rank_range_dir = 1 if rank_dir else -1
    # print("file_range_dir: ", file_range_dir)
    # print("rank_range_dir: ", rank_range_dir)
    # print("old_file: ", old_file)
    # print("old_rank: ", old_rank)
    # print("step: ", step)
    h_step = step * rank_range_dir
    f_traversed = 1

    start = old_file + rank_range_dir - (include_ends * rank_range_dir)
    end =  old_file + h_step + (include_ends * rank_range_dir)
    for file in range(start, end, rank_range_dir):
        rank = old_rank + file_range_dir * f_traversed
        # print("Currently scanning the square: ", file, ", ", rank)
        if file < 0 or file > 7 or rank < 0 or rank > 7:
            return None
        
        candidate_piece = board[rank, file]
        if candidate_piece is not None:
            if target_piece_type is None or (type(candidate_piece) == target_piece_type and candidate_piece.color == target_piece_color):
                return candidate_piece
        f_traversed += 1
            
    return None

# Classes

class Game:
    def __init__(self, game_pieces: np.ndarray = [], default_board = False):
        self.board = np.empty([8,8], dtype=object)

        self.turn = white
        self.en_passant_square = None
        self.black_in_check = False
        self.white_in_check = False
        self.b_kingside_castle_rights = True
        self.b_queenside_castle_rights = True
        self.w_kingside_castle_rights = True
        self.w_queenside_castle_rights = True
        self.b_king_pos = (7, e)
        self.w_king_pos = (0, e)
        self.active_pieces = game_pieces
        self.captured_pieces = np.array([], dtype=object)

    
        # 0: normal
        # 1: white castle kingside
        # 2: white castle queenside
        # 3: white en-passant
        # 4: white pawn promotion
        # 5: black castle kingside
        # 6: black castle queenside
        # 7: black en-passant
        # 8: black pawn promotion
        # 9: castle part 2
        self.last_move_type = NORMAL


        if (default_board):
            white_a_pawn = Pawn(self, white, 2, a)
            white_b_pawn = Pawn(self, white, 2, b)
            white_c_pawn = Pawn(self, white, 2, c)
            white_d_pawn = Pawn(self, white, 2, d)
            white_e_pawn = Pawn(self, white, 2, e)
            white_f_pawn = Pawn(self, white, 2, f)
            white_g_pawn = Pawn(self, white, 2, g)
            white_h_pawn = Pawn(self, white, 2, h)
            white_queenside_rook = Rook(self, white, 1, a)
            white_kingside_rook = Rook(self, white, 1, h)
            white_queenside_knight = Knight(self, white, 1, b)
            white_kingside_knight = Knight(self, white, 1, g)
            white_dark_square_bishop = Bishop(self, white, 1, c)
            white_light_square_bishop = Bishop(self, white, 1, f)
            white_queen = Queen(self, white, 1, d)
            white_king = King(self, white, 1, e)


            black_a_pawn = Pawn(self, black, 7, a)
            black_b_pawn = Pawn(self, black, 7, b)
            black_c_pawn = Pawn(self, black, 7, c)
            black_d_pawn = Pawn(self, black, 7, d)
            black_e_pawn = Pawn(self, black, 7, e)
            black_f_pawn = Pawn(self, black, 7, f)
            black_g_pawn = Pawn(self, black, 7, g)
            black_h_pawn = Pawn(self, black, 7, h)
            black_queenside_rook = Rook(self, black, 8, a)
            black_kingside_rook = Rook(self, black, 8, h)
            black_queenside_knight = Knight(self, black, 8, b)
            black_kingside_knight = Knight(self, black, 8, g)
            black_light_square_bishop = Bishop(self, black, 8, c)
            black_dark_square_bishop = Bishop(self, black, 8, f)
            black_queen = Queen(self, black, 8, d)
            black_king = King(self, black, 8, e)


            chess_board = np.full([8,8], dtype = Chess_Piece, fill_value=None)
            chess_board[7] = [black_queenside_rook, black_queenside_knight, black_light_square_bishop, black_queen, black_king, black_dark_square_bishop, black_kingside_knight, black_kingside_rook]
            chess_board[6] = [black_a_pawn, black_b_pawn, black_c_pawn, black_d_pawn, black_e_pawn, black_f_pawn, black_g_pawn, black_h_pawn]
            chess_board[1] = [white_a_pawn, white_b_pawn, white_c_pawn, white_d_pawn, white_e_pawn, white_f_pawn, white_g_pawn, white_h_pawn]
            chess_board[0] = [white_queenside_rook, white_queenside_knight, white_light_square_bishop, white_queen, white_king, white_dark_square_bishop, white_kingside_knight, white_kingside_rook]

            self.active_pieces.extend(chess_board[7])
            self.active_pieces.extend(chess_board[6])
            self.active_pieces.extend(chess_board[1])
            self.active_pieces.extend(chess_board[0])
            self.active_pieces = np.array(self.active_pieces, dtype = Chess_Piece)
            self.board = chess_board

        

class Chess_Piece:
    def __init__(self, m_game: Game, color: bool, rank: int, file: int):
        self.m_game = m_game
        self.color = color
        self.rank = rank - 1
        self.file = file

    
    """
    Verifies that move is playable. Later, may add flag that specifies in what context this function was
    called: in order to make a move, or to check if a move is possible in some other context
    """
    def check_valid_move(self, new_rank: int, new_file: int) -> bool:
        pass

    def calc_horizontal_direction(self, old_file, new_file) -> bool:
        # print("calc_horizontal_direction called with old_file: ", old_file, " new_file: ", new_file)
        # res = new_file > old_file
        # if (res):
        #     print("Result: Going right")
        # else:
        #     print("Result: Going left")
        return new_file > old_file
        
    def calc_vertical_direction(self, old_rank, new_rank) -> bool:
        # print("calc_vertical_direction called with old_rank: ", old_rank, " new_rank: ", new_rank)
        # res = new_rank > old_rank
        # if (res):
        #     print("Result: going up")
        # else:
        #     print("Result: going down")
        return new_rank > old_rank

        

    def unique_move(self, type: int, new_rank, new_file):
        # print("Unique_move called for type: ", type)
        if (type == NORMAL):
            self.m_game.en_passant_square = None
            pass
        elif (type == W_KS_CASTLE):
            self.m_game.en_passant_square = None
            self.m_game.w_kingside_castle_rights = False
            self.m_game.w_queenside_castle_rights = False

            # move rook
            kingside_rook: Rook = self.m_game.board[0, h]
            assert(kingside_rook is not None)

            self.m_game.last_move_type = NORMAL
            print("moving rook")
            kingside_rook.move(0, f)

            print_board(self.m_game.board)
        elif (type == W_QS_CASTLE):
            self.m_game.en_passant_square = None
            pass
        elif (type == W_EN_PASSANT):
            ep_square = self.m_game.en_passant_square
            self.m_game.board[ep_square[0] - 1, ep_square[1]] = None
            self.m_game.en_passant_square = None
            
        elif (type == W_PROMOTION):
            self.m_game.en_passant_square = None
            pass
        elif (type == B_KS_CASTLE):
            self.m_game.en_passant_square = None
            pass
        elif (type == B_QS_CASTLE):
            self.m_game.en_passant_square = None
            pass
        elif (type == B_EN_PASSANT):
            ep_square = self.m_game.en_passant_square
            self.m_game.board[ep_square[0] + 1, ep_square[1]] = None
            self.m_game.en_passant_square = None
        elif (type == B_PROMOTION):
            self.m_game.en_passant_square = None
            pass
        elif (type == W_PAWN_2S):
            self.m_game.en_passant_square = (new_rank - 1, new_file)
        elif (type == B_PAWN_2S):
            self.m_game.en_passant_square = (new_rank + 1, new_file)


    """
    Final move function, only called once valid move has been verified
    """
    def move(self, new_rank: int, new_file: int):
        # board: np.ndarray = self.m_game.board

        # update if enemy king is in check

        # update king position if necessary
        if (type(self) == King):
            # print("changing king metadata")
            if (self.color):
                self.m_game.w_king_pos = (new_rank, new_file)
                self.m_game.w_kingside_castle_rights = False
                self.m_game.w_queenside_castling_rights = False
            else:
                self.m_game.b_king_pos = (new_rank, new_file)
                self.m_game.b_kingside_castling_rights = False
                self.m_game.b_queenside_castling_rights = False
            
        elif (type(self) == Rook):
            if (self.color and self.file == h):
                self.m_game.w_kingside_castle_rights = False
            elif (self.color and self.file == a):
                self.m_game.w_queenside_castle_rights = False
            elif (not self.color and self.file == a):
                self.m_game.b_kingside_castle_rights = False
            elif (not self.color and self.file == h):
                self.m_game.b_queenside_castle_rights = False
        
        elif (type(self) == Pawn):
            self.has_moved = True
                
        
        
        # specific situation moves
        self.unique_move(self.m_game.last_move_type, new_rank, new_file)
        
        # print("Moving piece to new_rank = ", new_rank, " new_file = ", new_file)
        self.m_game.board[new_rank, new_file] = self
        # print("Vacating old square at self.rank = ", self.rank, "self.file = ", self.file)
        self.m_game.board[self.rank, self.file] = None

        self.rank = new_rank
        self.file = new_file

        self.m_game.turn = not self.m_game.turn


    """
    Checks universal requirements regardless of piece type, then checks if specific piece move is valid
    """
    def try_move(self, new_file, new_rank, debug_mode = True):
        # Enforce correct move order
        if (self.m_game.turn != self.color):
            print("Cannot move on opponent's turn")

        new_rank -= debug_mode
        if (new_rank == self.rank and new_file == self.file):
            print("Piece cannot move to own square")
            return False
        
        # check if moving to square occupied by own piece
        if (self.m_game.board[new_rank, new_file] is not None):
            same_color: bool = self.m_game.board[new_rank, new_file].color == self.color
            if (same_color):
                print("Cannot move to square occupied by piece of own color")
                return False

        if self.check_valid_move(new_rank, new_file):
            # add condition here which evaluates if side that just moved is in check at end of turn.
            # if so, must find a new move. 
            print("Valid move")
            # print("Moving piece to new square")
            self.move(new_rank, new_file)
        else:
            print("Invalid move")
            return False


    def update_game_info(self):
        self.m_game.turn = not self.m_game.turn


    def __str__(self):
        color_choices = ["B", "W"]
        return color_choices[self.color]
         

class King(Chess_Piece):
    def __init__(self, m_game: Game, color: bool, rank: int, file: int):
        super().__init__(m_game, color, rank, file)

    def move_is_castle(self, new_file, new_rank):
        valid_rank: int = 0 if self.color else 7
        is_castle_square: bool = new_rank == valid_rank and (new_file == g or new_file == c) 
        is_orig_square: bool = self.rank == valid_rank and self.file == e
        return (is_orig_square and is_castle_square)

    def check_legal_castle(self, direction) -> bool:
        # combined_occupied = np.logical_or(self.m_game.white_occupied_squares, self.m_game.black_occupied_squares)

        # cannot castle out of check
        # Determine color-specific variables
        in_check = self.is_check(self.rank, self.file)
        kingside_rights = self.m_game.w_kingside_castle_rights if self.color else self.m_game.b_kingside_castle_rights
        queenside_rights = self.m_game.w_queenside_castle_rights if self.color else self.m_game.b_queenside_castle_rights
        rank = 0 if self.color else 7

        if in_check:
            print(f"Cannot castle, {'white' if self.color else 'black'} king is in check")
            return False

        if not kingside_rights and direction:
            print(f"Cannot castle, {'white' if self.color else 'black'} kingside rights lost")
            return False
        if not queenside_rights and not direction:
            print(f"Cannot castle, {'white' if self.color else 'black'} queenside rights lost")
            return False

        castling_blocked = False
        if direction:
            if not kingside_rights:
                print(f"Cannot castle: no {'white' if self.color else 'black'} kingside castling rights")
                return False
            pieces_block = scan_rank(self.m_game.board, old_file=e, new_file=g, rank=rank, direction=1) is not None
            enemies_block = self.is_check(rank, f) or self.is_check(rank, g)
            castling_blocked = enemies_block or pieces_block
        else:
            if not queenside_rights:
                print(f"Cannot castle: no {'white' if self.color else 'black'} queenside castling rights")
                return False
            pieces_block = scan_rank(self.m_game.board, old_file=e, new_file=b, rank=rank, direction=0) is not None
            enemies_block = self.is_check(rank, d) or self.is_check(rank, c)
            castling_blocked = enemies_block or pieces_block

        if castling_blocked:
            print("Cannot castle, path is blocked")
            print("pieces_block: ", pieces_block)
            print("enemies_block: ", enemies_block)
            return False

        print("Castling is legal")
        if self.color:
            self.m_game.last_move_type = W_KS_CASTLE if direction else W_QS_CASTLE
        else:
            self.m_game.last_move_type = B_KS_CASTLE if direction else B_QS_CASTLE
        return True
            
        


    def check_valid_move(self, new_rank, new_file):
        print("Piece type: ", self)

        is_castle: bool = self.move_is_castle(new_file, new_rank)
        if (is_castle):
            # true if kingside, false if queenside
            direction: bool = new_file == g
            return self.check_legal_castle(direction)

        # not a castle move
        file_dif: int = abs(new_file - self.file)
        rank_dif: int = abs(new_rank - self.rank)
        if not (rank_dif == 1 or file_dif == 1):
            
            print("Invalid move, king can only move one square in any direction")
            return False
        
        print("Valid king move")
        return True
        
    
    def is_check(self, rank, file):

        # check along orthogonal and diagonal directions for pieces. If first piece encountered is opposite
        # color, then king would be in check at that location. If first piece encountered is own color, then
        # king is not threatened in that direction


        # check orthogonal moves
        piece_N = scan_file(self.m_game.board, rank, 7, file, True) 
        piece_S = scan_file(self.m_game.board, rank, 0, file, False) 
        piece_W = scan_rank(self.m_game.board, rank, file, 7, True) 
        piece_E = scan_rank(self.m_game.board, rank, file, 0, False) 

        # print("piece_N: " +  str(type(piece_N)))

        piece_arr = [piece_N, piece_S, piece_W, piece_E]
        for piece in piece_arr:
            if piece is None:
                continue
            if piece.color != self.color:
                if type(piece) == Rook or type(piece) == Queen:
                    return True
                elif type(piece) == King:
                    # if king, must be one displacement away      
                    if (abs(piece.rank - rank) == 1 or abs(piece.file - file) == 1):
                        return True
                
        # check diagonal moves
        piece_NE = scan_diag(self.m_game.board, rank, file, 8, True, True) 
        piece_SE = scan_diag(self.m_game.board, rank, file, 8, False, True)
        piece_SW = scan_diag(self.m_game.board, rank, file, 8, False, False)
        piece_NW = scan_diag(self.m_game.board, rank, file, 8, True, False)

        # print("piece_NW: " +  str(type(piece_NW)))

        piece_arr = [piece_NE, piece_SE, piece_SW, piece_NW]
        for piece in piece_arr:
            if piece is None:
                continue
            if piece.color != self.color:
                if type(piece) == Bishop or type(piece) == Queen:
                    return True
                elif type(piece) == King:
                    # if king, must be one displacement away
                    if (abs(piece.rank - rank) == 1 or abs(piece.file - file) == 1):
                        return True
                elif type(piece) == Pawn:
                    if (self.color): # if white
                        if ((piece.rank - rank) == 1 and abs(piece.file - file) == 1):
                            return True   
            
        # Otherwise, need to check knight moves
        for move in KNIGHT_MOVES:
            curr_rank = rank - move[0]
            curr_file = file - move[1]

            if (curr_rank not in range(8) or curr_file not in range(8)):
                 continue
            
            piece = self.m_game.board[curr_rank][curr_file]
            if (type(piece) == Knight):
                if self.color != piece.color:
                    return True
    
        return False

    def __str__(self):
        return super().__str__() + "K"

class Pawn(Chess_Piece):
    def __init__(self, m_game: Game, color: bool, rank: int, file: int):
        super().__init__(m_game, color, rank, file)
        self.has_moved = False

    def check_valid_move(self, new_rank, new_file) -> bool:
        x_displacement: int = new_file - self.file
        y_displacement: int = new_rank - self.rank


        direction = 1 if self.color else -1
        start_rank = 1 if self.color else 6
        is_capture = abs(x_displacement) == 1 and y_displacement == direction

        if is_capture:
            target_piece = self.m_game.board[new_rank, new_file]
            if target_piece is None:
                # check if en-passant capture
                if self.m_game.en_passant_square == (new_rank, new_file) and self.m_game.en_passant_square is not None:
                    print(f"Valid move, {'white' if self.color else 'black'} pawn captures piece en-passant")
                    self.m_game.last_move_type = W_EN_PASSANT if self.color else B_EN_PASSANT
                    return True
                print("Invalid move, not en-passant and no piece to capture")
                return False
            elif target_piece.color != self.color:
                print(f"Valid move, {'white' if self.color else 'black'} pawn captures enemy piece diagonally")
                return True
            else:
                print("Invalid move, cannot capture own piece")
                return False
        else:
            if x_displacement != 0:
                print(f"Invalid move, {'white' if self.color else 'black'} pawn can only move forward when not capturing")
                return False

            piece_in_front = self.m_game.board[self.rank + direction, self.file]
            piece_two_in_front = self.m_game.board[self.rank + 2 * direction, self.file] if (self.rank == start_rank) else None

            if y_displacement == direction and piece_in_front is None:
                return True
            elif (
                y_displacement == 2 * direction
                and piece_in_front is None
                and piece_two_in_front is None
                and self.rank == start_rank
                and not self.has_moved
            ):
                self.m_game.last_move_type = W_PAWN_2S if self.color else B_PAWN_2S
                return True
            else:
                print(f"Invalid move, {'white' if self.color else 'black'} pawn can only move forward one square or two squares from starting position")
                return False

                
    def __str__(self):
        return super().__str__().lower() + "p"
    
class Rook(Chess_Piece):
    def __init__(self, m_game: Game, color: bool, rank: int, file: int):
        super().__init__(m_game, color, rank, file)

    def check_valid_move(self, new_rank, new_file):
        if (self.rank != new_rank and self.file != new_file):
            return False
        elif (self.rank != new_rank and self.file == new_file):
            direction = self.calc_vertical_direction(self.rank, new_rank)
            return scan_file(self.m_game.board, self.rank, new_rank, self.file, direction) is None
        else:
            direction = self.calc_horizontal_direction(self.file, new_file)
            return scan_rank(self.m_game.board, self.file, new_file, self.rank, direction) is None
    
    def __str__(self):
        return super().__str__() + "R"

class Knight(Chess_Piece):
    def __init__(self, m_game: Game, color: bool, rank: int, file: int):
        super().__init__(m_game, color, rank, file)

    def check_valid_move(self, new_rank, new_file):
        rank_displ = abs(new_rank - self.rank)
        file_displ = abs(new_file - self.file)
        if rank_displ == 1:
            return file_displ == 2
        elif rank_displ == 2:
            return file_displ == 1
        else:
            return False

    def __str__(self):
        return super().__str__() + "N"

class Bishop(Chess_Piece):
    def __init__(self, m_game: Game, color: bool, rank: int, file: int):
        super().__init__(m_game, color, rank, file)

    def check_valid_move(self, new_rank, new_file):
        file_displ = new_rank - self.rank
        rank_displ = new_file - self.file
        if (abs(file_displ) != abs(rank_displ)):
            print("Invalid Bishop move: piece must move diagonally")
            return False
        else:
            
            file_dir = self.calc_vertical_direction(self.rank, new_rank)
            rank_dir = self.calc_horizontal_direction(self.file, new_file)
            if (scan_diag(self.m_game.board, self.rank, self.file, file_displ, file_dir, rank_dir) is None):
                return True
            else:
                print("Invalid Bishop move: piece blocking the way")
                return False
        

    def __str__(self):
        return super().__str__() + "B"

class Queen(Chess_Piece):
    def __init__(self, m_game: Game, color: bool, rank: int, file: int):
        super().__init__(m_game, color, rank, file)

    def check_valid_move(self, new_rank, new_file):
        # if rank != file, check conditions for bishop move
        if (self.rank != new_rank and self.file != new_file):
            
            file_displ = new_rank - self.rank
            rank_displ = new_file - self.file
            if (abs(file_displ) != abs(rank_displ)):
                return False
            else:

                direction_on_file = self.calc_vertical_direction(old_rank=self.rank, new_rank=new_rank)
                direction_on_rank = self.calc_horizontal_direction(old_file=self.file, new_file=new_file)

                if (scan_diag(self.m_game.board, self.rank, self.file, file_displ, direction_on_file, direction_on_rank) is None):
                    return True
                else:
                    return False
                
        # otherwise, check conditions for rook move
        elif (self.rank != new_rank and self.file == new_file):
            direction = self.calc_vertical_direction(self.rank, new_rank)
            return scan_file(self.m_game.board, self.rank, new_rank, self.file, direction) is None
        else:
            direction = self.calc_horizontal_direction(self.file, new_file)
            return scan_rank(self.m_game.board, self.file, new_file, self.rank, direction) is None

    def __str__(self):
        return super().__str__() + "Q"
    
def print_board(board):
    print("-" * 41)
    curr_row: int = board.shape[0] - 1
    while curr_row >= 0:
        print("| " + " | ".join(str(piece) if piece is not None else "  " for piece in board[curr_row, :]) + " |")
        print("-" * 41)
        curr_row -=1