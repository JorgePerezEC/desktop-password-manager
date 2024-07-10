from customtkinter import *     #GUI library
from PIL import Image           #Image library
from classes.cls_app import App

# app = CTk()
app = App()
"""
Main app settings
"""

#Main frame
main_frame = CTkFrame(master=app, bg_color="red")
main_frame.pack(fill='both', expand=True)
# Subframe 1 - Columna izquierda
# subframe1 = CTkFrame(master=main_frame, fg_color="#2A3E65")
scrollable_frame_left = CTkScrollableFrame(master=main_frame, fg_color="#2A3E65", )
scrollable_frame_left.place(relx=0.5, rely=1, anchor= S)
scrollable_frame_left.pack(side='left', fill='both', expand=True)

# Subframe 2 - Columna central
subframe2 = CTkFrame(master=main_frame, fg_color="#2A3D62")
subframe2.pack(side='left', fill='both', expand=True)

# Subframe 3 - Columna derecha
subframe3 = CTkFrame(master=main_frame, fg_color="#1A2650")
subframe3.pack(side='left', fill='both', expand=True)

# frame = CTkFrame(master=app, fg_color="#2A3D62",border_width=2)
# frame.pack(expand=True)

app.mainloop()