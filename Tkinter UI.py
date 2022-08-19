from PIL import ImageTk,Image
import json
import customtkinter
import json

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Lava")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.iconbitmap('assets/rocket.ico')
        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180, fg_color='#1d1d1d',
                                                 corner_radius=16)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, fg_color='#1d1d1d', corner_radius=12)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=0)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, weight=0)  # empty row as spacing
        self.frame_left.grid_rowconfigure(0, minsize=0)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=0)  # empty row with minsize as spacing

        self.logo_img = ImageTk.PhotoImage(Image.open("assets/rocket.png"))

        self.my_label = customtkinter.CTkLabel(master=self.frame_left, image=self.logo_img, width=5, height=5)
        self.my_label.grid(row=1, column=0, pady=15, padx=0, sticky='nswe')

        self.lava_title = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Lava", width=5, height=0,
                                              text_color='red',
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lava_title.grid(row=0, column=0, pady=0, padx=0, sticky='w')

        self.goto_mines = customtkinter.CTkButton(master=self.frame_left,
                                                hover_color='#2d2d2d',
                                                text_font=("Roboto Medium", -25),
                                                text_color='Red',
                                                text="Credits", width=45, height=25, fg_color='#1d1d1d',
                                                command=self.create_toplevel)
        self.goto_mines.grid(row=8, pady=185, padx=20, sticky='nswe')

        self.goto_crash = customtkinter.CTkButton(master=self.frame_left,
                                                hover_color='#2d2d2d',
                                                text_font=("Roboto Medium", -25),
                                                text_color='Red',
                                                text="Crash", width=145, height=40, fg_color='#1d1d1d',
                                                command=self.open_crash_tab)
        self.goto_crash.grid(row=2, pady=5, padx=20, sticky='nswe')

        self.goto_mines = customtkinter.CTkButton(master=self.frame_left,
                                                hover_color='#2d2d2d',
                                                text_font=("Roboto Medium", -25),
                                                text_color='Red',
                                                text="Mines", width=145, height=40, fg_color='#1d1d1d',
                                                command=self.open_mines_tab)
        self.goto_mines.grid(row=3, pady=5, padx=20, sticky='nswe')
        self.goto_roulette = customtkinter.CTkButton(master=self.frame_left,
                                                hover_color='#2d2d2d',
                                                text_font=("Roboto Medium", -25),
                                                text_color='Red',
                                                text="Roulette", width=145, height=40, fg_color='#1d1d1d',
                                                command=self.open_roulette_tab)
        self.goto_roulette.grid(row=4, pady=5, padx=20, sticky='nswe')

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)
    
    def open_crash_tab(self):
        # everything you want to show when you click the crash tab should go in this function
        self.crash_test = customtkinter.CTkLabel(master=self.frame_right,
                                            text="Crash\n" + "Predictor", width=5, height=0, fg_color='#1d1d1d',
                                            text_color='Red',
                                            text_font=("Roboto Medium", -65))  # font name and size in px
        self.crash_test.grid(row=1, column=1, pady=15, padx=0, sticky='nswe')

    def open_mines_tab(self):
        self.mines_stuff = customtkinter.CTkLabel(master=self.frame_right,
                                            text="Mines\n", width=5, height=0, fg_color='#1d1d1d',
                                            text_color='Red',
                                            text_font=("Roboto Medium", -65))  # font name and size in px
        self.mines_stuff.grid(row=1, column=1, pady=15, padx=0, sticky='nswe')

        


    def open_roulette_tab(self):
        # everything you want to show when you click the roulette tab should go in this function
        self.roulette_stuff = customtkinter.CTkLabel(master=self.frame_right,
                                            text="Roulette", width=5, height=0, fg_color='#1d1d1d',
                                            text_color='Red',
                                            text_font=("Roboto Medium", -65))  # font name and size in px
        self.roulette_stuff.grid(row=1, column=1, pady=15, padx=0, sticky='nswe')
        
    def crash_predictBtn(self):
        print("Predict")
    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("260x150")
        window.iconbitmap('assets/rocket.ico')
        window.title('Lava Credits')
        label = customtkinter.CTkLabel(master=window, text="Geek#7216",text_font=("Roboto Medium", -35))
        label.grid(row=1, column=1, pady=15, padx=0, sticky='nswe')

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()