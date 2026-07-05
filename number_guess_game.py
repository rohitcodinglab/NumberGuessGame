import tkinter as tk
from tkinter import messagebox
import random

# -----------------------
# Game Variables
# -----------------------
number = random.randint(1, 100)
attempts = 0
max_attempts = 10

# -----------------------
# Guess Function
# -----------------------
def check_guess():
    global number, attempts

    guess = entry.get()

    if not guess.isdigit():
        result.config(text="❌ Enter a valid number!", fg="#ff5555")
        return

    guess = int(guess)
    attempts += 1

    attempts_label.config(
        text=f"Attempts: {attempts}/{max_attempts}"
    )

    if guess < number:
        result.config(text="Guess higher number please", fg="#00d9ff")

    elif guess > number:
        result.config(text="guess lower number please", fg="#ffb347")

    else:
        result.config(
            text=f"🎉 Correct! Number was {number}",
            fg="#00ff7f"
        )
        messagebox.showinfo(
            "Congratulations",
            f"You guessed it in {attempts} attempts!"
        )
        entry.config(state="disabled")

    if attempts >= max_attempts and guess != number:
        messagebox.showinfo(
            "Game Over",
            f"You Lost!\nThe number was {number}"
        )
        entry.config(state="disabled")

    entry.delete(0, tk.END)


# -----------------------
# Restart Game
# -----------------------
def restart():
    global number, attempts

    number = random.randint(1, 100)
    attempts = 0

    entry.config(state="normal")
    entry.delete(0, tk.END)

    result.config(
        text="Guess a number between 1 and 100",
        fg="white"
    )

    attempts_label.config(
        text=f"Attempts: 0/{max_attempts}"
    )


# -----------------------
# GUI
# -----------------------
root = tk.Tk()
root.title("🎯 RohitCodingLab")
root.geometry("600x550")
root.configure(bg="#1f1f2e")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🎯 Number Guessing Game",
    font=("Segoe UI", 22, "bold"),
    bg="#1f1f2e",
    fg="cyan"
)
title.pack(pady=20)

instruction = tk.Label(
    root,
    text="I'm thinking of a number (1 - 100)",
    font=("Segoe UI", 12),
    bg="#1f1f2e",
    fg="white"
)
instruction.pack()

entry = tk.Entry(
    root,
    font=("Segoe UI", 18),
    justify="center",
    width=10,
    bd=3
)
entry.pack(pady=20)

guess_btn = tk.Button(
    root,
    text="Guess",
    font=("Segoe UI", 14, "bold"),
    bg="#00b894",
    fg="white",
    width=15,
    command=check_guess
)
guess_btn.pack()

result = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Segoe UI", 14),
    bg="#1f1f2e",
    fg="white"
)
result.pack(pady=20)

attempts_label = tk.Label(
    root,
    text=f"Attempts: 0/{max_attempts}",
    font=("Segoe UI", 12),
    bg="#1f1f2e",
    fg="#bbbbbb"
)
attempts_label.pack()

restart_btn = tk.Button(
    root,
    text="🔄 Play Again",
    font=("Segoe UI", 14, "bold"),
    bg="#0984e3",
    fg="white",
    width=15,
    command=restart
)
restart_btn.pack(pady=20)

footer = tk.Label(
    root,
    text="Made with Python ❤️",
    font=("Segoe UI", 10),
    bg="#1f1f2e",
    fg="gray"
)
footer.pack(side="bottom", pady=15)

root.mainloop()