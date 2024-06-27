import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"


def choose_option(option):
    global user_score, computer_score, choice_made
    if not choice_made:
        choice_made = True
        user_choice = option.lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        user_img = Image.open(f"{user_choice}.png").resize((150, 150), Image.LANCZOS)
        user_img = ImageTk.PhotoImage(user_img)
        computer_img = Image.open(f"{computer_choice}.png").resize((150, 150), Image.LANCZOS)
        computer_img = ImageTk.PhotoImage(computer_img)

        label_user_choice.config(image=user_img)
        label_user_choice.image = user_img
        label_computer_choice.config(image=computer_img)
        label_computer_choice.image = computer_img

        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            user_score += 1
            label_result.config(text="You win!", fg="green")
        elif result == "computer":
            computer_score += 1
            label_result.config(text="Computer wins!", fg="red")
        else:
            label_result.config(text="It's a tie!", fg="blue")

        label_score.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

        button_rock.config(state=tk.DISABLED)
        button_paper.config(state=tk.DISABLED)
        button_scissors.config(state=tk.DISABLED)


def reset_game():
    global user_score, computer_score, choice_made
    user_score = 0
    computer_score = 0
    choice_made = False

    label_score.config(text="Score - You: 0, Computer: 0")
    label_user_choice.config(image="")
    label_computer_choice.config(image="")
    label_result.config(text="")

    button_rock.config(state=tk.NORMAL)
    button_paper.config(state=tk.NORMAL)
    button_scissors.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")
root.resizable(0,0)

user_score = 0
computer_score = 0
choice_made = False

rock_img = Image.open("rock.png").resize((100, 100), Image.LANCZOS)
rock_img = ImageTk.PhotoImage(rock_img)
paper_img = Image.open("paper.png").resize((100, 100), Image.LANCZOS)
paper_img = ImageTk.PhotoImage(paper_img)
scissors_img = Image.open("scissors.png").resize((100, 100), Image.LANCZOS)
scissors_img = ImageTk.PhotoImage(scissors_img)

label_title = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 18, "bold"))
label_title.pack(pady=20)

label_instruction = tk.Label(root, text="Choose one:", font=("Helvetica", 14))
label_instruction.pack()

button_rock = tk.Button(root, image=rock_img, command=lambda: choose_option("rock"))
button_rock.pack(side=tk.LEFT, padx=10)

button_paper = tk.Button(root, image=paper_img, command=lambda: choose_option("paper"))
button_paper.pack(side=tk.LEFT, padx=10)

button_scissors = tk.Button(root, image=scissors_img, command=lambda: choose_option("scissors"))
button_scissors.pack(side=tk.LEFT, padx=10)

label_user_choice = tk.Label(root)
label_user_choice.pack(pady=10)

label_computer_choice = tk.Label(root)
label_computer_choice.pack(pady=10)

label_result = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
label_result.pack(pady=20)

label_score = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14))
label_score.pack()

button_reset = tk.Button(root, text="Reset", width=10, command=reset_game)
button_reset.pack(pady=10)

button_quit = tk.Button(root, text="Quit", width=10, command=root.destroy)
button_quit.pack(pady=10)

root.mainloop()
