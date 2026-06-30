
BOARD_X_CHARACTERS = ['A','B','C', 'D', 'E', 'F', 'G', 'H']
BOARD_LENGTH = 8

def create_coordinates_string(x, y) -> str:
    """
        Create a string representation of the chess coordinates
        Input: (x, y) where x is the index of the column and y is the index of the row
        Output: "A1"
    """
    return f"{BOARD_X_CHARACTERS[x]}{y}"

def transform_coordinates_to_chess_coordinates(
        up_positions: list[tuple[int, int]], 
        down_positions: list[tuple[int, int]]
    ) -> list[str]:
    """
        Transform the coordinates from (x, y) to chess coordinates (A1, B2, etc)
        Input: [(x, y), (x, y), (x, y), (x, y)]
        Output: ["A1", "B2", "C3", "D4"]
    """
    up_coords = [create_coordinates_string(position[0], BOARD_LENGTH - position[1]) for position in up_positions]
    down_coords = [create_coordinates_string(position[0], BOARD_LENGTH - position[1]) for position in down_positions]

    return up_coords + down_coords    


def _calculate_up_positions(position: tuple[int, int]) -> list[str]:
    """ 
        Calculate the four potental positions for a knight to move up the board.
        Input: (x, y) where x is the index of the column and y is the index of the row
        Output: [(x, y), (x, y), (x, y), (x, y)]
    """

    positions = None
    x, y = position

    if y == 0:
        return []

    positions = [
        (x - 2, y - 1) if x > 1 else None, # two to the left, one up
        (x - 1, y - 2) if x >= 1 and y >= 2 else None, # two up, one to the left
        (x + 1, y - 2) if x <= 6 and y >= 2 else None, # two up, one to the right
        (x + 2, y - 1) if x <= 5 else None # two to the right, one up
    ]

    return [position for position in positions if position]

def _calculate_down_positions(position: tuple[int, int]) -> list[str]:
    """ 
        Calculate the four potental positions for a knight to move down the board.
        Input: (x, y) where x is the index of the column and y is the index of the row
        Output: [(x, y), (x, y), (x, y), (x, y)]
    """
    positions = None
    x, y = position

    if y == 7:
        return []
    
    positions = [
        (x - 2, y + 1) if x > 1 else None, # two to the left, one down
        (x - 1, y + 2) if x >= 1 and y <= 5 else None, # one to the left, two down
        (x + 1, y + 2) if x <= 6 and y <= 5 else None, # one to the right, two down
        (x + 2, y + 1) if x <= 5 and y <= 6 else None # two to the right, one down
    ]

    return [position for position in positions if position]


def get_knight_position(board_position: str) -> list[str]:
    """
        Get all of the positions for a next potential knight move
        Sample Input: E4
        Output: ["F6", ...]
    """

    if not board_position:
        raise ValueError("A board position is required")

    if len(board_position) != 2:
        raise ValueError("The board position must be of length 2")

    x, y = list(board_position)

    if x not in BOARD_X_CHARACTERS:
        raise ValueError("X position must be between A-G")

    y_number_value = int(y)

    if y_number_value < 1 or y_number_value > BOARD_LENGTH:
        raise ValueError("The Y value must be between 0-8")
    
    index_x_position = BOARD_X_CHARACTERS.index(x)
    chess_board_position_tuple = (index_x_position, BOARD_LENGTH - int(y))

    up_positions = _calculate_up_positions(chess_board_position_tuple)
    down_positions = _calculate_down_positions(chess_board_position_tuple)

    chess_coords_transform = transform_coordinates_to_chess_coordinates(up_positions, down_positions)

    return chess_coords_transform
    


# Sample Input: 'E4'
if __name__ == "__main__":
    print(get_knight_position("D4"))  # ['B4', 'C3', 'E3', 'F4', 'B6', 'C7', 'E7', 'F6']
    print(get_knight_position("A1"))  # ['B3', 'C2']
    print(get_knight_position("H8"))  # ['F7', 'G6']
