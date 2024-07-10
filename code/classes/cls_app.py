import customtkinter as ctk

# Create App class
class App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("ISTER Password Manager")    
# Dimensions of the window will be 870px x 600px
        self.geometry("870x600")
        self.resizable(False,False)
        ctk.set_default_color_theme('./theme/dark-blue.json')