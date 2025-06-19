import numpy as np
from macros import *

class Game:
    def __init__(self, game_pieces: np.ndarray):
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


    
    """
    Checks if pieces block squares in between self and final destination along rank
    Gets called with rank1 = starting rank, rank2 = destination rank
    :param direction: 1 = Going up, 0 = Going down
    """
    def scan_file(self, old_rank, new_rank, file, direction: bool):
        range_dir = 1 if direction else -1
        displ = abs(new_rank - old_rank)
        for rank in range(old_rank + range_dir, new_rank, range_dir):
            if rank < 0 or rank > 7:
                return None
            if self.m_game.board[rank, file] is not None:
                return self.m_game.board[rank, file]
        return None

    """
    Returns the first piece encounter along rank
    Gets called with rank1 = starting rank, rank2 = destination rank
    :param direction: 1 = Going right, 0 = Going left
    """
    def scan_rank(self, rank, old_file, new_file, direction: int):
        range_dir = 1 if direction else -1
        displ = abs(new_file - old_file)
        for file in range(old_file + range_dir, new_file, range_dir):
            if file < 0 or file > 7:
                return None
            if self.m_game.board[rank, file] is not None:
                return self.m_game.board[rank, file]
        return None

            
    
    """
    :param file_dir: 1 = Going up, 0 = Going down
    :param rank_dir: 1 = Going right, 0 = Going left

    """
    def scan_diag(self, old_rank, old_file, step: int, file_dir: int, rank_dir):
        file_range_dir = 1 if file_dir else -1
        rank_range_dir = 1 if rank_dir else -1
        print("file_range_dir: ", file_range_dir)
        print("rank_range_dir: ", rank_range_dir)
        print("old_file: ", old_file)
        print("old_rank: ", old_rank)
        print("step: ", step)
        h_step = step * rank_range_dir
        f_traversed = 1
        for file in range(old_file + rank_range_dir, old_file + h_step, rank_range_dir):
            rank = old_rank + file_range_dir * f_traversed
            print("Currently scanning the square: ", file, ", ", rank)
            if file < 0 or file > 7 or rank < 0 or rank > 7:
                return None
            if self.m_game.board[rank, file] is not None:
                return self.m_game.board[rank, file]
            f_traversed += 1
                
        return None
        

    def unique_move(self, type: int, new_rank, new_file):
        if (type == NORMAL):
            pass
        elif (type == W_KS_CASTLE):
            self.m_game.w_kingside_castle_rights = False
            self.m_game.w_queenside_castle_rights = False

            # move rook
            kingside_rook: Rook = self.m_game.board[0, h]
            assert(kingside_rook is not None)

            self.m_game.last_move_type = NORMAL
            kingside_rook.move(0, f)
        elif (type == W_QS_CASTLE):
            pass
        elif (type == W_EN_PASSANT):
            self.m_game.en_passant_square = None
        elif (type == W_PROMOTION):
            pass
        elif (type == B_KS_CASTLE):
            pass
        elif (type == B_QS_CASTLE):
            pass
        elif (type == B_EN_PASSANT):
            self.m_game.en_passant_square = None
        elif (type == B_PROMOTION):
            pass
        elif (type == W_PAWN_2S):
            self.m_game.en_passant_square = (new_rank - 1, new_file)
        elif (type == B_PAWN_2S):
            self.m_game.en_passant_square = (new_rank + 1, new_file)


    """
    Final move function, only called once valid move has been verified
    """
    def move(self, new_rank: int, new_file: int):
        board: np.ndarray = self.m_game.board

        # print("Moving piece to new_rank = ", new_rank, " new_file = ", new_file)
        board[new_rank, new_file] = self
        # print("Vacating old square at self.rank = ", self.rank, "self.file = ", self.file)
        board[self.rank, self.file] = None


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
            
        
        elif (type(self) == Pawn):
            self.has_moved = True
                
        self.rank = new_rank
        self.file = new_file
        
        # specific situation moves
        self.unique_move(self.m_game.last_move_type, new_rank, new_file)
        


    """
    Checks universal requirements regardless of piece type, then checks if specific piece move is valid
    """
    def try_move(self, new_file, new_rank):
        new_rank -= 1
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
        in_check = self.m_game.white_in_check if self.color else self.m_game.black_in_check
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
            pieces_block = self.scan_rank(old_file=e, new_file=g, rank=rank, direction=1) is not None
            enemies_block = False
            castling_blocked = enemies_block or pieces_block
        else:
            if not queenside_rights:
                print(f"Cannot castle: no {'white' if self.color else 'black'} queenside castling rights")
                return False
            pieces_block = self.scan_rank(old_file=e, new_file=c, rank=rank, direction=0) is not None
            enemies_block = False
            castling_blocked = enemies_block or pieces_block

        if castling_blocked:
            print("Cannot castle, path is blocked")
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
            return self.scan_file(self.rank, new_rank, self.file, direction) is None
        else:
            direction = self.calc_horizontal_direction(self.file, new_file)
            return self.scan_rank(self.file, new_file, self.rank, direction) is None
    
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
            if (self.scan_diag(self.rank, self.file, file_displ, file_dir, rank_dir) is None):
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

                if (self.scan_diag(self.rank, self.file, file_displ, direction_on_file, direction_on_rank) is None):
                    return True
                else:
                    return False
                
        # otherwise, check conditions for rook move
        elif (self.rank != new_rank and self.file == new_file):
            direction = self.calc_vertical_direction(self.rank, new_rank)
            return self.scan_file(self.rank, new_rank, self.file, direction) is None
        else:
            direction = self.calc_horizontal_direction(self.file, new_file)
            return self.scan_rank(self.file, new_file, self.rank, direction) is None

    def __str__(self):
        return super().__str__() + "Q"
    
def print_board(board):
    print("-" * 41)
    curr_row: int = board.shape[0] - 1
    while curr_row >= 0:
        print("| " + " | ".join(str(piece) if piece is not None else "  " for piece in board[curr_row, :]) + " |")
        print("-" * 41)
        curr_row -=1