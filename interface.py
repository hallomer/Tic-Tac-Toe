#!/usr/bin/python3
"""Inital interface for Tic-Tac-Toe game."""
from tkinter import *

CANVAS_WIDTH = 360
CANVAS_HEIGHT = 600


def create_buttons(canvas):
    """Create buttons and their text on the canvas."""
    # Add buttons
    player1_button = canvas.create_rectangle(
        CANVAS_WIDTH / 2 - 80,
        CANVAS_HEIGHT / 3 + 90,
        CANVAS_WIDTH / 2 + 80,
        CANVAS_HEIGHT / 3 + 130,
        fill="green", outline="black"
    )

    player2_button = canvas.create_rectangle(
        CANVAS_WIDTH / 2 - 80,
        CANVAS_HEIGHT / 3 + 150,
        CANVAS_WIDTH / 2 + 80,
        CANVAS_HEIGHT / 3 + 190,
        fill="orange", outline="black"
    )
    # Add text to buttons
    player1_button_text = canvas.create_text(
        (CANVAS_WIDTH / 2 - 80 + CANVAS_WIDTH / 2 + 80) / 2,
        (CANVAS_HEIGHT / 3 + 90 + CANVAS_HEIGHT / 3 + 130) / 2,
        text="one player",
        fill="black",
        font=("American Typewriter", 20)
    )

    player2_button_text = canvas.create_text(
        (CANVAS_WIDTH / 2 - 80 + CANVAS_WIDTH / 2 + 80) / 2,
        (CANVAS_HEIGHT / 3 + 150 + CANVAS_HEIGHT / 3 + 190) / 2,
        text="two players",
        fill="black",
        font=("American Typewriter", 20)
    )

    return player1_button, player1_button_text, player2_button, player2_button_text


def setup_canvas(window):
    """Set up the canvas with background, title, and buttons."""
    # Create and pack a canvas widget
    canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Load an image and add it to the canvas
    img = PhotoImage(file="background.png")
    canvas.img = img
    canvas.create_image(0, 0, anchor=NW, image=img)

    # Add title of the game
    canvas.create_text(
        CANVAS_WIDTH / 2, CANVAS_HEIGHT / 3,
        text="Tic-Tac-Toe",
        fill="yellow",
        font=("American Typewriter", 60)
    )
    # Shoutoout to Sudan
    canvas.create_text(20, 20, text="🇸🇩")

    # Set up buttons
    player1_button, player1_button_text, player2_button, player2_button_text = create_buttons(canvas)
    
    return canvas, img, player1_button, player1_button_text, player2_button, player2_button_text