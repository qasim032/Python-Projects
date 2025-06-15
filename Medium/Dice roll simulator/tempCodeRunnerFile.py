        
     set_appearance_mode("Dark")
     set_default_color_theme("blue")

     app = CTk()
     app.geometry("600x600")
     app.title("Dice Roll Simulator")

     # banner
     banner = CTkLabel(master=app, text="Dice Roll Simulator", font=("Arial", 24, "bold"), text_color="#8B1740")
     banner.place(relx=0.5, rely=0.1, anchor="center")

     # Initial image label placeholder
     img_label = None

     # Button
     btn = CTkButton(master=app, text="Roll the Dice", command=rolldice, corner_radius=32, fg_color="#8B1740", hover_color="#059FFF")
     btn.place(relx=0.5, rely=0.65, anchor="center")




