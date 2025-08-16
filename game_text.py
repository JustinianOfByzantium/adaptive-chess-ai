from game_logic import *
from macros import *



def move_parser(move_str, game):
    if len(move_str) == 2:
        return parse_pawn_move(move_str, game)
    if len(move_str) == 4 and move_str[1] == "x":
        return parse_pawn_capture(move_str, game)

def parse_dest_square(target_str):
    file_str = target_str[0]
    rank_str = target_str[1]
    file = -1
    rank = -1
    try:
        file = FILE_IDX[file_str]
        rank = int(rank_str)
        if rank not in range(1,8):
            raise ValueError
        rank -= 1
    except KeyError:
        print(f"Could not parse file '{file}', must be a letter between a and h")
        return -1
    except (TypeError, ValueError):
        print(f"Could not parse rank '{rank}', must be a number between 1 and 8")
        return -1
    
    new_square = (rank, file)
    return new_square

def parse_pawn_move(move_str, game):
    target_str = move_str[0:2]
    new_square = parse_dest_square(target_str)
    if (new_square == -1): return -1
    rank = new_square[0]
    file = new_square[1]

    # determine which square the piece is trying to move from
    scan_dir = -1 if game.turn else 1
    
    old_square = (-1, -1)
    if type(game.board[rank + scan_dir, file]) is Pawn:
        old_square = (rank + scan_dir, file)
    else:
        if type(game.board[rank + scan_dir * 2, file]) is Pawn:
            old_square = (rank + scan_dir * 2, file)
        else:
            print("Invalid pawn move, no valid piece on originator square")
            return -1
        
    return (old_square, new_square)



        

def parse_pawn_capture(move_str, game):
    old_file_str = move_str[0]
    target_str = move_str[2:4]
    new_square = parse_dest_square(target_str)
    if (new_square == -1): return -1
    rank = new_square[0]
    file = new_square[1]

    # determine which square the piece is trying to move from 
    try:
        old_file = FILE_IDX[old_file_str]
    except KeyError:
        print(f"Could not parse file '{file}', must be a letter between a and h")
        return -1
    
    scan_dir = -1 if game.turn else 1
    if type(game.board[rank + scan_dir, old_file] is Pawn):
        old_square = (rank + scan_dir, old_file)
        return (old_square, new_square)
    else:
        print("Parsed move is an invalid pawn capture")
        return -1
    

    




    

def parse_and_move(move_str, game):
    parsed_move = move_parser(move_str, game)
    if (parsed_move == -1):
        print("Parsing move caused an error")
        return -1
    
    
    old_rank = parsed_move[0][0]
    old_file = parsed_move[0][1]
    new_rank = parsed_move[1][0]
    new_file = parsed_move[1][1]

    game.board[old_rank, old_file].try_move(new_file, new_rank, False)

def play_game():
    active_game: Game = Game(default_board=True)
    print_board(active_game.board)

    parse_and_move("e4", active_game)
    print_board(active_game.board)

    parse_and_move("e5", active_game)
    print_board(active_game.board)

    # parse_and_move("xg", active_game)
    # print_board(active_game.board)

    parse_and_move("d4", active_game)
    print_board(active_game.board)

    parse_and_move("exd4", active_game)
    print_board(active_game.board)

    parse_and_move("e5", active_game)
    print_board(active_game.board)

    parse_and_move("f5", active_game)
    print_board(active_game.board)

    # parse_and_move("a3", active_game)
    # print_board(active_game.board)

    # parse_and_move("a6", active_game)
    # print_board(active_game.board)

    parse_and_move("exf6", active_game)
    print_board(active_game.board)