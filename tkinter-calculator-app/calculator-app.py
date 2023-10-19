from tkinter import *

def choice():
    accepted.config(text=str(on_or_off.get()))

main_window = Tk()
main_window.geometry("500x500")

on_or_off = BooleanVar()
check = Checkbutton(main_window, text="Accept T&Cs", variable=on_or_off, command=choice)
check.pack()

accepted = Label(main_window)
accepted.pack()

main_window.mainloop()