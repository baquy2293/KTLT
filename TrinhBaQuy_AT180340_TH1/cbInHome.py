import tkinter as tk
import random
from PIL import Image, ImageTk


def rock_paper_scissors(player_choice):
    global player_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result.config(text=f"Tie! Both chose {player_choice}.")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result.config(text=f" You win! {player_choice} beats {computer_choice}.")
        player_score += 1
        update_scores()
    else:
        result.config(text=f" You lose! {computer_choice} beats {player_choice}.")
        computer_score += 1
        update_scores()

def update_scores():
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")

def play_rock():
    rock_paper_scissors('Rock')

def play_paper():
    rock_paper_scissors('Paper')

def play_scissors():
    rock_paper_scissors('Scissors')

root = tk.Tk()
root.title('Rock Paper Scissors')


player_score = 0
computer_score = 0


rock_img = Image.open("E:/pyhton/pythonProject/1.png").resize((65,65))
paper_img = Image.open("E:/pyhton/pythonProject/2.png").resize((65,65))
scissors_img = Image.open("E:/pyhton/pythonProject/3.png").resize((65,65))

rock_photo = ImageTk.PhotoImage(rock_img)
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_photo = ImageTk.PhotoImage(scissors_img)


rock_btn = tk.Button(root, image=rock_photo,pady=5,command=play_rock)
rock_btn.pack()

paper_btn = tk.Button(root, image=paper_photo,pady=5, command=play_paper)
paper_btn.pack()

scissors_btn = tk.Button(root, image=scissors_photo,pady=5, command=play_scissors)
scissors_btn.pack()

result = tk.Label(root, font=('Arial', 20))
result.pack()

player_score_label = tk.Label(root, text=f"Player: {player_score}", font=('Arial', 15))
player_score_label.pack()

computer_score_label = tk.Label(root, text="Computer: {computer_score}", font=('Arial', 15))
computer_score_label.pack()

root.mainloop()