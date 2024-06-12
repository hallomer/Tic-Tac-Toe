#!/usr/bin/python3
"""Main module for Tic-Tac-Toe game."""
from tkinter import *
from interface import setup_canvas
from buttons import start_one_player_game, start_two_players_game


CANVAS_WIDTH = 360
CANVAS_HEIGHT = 600


def main():
    """Main function."""
    window = Tk()
    window.title('Tic-Tac-Toe')

    canvas, img, player1_button, player1_button_text, player2_button, player2_button_text = setup_canvas(window)

    # Bind the click events to the rectangles
    canvas.tag_bind(player1_button, '<ButtonRelease>', lambda event: start_one_player_game(event, canvas))
    canvas.tag_bind(player1_button_text, '<ButtonRelease>', lambda event: start_one_player_game(event, canvas))
    canvas.tag_bind(player2_button, '<ButtonRelease>', lambda event: start_two_players_game(event, canvas))
    canvas.tag_bind(player2_button_text, '<ButtonRelease>', lambda event: start_two_players_game(event, canvas))

    window.mainloop()

if __name__ == "__main__":
    main()
