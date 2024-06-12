#!/usr/bin/python3
"""Game logic for Tic-Tac-Toe game."""
from tkinter import *
from buttons import show_endgame_buttons

CANVAS_WIDTH = 360
CANVAS_HEIGHT = 600

def setup_game_board(canvas, one_player=False):
    """Set up the game board on the canvas."""
    # Clear the canvas, and add the background
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=canvas.img)

    # Shoutout to Sudan 
    canvas.create_text(20, 20, text="🇸🇩")
    
    # Display turn label
    turn_label = canvas.create_text(
    CANVAS_WIDTH / 2, CANVAS_HEIGHT / 8,
    text="Your turn" if one_player else "X's turn", fill="yellow", 
    font=("American Typewriter", 40)
    )

    # Calculate starting x position to center the grid
    box_size = 118
    grid_top = CANVAS_HEIGHT / 5
    grid_width = 3 * box_size
    start_x = (CANVAS_WIDTH - grid_width) / 2

    # Draw the Tic-Tac-Toe grid (3x3), starting at start_x
    board = [["" for _ in range(3)] for _ in range(3)]
    cells = {}
    for row in range(3):
        for col in range(3):
            x0, y0 = start_x + col * box_size, grid_top + row * box_size
            x1, y1 = start_x + (col + 1) * box_size, grid_top + (row + 1) * box_size
            rect = canvas.create_rectangle(
                x0, y0, x1, y1, fill="dark slate blue", outline="lavender"
            )
            cells[rect] = (row, col)

    # Initialize game_over flag
    canvas.game_over = False

    # Bind click events to the cells
    for rect in cells:
        canvas.tag_bind(
            rect, '<ButtonRelease>',
            lambda event, rect=rect: handle_click(event, canvas, rect, cells, board, turn_label, one_player)
        )

def update_turn_label(canvas, turn_label, text, one_player=False):
    """Update the turn label text."""
    if one_player and text == "O's turn":
        text = "Computer's turn"
    if one_player and text == "X's turn":
        text = "Your turn"
    canvas.itemconfigure(turn_label, text=text)

def check_winner(board):
    """Check for a winner in the Tic-Tac-Toe game."""
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
            return board[row][0], [(row, 0), (row, 1), (row, 2)], True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col], [(0, col), (1, col), (2, col)], True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0], [(0, 0), (1, 1), (2, 2)], True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2], [(0, 2), (1, 1), (2, 0)], True

    # Check for tie
    if all(cell != "" for row in board for cell in row):
        return "Tie", [], True

    return None, [], False

def handle_click(event, canvas, rect, cells, board, turn_label, one_player=False):
    """Handle a cell click."""
    # Check if the game is over
    if canvas.game_over:
        return

    row, col = cells[rect]
    if board[row][col] == "":  # Check if cell is empty
        current_player = "X" if canvas.itemcget(turn_label, "text") in ["X's turn", "Your turn"] else "O"
        board[row][col] = current_player

        # Draw the player's mark on the cell
        x0, y0, x1, y1 = canvas.coords(rect)
        canvas.create_text(
            (x0 + x1) / 2, (y0 + y1) / 2,
            text=current_player, fill="yellow", 
            font=("American Typewriter", 40)
        )

        # Check for win condition
        winner, winning_cells, game_over = check_winner(board)
        if game_over:
            if winner == "Tie":
                update_turn_label(canvas, turn_label, "Tied game :)")
            else:
                if one_player:
                    if winner == "X":
                        update_turn_label(canvas, turn_label, "You win :)")
                    else:
                        update_turn_label(canvas, turn_label, "Computer wins :)")
                else:
                    update_turn_label(canvas, turn_label, f"Player {winner} wins :)")
                highlight_winning_cells(canvas, cells, winning_cells)
            show_endgame_buttons(canvas)
            canvas.game_over = True  # Set game_over flag to True
            return

        # Switch turn
        if one_player and current_player == "X":
            update_turn_label(canvas, turn_label, "Computer's turn", one_player=True)
            canvas.after(500, lambda: make_computer_move(canvas, cells, board, turn_label))
        else:
            next_turn = "X's turn" if current_player == "O" else "O's turn"
            update_turn_label(canvas, turn_label, next_turn, one_player=one_player)


def highlight_winning_cells(canvas, cells, winning_cells):
    """Highlight the winning cells."""
    for rect, (row, col) in cells.items():
        if (row, col) in winning_cells:
            canvas.itemconfigure(rect, outline="yellow", width=5)



def make_computer_move(canvas, cells, board, turn_label):
    import random
    """Perform the computer's move."""
    # Basic computer strategy
    def find_winning_move(mark):
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = mark
                    if check_winner(board)[2]:
                        board[row][col] = ""
                        return (row, col)
                    board[row][col] = ""
        return None

    # Check if the computer can win
    move = find_winning_move("O")
    if move is None:
        # Check if the player is about to win and block
        move = find_winning_move("X")
    if move is None:
        # Take the center if available
        if board[1][1] == "":
            move = (1, 1)
    if move is None:
        # Take a random available move
        available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
        move = random.choice(available_moves)

    row, col = move
    board[row][col] = "O"

    # Draw the computer's mark on the cell
    for rect, pos in cells.items():
        if pos == (row, col):
            x0, y0, x1, y1 = canvas.coords(rect)
            canvas.create_text(
                (x0 + x1) / 2, (y0 + y1) / 2,
                text="O", fill="yellow", 
                font=("American Typewriter", 40)
            )

    # Check for win condition
    winner, winning_cells, game_over = check_winner(board)
    if game_over:
        if winner == "Tie":
            update_turn_label(canvas, turn_label, "Tied game :)")
        else:
            if winner == "X":
                update_turn_label(canvas, turn_label, "You win :)")
            else:
                update_turn_label(canvas, turn_label, "Computer wins :)")
            highlight_winning_cells(canvas, cells, winning_cells)
        show_endgame_buttons(canvas)
        canvas.game_over = True
        return

    # Switch turn back to player
    update_turn_label(canvas, turn_label, "Your turn", one_player=True)
