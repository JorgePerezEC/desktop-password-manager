import customtkinter
from PIL import Image
from ctypes import windll
import os

# customtkinter.set_default_color_theme('./theme/dark-blue.json')

class App(customtkinter.CTk):
    width = 1000
    height = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ISTER Password Manager")
        # self.geometry(f"{self.width}x{self.height}")
        self.center_window()
        self.resizable(False, False)
        self.overrideredirect(True)
        self.minimized = False
        self.maximized = False

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/img/background.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=1, column=0, sticky="nsew")

        # Create a frame for the custom title bar
        self.title_bar = customtkinter.CTkFrame(self, height=20, fg_color="#2A3D62")
        self.title_bar.grid(row=0, column=0, sticky="ew")

        # Add custom buttons to the title bar
        self.minimize_button = customtkinter.CTkButton(self.title_bar, text="", width=14, height=14, command=self.minimize, corner_radius=7, fg_color="#61C554", hover_color="#448F3A")
        self.minimize_button.pack(side='left', padx=5, pady=5)

        self.close_button = customtkinter.CTkButton(self.title_bar, text="", width=14, height=14, command=self.close, corner_radius=7, fg_color="#ED695E", hover_color="#DA4C40")
        self.close_button.pack(side='left', padx=2, pady=5)

        # Allow dragging the window
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=1, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="PASSWORD MANAGER\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="Username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

        # Some settings
        self.bind("<FocusIn>", self.deminimize)
        self.after(10, lambda: self.set_app_window(self))

    # def set_app_window(self, main_window):
    #     GWL_EXSTYLE = -20
    #     WS_EX_APPWINDOW = 0x00040000
    #     WS_EX_TOOLWINDOW = 0x00000080
    #     hwnd = windll.user32.GetParent(main_window.winfo_id())
    #     stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    #     stylew = stylew & ~WS_EX_TOOLWINDOW
    #     stylew = stylew | WS_EX_APPWINDOW
    #     res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    #     main_window.wm_withdraw()
    #     main_window.after(10, lambda: main_window.wm_deiconify())

    def set_app_window(self, main_window):
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        hwnd = windll.user32.GetParent(main_window.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
        # main_window.attributes("-alpha", 1)  # Oculta la ventana
        # main_window.minimized = True
        self.wm_withdraw()
        self.after(10, lambda: self.wm_deiconify())

    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=100)  # show main frame

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=1, column=0, sticky="ns")  # show login frame

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
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición de la ventana para que esté centrada
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2

        # Establecer la geometría de la ventana con la posición calculada
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")


if __name__ == "__main__":
    app = App()
    app.iconbitmap("img/ico/app_logo.ico")
    app.mainloop()
