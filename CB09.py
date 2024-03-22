from tkinter import *
from tkinter import messagebox
import os
import pygame
import tkinter as tk
from tkinter import filedialog
window = Tk()
window.geometry("560x720")
window.title("Log in window")
List_user_Pass = []



def open():
    def play_music():
        selected_song = listbox.get(tk.ACTIVE)
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()

    def stop_music():
        pygame.mixer.music.stop()

    def load_music():
        folder = filedialog.askdirectory()
        os.chdir(folder)
        songs = [file for file in os.listdir(folder) if file.endswith(".mp3")]
        for song in songs:
            listbox.insert(tk.END, song)

    def quit_music():
        root.destroy()
    root = tk.Tk()
    root.title("MP3 Player")
    pygame.init()
    pygame.mixer.init()

    listbox = tk.Listbox(root, width=50)
    listbox.pack(pady=18)

    play_button = tk.Button(root, text="Play", command=play_music)
    play_button.pack(pady=5)

    stop_button = tk.Button(root, text="Stop", command=stop_music)
    stop_button.pack(pady=5)

    load_button = tk.Button(root, text="Load Music Folder", command=load_music)
    load_button.pack(pady=10)
    button_quit = tk.Button(root, text="Quit", command=quit_music).pack()

def check(username,password):
    for entry in range(0,len(List_user_Pass)):
        if List_user_Pass[entry] ==(username+password):
           open()


def showList ():
    for entry in range(0,len(List_user_Pass)):
        print(List_user_Pass[entry])
def resgister():
 window1 = Tk()
 window1.geometry("560x720")
 window1.title("Sign up window")
 label_3 = Label(window1,font=("Arial", 15), fg="black", text="username").pack()
 entry_3 = (Entry(window1))
 entry_3.pack()
 label_4 =Label(window1,font=("Arial", 15), fg="black", text="password").pack()
 entry_4 = Entry(window1, font=("Arial", 15), fg="black", show="*")
 entry_4.pack()
 blank_3 = Label(window1,font=("Arial", 15), fg="black", text="").pack()
 def save_user_pass():
     List_user_Pass.append(entry_3.get()+entry_4.get())
     showList()
     window1.destroy()
 button_3 = Button(window1, text="Sign up", font=("Arial", 15), fg="black", bg="cyan", command=save_user_pass).pack()

label_1 = Label(window,font = ("Arial", 15), fg = "black", text = "username").pack()
entry_1 =Entry(window,font = ("Arial", 15), fg = "black")
entry_1.pack()
label_2 = Label(window,font = ("Arial", 15), fg = "black", text = "password").pack()
entry_2 =Entry(window,font = ("Arial", 15), fg = "black", show = "*")
entry_2.pack()
blank_1 = Label(window,font = ("Arial", 15), fg = "black", text = "").pack()
def ktra():
    check(entry_1.get(),entry_2.get())

button_1 =Button(window,text = "Log in", font = ("Arial", 15), fg = "black", command =ktra).pack()
blank_2 = Label(window,font = ("Arial", 15), fg = "black", text = "").pack()
button_2 = Button(window,text = "Sign up", font = ("Arial", 15), fg = "black", bg = "cyan", command = resgister)
button_2.pack()


window.mainloop()

