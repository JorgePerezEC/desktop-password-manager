import customtkinter
from PIL import Image
from ctypes import windll
import os
from components.login_page import LoginPage
from components.main_page import MainPage

class App(customtkinter.CTk):
    width = 1000
    height = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ISTER Password Manager")
        self.center_window()
        self.resizable(False, False)
        self.overrideredirect(True)
        self.minimized = False
        self.maximized = False

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/img/background.jpg"), size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=1, column=0, sticky="nsew")

        self.title_bar = customtkinter.CTkFrame(self, height=20, fg_color="#2A3D62")
        self.title_bar.grid(row=0, column=0, sticky="ew")

        self.minimize_button = customtkinter.CTkButton(self.title_bar, text="", width=14, height=14, command=self.minimize, corner_radius=7, fg_color="#61C554", hover_color="#448F3A")
        self.minimize_button.pack(side='left', padx=5, pady=5)

        self.close_button = customtkinter.CTkButton(self.title_bar, text="", width=14, height=14, command=self.close, corner_radius=7, fg_color="#ED695E", hover_color="#DA4C40")
        self.close_button.pack(side='left', padx=2, pady=5)

        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)

        self.login_page = LoginPage(self, self.show_main_page)
        self.main_page = MainPage(self, self.show_login_page)

        # self.show_login_page()

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

    def show_login_page(self):
        self.main_page.pack_forget()
        # self.login_page.pack(fill="both", expand=True)
        self.login_page.grid(row=1, column=0, sticky="ns")


    def show_main_page(self):
        self.login_page.pack_forget()
        self.main_page.grid(row=1, column=0, sticky="nsew", padx=100)
        
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

    # Window manipulation methods

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

if __name__ == "__main__":
    app = App()
    app.iconbitmap("img/ico/app_logo.ico")
    app.mainloop()
