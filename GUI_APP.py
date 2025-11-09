"""
Ecson Cervantes
""""
import random
import tkinter as tk
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

player_score = 0
computer_score = 0
tie_score = 0

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0, Computer: 0, Ties: 0", font=("Arial", 12))
score_label.pack(pady=10)

def play_round(player_choice):
    global player_score, computer_score, tie_score
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}")
    if result == "You win!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    elif result == "It's a tie!":
        tie_score += 1
    score_label.config(text=f"Score - You: {player_score}, Computer: {computer_score}, Ties: {tie_score}")

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play_round('rock'))
rock_button.grid(row=0, column=0, padx=5)
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play_round('paper'))
paper_button.grid(row=0, column=1, padx=5)
scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play_round('scissors'))
scissors_button.grid(row=0, column=2, padx=5)
quit_button = tk.Button(root, text="Quit", width=10, command=root.quit)
quit_button.pack(pady=10)

root.mainloop()