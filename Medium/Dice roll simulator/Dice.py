from customtkinter import *
import random
from PIL import Image
from customtkinter import CTkImage

def rolldice():
    images = [
        "D:/Python-Projects/Medium/Dice roll simulator/01.PNG",
        "D:/Python-Projects/Medium/Dice roll simulator/02.PNG",
        "D:/Python-Projects/Medium/Dice roll simulator/03.PNG",
        "D:/Python-Projects/Medium/Dice roll simulator/04.PNG",
        "D:/Python-Projects/Medium/Dice roll simulator/05.PNG",
        "D:/Python-Projects/Medium/Dice roll simulator/06.PNG"
    ]
    
    img = Image.open(random.choice(images))
    img = img.resize((200, 200))
    ctk_img = CTkImage(light_image=img, size=(200, 200))

    global img_label
    if img_label:
        img_label.destroy()

    img_label = CTkLabel(master=app, image=ctk_img, text="") 
    img_label.image = ctk_img 
    img_label.place(relx=0.5, rely=0.4, anchor="center")


set_appearance_mode("Dark")
set_default_color_theme("blue")
img_label = None  
app = CTk()
app.geometry("600x600")
app.title("Dice Roll Simulator")
banner = CTkLabel(master=app, text="Dice Roll Simulator", font=("Arial", 24, "bold"), text_color="#8B1740")
banner.place(relx=0.5, rely=0.1, anchor="center")
btn = CTkButton(master=app, text="Roll the Dice", command=rolldice, corner_radius=32, fg_color="#8B1740", hover_color="#059FFF")
btn.place(relx=0.5, rely=0.65, anchor="center")
btnExit = CTkButton(master=app, text="Exit", command=app.destroy, corner_radius=32, fg_color="#8B1740", hover_color="#059FFF")
btnExit.place(relx=0.5, rely=0.75, anchor="center")

# Run
app.mainloop()
