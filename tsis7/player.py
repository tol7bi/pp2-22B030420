from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('Music Player')
root.geometry("300x500")

pygame.mixer.init()

menu_bar = Menu(root)
root.config(menu=menu_bar)

songs = []
curr_song = ""
paused = False


def load_music():
    global curr_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        sl.insert("end", song)

    sl.selection_set(0)
    curr_song = songs[sl.curselection()[0]]


def play_music():
    global curr_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, curr_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True


def next_music():
    global curr_song, paused

    try:
        sl.selection_clear(0, END)
        sl.selection_set(songs.index(curr_song) + 1)
        curr_song = songs[sl.curselection()[0]]
        play_music()
    except:
        pass


def previous_music():
    global curr_song, paused

    try:
        sl.selection_clear(0, END)
        sl.selection_set(songs.index(curr_song) - 1)
        curr_song = songs[sl.curselection()[0]]
        play_music()
    except:
        pass


organise_menu = Menu(menu_bar)
organise_menu.add_command(label='Select Folder', command=load_music)
menu_bar.add_cascade(label='Organise', menu=organise_menu)


sl = Listbox(root, bg="green", fg="white", width=70, height=25)
sl.pack()


play_img = PhotoImage(file="img/play-button-arrowhead2.png")
next_img = PhotoImage(file="img/next2.png")
previous_img = PhotoImage(file="img/left-arrow2.png")
pause_img = PhotoImage(file="img/pause2.png")

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_img, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_img, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_img, borderwidth=0, command=next_music)
previous_btn = Button(control_frame, image=previous_img, borderwidth=0, command=previous_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
previous_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()