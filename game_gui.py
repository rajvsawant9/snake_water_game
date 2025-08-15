import tkinter as tk
import random

# Your mapping and reverse mapping
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

def play_game(user_input):
    computer = random.choice([1, -1, 0])
    you = youDict[user_input]

    user_choice = reverseDict[you]
    computer_choice = reverseDict[computer]

    # Determine result (your exact logic)
    if computer == you:
        result = "It's a draw!"
    else:
        if computer == 1 and you == -1:
            result = "You lose!"
        elif computer == 1 and you == 0:
            result = "You win!"
        elif computer == -1 and you == 1:
            result = "You win!"
        elif computer == -1 and you == 0:
            result = "You lose!"
        elif computer == 0 and you == 1:
            result = "You lose!"
        elif computer == 0 and you == -1:
            result = "You win!"
        else:
            result = "Something went wrong!"

    result_label.config(
        text=f"Your choice: {user_choice}\n"
             f"Computer's choice: {computer_choice}\n\n"
             f"{result}"
    )

# GUI setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="Snake (s), Water (w), or Gun (g)", font=("Arial", 16))
title.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

snake_btn = tk.Button(button_frame, text="Snake (s)", width=12, font=("Arial", 12),
                      command=lambda: play_game("s"))
snake_btn.grid(row=0, column=0, padx=10)

water_btn = tk.Button(button_frame, text="Water (w)", width=12, font=("Arial", 12),
                      command=lambda: play_game("w"))
water_btn.grid(row=0, column=1, padx=10)

gun_btn = tk.Button(button_frame, text="Gun (g)", width=12, font=("Arial", 12),
                    command=lambda: play_game("g"))
gun_btn.grid(row=0, column=2, padx=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14), justify="center")
result_label.pack(pady=30)

# Start GUI loop
root.mainloop()
