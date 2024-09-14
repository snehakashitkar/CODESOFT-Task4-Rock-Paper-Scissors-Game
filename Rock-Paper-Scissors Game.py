import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the result and scores after each round
def play_round(user_choice):
    global user_score, computer_score

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

    # Update scores
    if "You win!" in result:
        user_score += 1
    elif "Computer wins!" in result:
        computer_score += 1

    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

# Function to restart the game
def restart_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score: You 0 - 0 Computer")
    result_label.config(text="Make your move!")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")

# Initialize scores
user_score = 0
computer_score = 0

# Title label
title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 20))
title_label.pack(pady=10)

# Result label
result_label = tk.Label(window, text="Make your move!", font=("Arial", 14))
result_label.pack(pady=10)

# Score label
score_label = tk.Label(window, text="Score: You 0 - 0 Computer", font=("Arial", 12))
score_label.pack(pady=10)

# Create buttons for rock, paper, scissors
rock_button = tk.Button(window, text="Rock", width=15, height=2, command=lambda: play_round('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=15, height=2, command=lambda: play_round('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=15, height=2, command=lambda: play_round('scissors'))
scissors_button.pack(pady=5)

# Restart game button
restart_button = tk.Button(window, text="Restart Game", width=15, height=2, command=restart_game)
restart_button.pack(pady=20)

# Start the GUI loop
window.mainloop()
