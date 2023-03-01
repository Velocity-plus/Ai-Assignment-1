# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_board(board):
    """
    Print the current state of the Kalaha board.
    """
    print("      ┌──────┬──────┬──────┬──────┬──────┐")
    print("      │  {:2d}  │  {:2d}  │  {:2d}  │  {:2d}  │  {:2d}  │".format(board[9], board[8], board[7], board[6], board[5]))
    print(" ┌────┴┬─────┴──────┴──────┴──────┴─────┬┴────┐")
    print(" │  {:2d} │                                │ {:2d}  │".format(board[11], board[10]))
    print(" └────┬┴─────┬──────┬──────┬──────┬─────┴┬────┘")
    print("      │  {:2d}  │  {:2d}  │  {:2d}  │  {:2d}  │  {:2d}  │".format(board[0], board[1], board[2], board[3], board[4]))
    print("      └──────┴──────┴──────┴──────┴──────┘")
    print("─────────────────────────────────────────────────────")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example usage:
    board = [4,4,4, 4, 4, 4, 4, 4, 4, 4, 0, 0]
    print_board(board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
