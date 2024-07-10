import customtkinter as ctk
from tkinter import BOTH, LEFT, RIGHT, X

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.grid(row=1, column=0, sticky="ns")
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="PASSWORD MANAGER\nLogin Page", 
                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = ctk.CTkEntry(self, width=200, placeholder_text="Username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = ctk.CTkEntry(self, width=200, show="*", placeholder_text="Password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def login(self):
        # Aquí puedes añadir la lógica de autenticación
        self.grid_forget()
        self.parent.show_main_page()
