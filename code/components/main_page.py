import customtkinter as ctk
from tkinter import BOTH, LEFT, RIGHT, X

class MainPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Main Page", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        self.main_label = ctk.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        
        self.back_button = ctk.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    def back_event(self):
        # Define actions for the back button
        pass