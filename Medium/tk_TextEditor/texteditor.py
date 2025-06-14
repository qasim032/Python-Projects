from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

filename = None

def new_file():
    global filename
    filename = "Untitled"
    text.delete(0.0, END) # Clear the text area
    
def save_file():
    global filename
    t = text.get(0.0, END) # Get all text from the start(0,0) till the end
    f = open(filename,'w')
    f.write(t)
    f.close()

def save_As_file():
    f = asksaveasfile(mode='w', defaultextension=".txt") # Ask user for file name
    t = text.get(0.0, END) 
    try:
        f.write(t)
        f.close()
    except:
        showerror(title="Oops!", message="Unable to save file")

def open_file():
    f = askopenfile(mode='r') # Ask user for file to open
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("Qasim's Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=1280, height=720)
text = Text(root,width=400, height=400)
text.pack()

menubar = Menu(root) # Create a menu bar
filemenu = Menu(menubar) # Create a file menu
filemenu.add_command(label="New", command=new_file) 
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save As", command=save_As_file)
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu) 
root.config(menu=menubar) 
root.mainloop() 
