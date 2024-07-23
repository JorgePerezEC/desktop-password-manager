import customtkinter as ctk

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, on_back):
        super().__init__(parent)

        self.parent = parent
        self.on_back = on_back
        self.create_widgets()

    def create_widgets(self):
        self.main_label = ctk.CTkLabel(self, text="CustomTkinter\nMain Page", font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(self, width=200, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.on_back, width=200)
        self.back_button.pack(pady=10)
