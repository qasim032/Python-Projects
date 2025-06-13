from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

filename = None

def new_file():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
def save_file():
    global filename
    
    