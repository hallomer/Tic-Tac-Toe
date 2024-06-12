#!/usr/bin/python3
"""Some buttons for Tic-Tac-Toe game."""
CANVAS_WIDTH = 360
CANVAS_HEIGHT = 600

# Global variable to store the game mode
game_mode = None

def start_one_player_game(event, canvas):
    from game_logic import setup_game_board
    """Handle the one player mode."""
    global game_mode
    game_mode = 'one_player'
    setup_game_board(canvas, one_player=True)

def start_two_players_game(event, canvas):
    from game_logic import setup_game_board
    """Handle the two players mode."""
    global game_mode
    game_mode = 'two_players'
    setup_game_board(canvas, one_player=False)

def show_endgame_buttons(canvas):
    """Show the 'Exit' and 'Play Again' buttons."""
    button_width = 100
    button_height = 50

    # Create "Exit" button and text
    exit_button = canvas.create_rectangle(
        CANVAS_WIDTH / 4 - button_width / 2,
        CANVAS_HEIGHT - 100,
        CANVAS_WIDTH / 4 + button_width / 2,
        CANVAS_HEIGHT - 100 + button_height,
        fill="red", outline="black"
    )
    exit_button_text = canvas.create_text(
        (CANVAS_WIDTH / 4 - button_width / 2 + CANVAS_WIDTH / 4 + button_width / 2) / 2,
        (CANVAS_HEIGHT - 100 + CANVAS_HEIGHT - 100 + button_height) / 2,
        text="Exit", fill="black", font=("American Typewriter", 18)
    )
    
    # Create "Play Again" button and text
    play_again_button = canvas.create_rectangle(
        3 * CANVAS_WIDTH / 4 - button_width / 2,
        CANVAS_HEIGHT - 100,
        3 * CANVAS_WIDTH / 4 + button_width / 2,
        CANVAS_HEIGHT - 100 + button_height,
        fill="green", outline="black"
    )
    play_again_button_text = canvas.create_text(
        (3 * CANVAS_WIDTH / 4 - button_width / 2 + 3 * CANVAS_WIDTH / 4 + button_width / 2) / 2,
        (CANVAS_HEIGHT - 100 + CANVAS_HEIGHT - 100 + button_height) / 2,
        text="Play Again", fill="black", font=("American Typewriter", 18)
    )

      # Bind click events to the buttons
    canvas.tag_bind(exit_button, '<ButtonRelease>', lambda event: canvas.master.quit())
    canvas.tag_bind(exit_button_text, '<ButtonRelease>', lambda event: canvas.master.quit())
    canvas.tag_bind(play_again_button, '<ButtonRelease>', lambda event: restart_game(canvas))
    canvas.tag_bind(play_again_button_text, '<ButtonRelease>', lambda event: restart_game(canvas))

def restart_game(canvas):
    """Restart the game with the previously selected mode."""
    from game_logic import setup_game_board
    global game_mode
    if game_mode == 'one_player':
        setup_game_board(canvas, one_player=True)
    elif game_mode == 'two_players':
        setup_game_board(canvas, one_player=False)
