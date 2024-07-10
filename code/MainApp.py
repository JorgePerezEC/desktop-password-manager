import customtkinter as ctk
from tkinter import *
from ctypes import windll
from PIL import Image
import os

from components.login_page import LoginPage
from components.main_page import MainPage

class App(ctk.CTk):
    width = 1000
    height = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ISTER Password Manager")
        self.overrideredirect(True)
        self.center_window()
        self.resizable(False, False)
        self.minimized = False
        self.maximized = False

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/img/background.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=1, column=0, sticky="nsew")

        self.create_title_bar()

        self.login_page = LoginPage(self)
        self.login_page.grid(row=1, column=0, sticky="nsew")
    
    def create_title_bar(self):
        title_bar = ctk.CTkFrame(self, height=20, bg_color="#2A3D62")
        title_bar.grid(row=0, column=0, sticky="ew")
        # Add custom buttons to the title bar
        minimize_button = ctk.CTkButton(title_bar, text="", width=14, height=14, command=self.minimize, corner_radius=7, fg_color="#61C554", hover_color="#448F3A")
        minimize_button.pack(side='left', padx=5, pady=5)

        close_button = ctk.CTkButton(title_bar, text="", width=14, height=14, command=self.close, corner_radius=7, fg_color="#ED695E", hover_color="#DA4C40")
        close_button.pack(side='left', padx=2, pady=5)

        # Allow dragging the window
        title_bar.bind("<ButtonPress-1>", self.start_move)
        title_bar.bind("<B1-Motion>", self.do_move)
        title_bar_title = ctk.CTkLabel(title_bar, text=self.title, bg_color="#10121f", fg_color='white', font=("helvetica", 10))
        title_bar_title.pack(side=LEFT, padx=10)

        # Some settings Important to show app
        self.bind("<FocusIn>", self.deminimize)
        self.after(10, lambda: self.set_app_window(self))

    def set_app_window(self, main_window):
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        hwnd = windll.user32.GetParent(main_window.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
        self.wm_withdraw()
        self.after(10, lambda: self.wm_deiconify())

    def close(self):
        self.destroy()

    def minimize(self):
        self.attributes("-alpha", 0)
        self.minimized = True

    def deminimize(self, event):
        self.focus()
        self.attributes("-alpha", 1)
        if self.minimized:
            self.minimized = False
            self.return_to_taskbar()

    def return_to_taskbar(self):
        self.overrideredirect(True)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.winfo_pointerx() - self.x
        y = self.winfo_pointery() - self.y
        self.geometry(f"+{x}+{y}")

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def show_main_page(self):
        self.login_page.grid_forget()
        self.main_page = MainPage(self)
        self.main_page.grid(row=1, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.iconbitmap("img/ico/app_logo.ico")
    app.mainloop()
