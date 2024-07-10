import customtkinter as ctk
from tkinter import *
from ctypes import windll
from components.login_page import LoginPage
from components.main_page import MainPage

class App(ctk.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tk_title = "Password Manager"
        self.title(tk_title) 
        self.overrideredirect(True) 
        # self.geometry(f"{self.width}x{self.height}+75+75")
        self.center_window()
        self.resizable(False, False)
        self.minimized = False
        self.maximized = False

        # Title bar
        title_bar = ctk.CTkFrame(self, bg_color="#10121f")

        # Buttons
        close_button = ctk.CTkButton(title_bar, text='  x  ', command=self.destroy, bg_color="#10121f",
                                    font=("calibri", 13), fg_color='white')
        expand_button = ctk.CTkButton(title_bar, text=' 🗖 ', command=self.maximize_me, bg_color="#10121f",
                                        fg_color='white', font=("calibri", 13))
        minimize_button = ctk.CTkButton(title_bar, text=' 🗕 ', command=self.minimize_me, bg_color="#10121f",
                                         fg_color='white', font=("calibri", 13))
        title_bar_title = ctk.CTkLabel(title_bar, text=tk_title, bg_color="#10121f", fg_color='white', font=("helvetica", 10))

        # Window frame
        window = ctk.CTkFrame(self, bg_color="#25292e")

        # Pack the widgets
        title_bar.pack(fill=X)
        close_button.pack(side=RIGHT, ipadx=7, ipady=1)
        expand_button.pack(side=RIGHT, ipadx=7, ipady=1)
        minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
        title_bar_title.pack(side=LEFT, padx=10)
        window.pack(expand=1, fill=BOTH)

        # Window resize
        resize_x_widget = ctk.CTkFrame(window, bg_color="#25292e", cursor='sb_h_double_arrow')
        resize_x_widget.pack(side=RIGHT, ipadx=2, fill=Y)
        resize_x_widget.bind("<B1-Motion>", self.resize_x)

        resize_y_widget = ctk.CTkFrame(window, bg_color="#25292e", cursor='sb_v_double_arrow')
        resize_y_widget.pack(side=BOTTOM, ipadx=2, fill=X)
        resize_y_widget.bind("<B1-Motion>", self.resize_y)

        # Some settings
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
        main_window.wm_withdraw()
        main_window.after(10, lambda: main_window.wm_deiconify())

    def minimize_me(self):
        self.attributes("-alpha", 0)
        self.minimized = True

    def deminimize(self, event):
        self.focus() 
        self.attributes("-alpha", 1)
        if self.minimized:
            self.minimized = False                              

    def maximize_me(self):
        if not self.maximized:
            self.normal_size = self.geometry()
            self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
            self.maximized = True 
        else:
            self.geometry(self.normal_size)
            self.maximized = False

    def resize_x(self, event):
        x_win = self.winfo_x()
        difference = (event.x_root - x_win) - self.winfo_width()
        if self.winfo_width() > 150:
            try:
                self.geometry(f"{self.winfo_width() + difference}x{self.winfo_height()}")
            except:
                pass
        else:
            if difference > 0:
                try:
                    self.geometry(f"{self.winfo_width() + difference}x{self.winfo_height()}")
                except:
                    pass

    def resize_y(self, event):
        y_win = self.winfo_y()
        difference = (event.y_root - y_win) - self.winfo_height()
        if self.winfo_height() > 150:
            try:
                self.geometry(f"{self.winfo_width()}x{self.winfo_height() + difference}")
            except:
                pass
        else:
            if difference > 0:
                try:
                    self.geometry(f"{self.winfo_width()}x{self.winfo_height() + difference}")
                except:
                    pass

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
    app.mainloop()






# import customtkinter
# import os

# customtkinter.set_default_color_theme('./theme/dark-blue.json')

# class App(customtkinter.CTk):
#     width = 900
#     height = 600

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.title("ISTER Password Manager")
#         self.geometry(f"{self.width}x{self.height}")
#         self.resizable(False, False)
#         self.overrideredirect(True)

#         # Create a frame for the custom title bar
#         self.title_bar = customtkinter.CTkFrame(self, height=40, fg_color="#2A3D62")
#         self.title_bar.pack(fill='x')

#         # Add custom buttons to the title bar
#         self.minimize_button = customtkinter.CTkButton(self.title_bar, text="", width=14, height=14,
#                                                        command=self.minimize, corner_radius=7,
#                                                        fg_color="#61C554", hover_color="#448F3A")
#         self.minimize_button.pack(side='left', padx=5, pady=5)

#         self.close_button = customtkinter.CTkButton(self.title_bar, text="", width=14, height=14,
#                                                     command=self.destroy, corner_radius=7,
#                                                     fg_color="#ED695E", hover_color="#DA4C40")
#         self.close_button.pack(side='left', padx=2, pady=5)

#         # Allow dragging the window
#         self.title_bar.bind("<ButtonPress-1>", self.start_move)
#         self.title_bar.bind("<B1-Motion>", self.do_move)

#         # Add label in the center
#         self.label = customtkinter.CTkLabel(self, text="Password Manager", font=customtkinter.CTkFont(size=20, weight="bold"))
#         self.label.pack(expand=True)

#         # Ensure the window shows in the taskbar
#         self.iconbitmap("img/ico/app_logo.ico")  # Asegúrate de proporcionar la ruta correcta a tu ícono
#         self.after(0, self.ensure_taskbar_visibility)

#     def ensure_taskbar_visibility(self):
#         self.overrideredirect(False)
#         self.after(0, self.add_custom_title_bar)

#     def add_custom_title_bar(self):
#         self.overrideredirect(True)

#     def minimize(self):
#         self.overrideredirect(False)
#         self.iconify()

#     def start_move(self, event):
#         self.x = event.x
#         self.y = event.y

#     def do_move(self, event):
#         x = self.winfo_pointerx() - self.x
#         y = self.winfo_pointery() - self.y
#         self.geometry(f"+{x}+{y}")

# if __name__ == "__main__":
#     app = App()
#     # app.iconbitmap("img/ico/app_logo.ico")  # Asegúrate de proporcionar la ruta correcta a tu ícono
#     app.mainloop()
