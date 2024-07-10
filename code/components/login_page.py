import customtkinter as ctk
from tkinter import BOTH

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, on_login):
        super().__init__(parent)

        self.parent = parent
        self.on_login = on_login
        # self.pack(fill=BOTH, expand=True)
        self.grid(row=1, column=0, sticky="ns")
        self.create_widgets()

    def create_widgets(self):
        self.login_label = ctk.CTkLabel(self, text="PASSWORD MANAGER\nLogin Page", font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(self, width=200, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, width=200, show="*", placeholder_text="Password")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login_event, width=200)
        self.login_button.pack(pady=10)

    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())
        self.on_login()
