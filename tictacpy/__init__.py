import functools
from random import randint


class Printer():
    PLAYERS = [None, "x", "o"]
    TILES = [
        [
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
        ],
        [
            "           ",
            "   \   /   ",
            "     +     ",
            "   /   \   ",
            "           ",
        ],
        [
            "           ",
            "     -     ",
            "   (   )   ",
            "     -     ",
            "           ",
        ],
    ]

    def __init__(self, board):
        self.board = board

    def print_title(self):
        print("TicTacPy - @yo__bur")
        print("===================")
        print("")

    def _overlay_tile_number(orig):
        @functools.wraps(orig)
        def inner(self, tile_number=0, line_number=0):
            result = orig(self, tile_number, line_number)
            if line_number == 0:
                return " " + str(tile_number + 1) + result[2:]

            return result
        return inner


    @_overlay_tile_number
    def _print_tile(self, tile_number=0, line_number=0):
        return self.TILES[self.board[tile_number]][line_number]

    def print_board(self):
        board_width = len(self.TILES[0][0]) * 3 + 2

        print(f" {'-' * board_width} ")
        for i in range(3):
            for r in range(len(self.TILES[0])):
                print(f"|{self._print_tile(i*3,r)}x{self._print_tile(i*3+1,r)}x{self._print_tile(i*3+2,r)}|")

            if i < 3 - 1:
                print(f"|{'x' * board_width}|")

        print(f" {'-' * board_width} ")

class TicTacPy():

    WINNABLE_PATTERNS = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    def __init__(self, first_player=None):
        self.board = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
        ]

        self.printer = Printer(self.board)
        self.current_player = first_player or randint(1,2)

    def _compare(self, pattern):
        tiles = [self.board[x] for x in pattern]
        return all(x == tiles[0] for x in tiles) and all(tiles)


    def start(self):
        self.printer.print_title()

        while True:
            self.printer.print_board()

            # Detect win.
            for pattern in self.WINNABLE_PATTERNS:
                if self._compare(pattern):
                    print(f"{self.printer.PLAYERS[self.board[pattern[0]]]} wins!")
                    return

            # Receive player input.
            while True:
                try:
                    selection = int(input(f"[{self.printer.PLAYERS[self.current_player]}] Pick a tile: ")) - 1
                except ValueError:
                    print("Invalid input...")
                    continue

                if self.board[selection] != 0:
                    print("Tile has already been selected...")
                    continue

                break

            # Update the board with the players selection.
            self.board[selection] = self.current_player

            # Switch current player
            self.current_player = [None, 2, 1][self.current_player]


def main():
    game = TicTacPy()
    game.start()


if __name__ == "__main__":
    main()
