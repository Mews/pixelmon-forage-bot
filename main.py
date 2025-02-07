import keyboard
import pydirectinput as pdi
from time import sleep as wait
import ttkbootstrap as ttk


def forage(g_press_num:int = 5):
    for _ in range(g_press_num):
        keyboard.press("G")
        wait(0.1)
    
    pdi.press("DOWN")
    wait(0.5)



class Options(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.default_options = {
            "g_presses": 5,                             # G presses per forage operation
            "g_press_delay": 0.1,                       # Seconds between G presses
            "forage_delay": 0.25,                       # Seconds between each forage operation
            "do_anti_afk_jump": True,                   # Whether or not to jump every 20 forage operations
            "forages_per_jump": 20,                     # How many forages it takes to do an afk jump
        }

        self.config(borderwidth=2, relief="groove")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.create_g_presses_frame()
        self.create_g_press_delay_frame()
        self.create_forage_delay_frame()
        self.create_anti_afk_jump_frame()
        self.create_forages_per_jump_frame()

    def create_g_presses_frame(self):
        self.g_presses_frame = ttk.Frame(self)

        self.master.options["g_presses"].set(self.default_options["g_presses"])

        int_validate_cmd = self.register(self.validate_int_input)

        self.g_presses_entry = ttk.Entry(
            self.g_presses_frame,
            validate="key",
            validatecommand=(int_validate_cmd, "%P"),
            font=("", 8),
            textvariable=self.master.options["g_presses"],
        )
        self.g_presses_entry.pack(side="bottom")

        ttk.Label(self.g_presses_frame, text="G presses per forage").pack(side="top")

        self.g_presses_frame.grid(row=0, column=0, padx=10, pady=10)

    def create_g_press_delay_frame(self):
        self.g_press_delay_frame = ttk.Frame(self)

        self.master.options["g_press_delay"].set(self.default_options["g_press_delay"])

        float_validate_cmd = self.register(self.validate_float_input)

        self.g_press_delay_entry = ttk.Entry(
            self.g_press_delay_frame,
            validate="key",
            validatecommand=(float_validate_cmd, "%P"),
            font=("", 8),
            textvariable=self.master.options["g_press_delay"],
        )
        self.g_press_delay_entry.pack(side="bottom")

        ttk.Label(self.g_press_delay_frame, text="G press delay (seconds)").pack(side="top")

        self.g_press_delay_frame.grid(row=2, column=0, padx=10, pady=10)

    def create_forage_delay_frame(self):
        self.forage_delay_frame = ttk.Frame(self)

        self.master.options["forage_delay"].set(self.default_options["forage_delay"])

        float_validate_cmd = self.register(self.validate_float_input)

        self.forage_delay_entry = ttk.Entry(
            self.forage_delay_frame,
            validate="key",
            validatecommand=(float_validate_cmd, "%P"),
            font=("", 8),
            textvariable=self.master.options["forage_delay"],
        )
        self.forage_delay_entry.pack(side="bottom")

        ttk.Label(self.forage_delay_frame, text="Forage delay (seconds)").pack(side="top")

        self.forage_delay_frame.grid(row=1, column=0, padx=10, pady=10)

    def create_anti_afk_jump_frame(self):
        self.anti_afk_jump_frame = ttk.Frame(self)

        self.master.options["do_anti_afk_jump"].set(self.default_options["do_anti_afk_jump"])

        self.anti_afk_jump_checkbutton = ttk.Checkbutton(
            self.anti_afk_jump_frame,
            text="Enable Anti-AFK jump",
            variable=self.master.options["do_anti_afk_jump"],
        )
        self.anti_afk_jump_checkbutton.pack(side="bottom")

        self.anti_afk_jump_frame.grid(row=0, column=1, padx=10, pady=10)
    
    def create_forages_per_jump_frame(self):
        self.forages_per_jump_frame = ttk.Frame(self)

        self.master.options["forages_per_jump"].set(self.default_options["forages_per_jump"])

        int_validate_cmd = self.register(self.validate_int_input)

        self.forages_per_jump_entry = ttk.Entry(
            self.forages_per_jump_frame,
            validate="key",
            validatecommand=(int_validate_cmd, "%P"),
            font=("", 8),
            textvariable=self.master.options["forages_per_jump"],
        )
        self.forages_per_jump_entry.pack(side="bottom")

        ttk.Label(self.forages_per_jump_frame, text="Forages between afk jumps").pack(side="top")

        self.forages_per_jump_frame.grid(row=1, column=1, padx=10, pady=10)
    
    
    def validate_int_input(self, x:str):
        if x == "":
            return True
        try:
            int(x)
            return True
        except:
            return False

    def validate_float_input(self, x:str):
        if x == "":
            return True
        try:
            float(x)
            return True
        except ValueError:
            return False





class Controls(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.config(borderwidth=2, border=2, relief="groove")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.hotkey = "F7"
        self.create_start_frame()

    """
    def create_hotkey_frame(self):
        self.hotkey_frame = ttk.Frame(self)

        self.new_hotkey_button = ttk.Button(self.hotkey_frame, text="Change hotkey")
        self.new_hotkey_button.pack(side="left", padx=10, pady=10)

        self.hotkey_label = ttk.Label(self.hotkey_frame, text=f"Current hotkey: {self.hotkey}")
        self.hotkey_label.pack(side="right", padx=10, pady=10)

        self.hotkey_frame.grid(row=0, column=0, padx=10, pady=(0,10))
    """

    def create_start_frame(self):
        self.start_frame = ttk.Frame(self)

        self.start_button = ttk.Button(self.start_frame, text="Start (F7)", state="normal", command=self.master.start_button)
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = ttk.Button(self.start_frame, text="Stop (F7)", state="disabled", command=self.master.stop_button)
        self.stop_button.pack(side="left", padx=10, pady=10)

        self.start_frame.grid(row=1, column=0, padx=10, pady=10)
    

    def update_buttons(self, started):
        if started:
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
        else:
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")







class App(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.started = False
        self.last_forage_time = 0
        self.forage_count = 0

        self.options = {
            "g_presses": ttk.StringVar(self),           # G presses per forage operation
            "g_press_delay": ttk.StringVar(self),       # Seconds between G presses
            "forage_delay": ttk.StringVar(self),        # Seconds between each forage operation
            "do_anti_afk_jump": ttk.BooleanVar(self),   # Whether or not to jump every 20 forage operations
            "forages_per_jump": ttk.StringVar(self),    # How many forages it takes to do an afk jump
        }

        keyboard.add_hotkey("F7", self.hotkey_pressed)

        self.title("Pixelmon forage bot")
        self.geometry("600x600")
        self.resizable(0, 0)
        self.iconbitmap("assets/forage.ico")
        
        self.rowconfigure(0, uniform="xyz", weight=3)
        self.rowconfigure(1, uniform="xyz", weight=4)
        self.columnconfigure(0, weight=1)

        self.options_frame = Options(self)
        self.options_frame.grid(column=0, row=0, sticky="NSWE", padx=10, pady=10)

        self.controls_frame = Controls(self)
        self.controls_frame.grid(column=0, row=1, sticky="NSWE", padx=10, pady=(0,10))


        self.after(100, self.loop)
    

    def start_button(self):
        self.started = True

        self.controls_frame.update_buttons(self.started)


    def stop_button(self):
        self.started = False

        self.controls_frame.update_buttons(self.started)

    
    def hotkey_pressed(self):
        self.started = not self.started

        self.controls_frame.update_buttons(self.started)

    
    def loop(self):
        if self.started:
            forage(int(self.options["g_presses"].get()))
            self.forage_count += 1

            if self.forage_count % int(self.options["forages_per_jump"].get()) == 0 and self.options["do_anti_afk_jump"].get():
                for _ in range(3):
                    pdi.press("space")
                    wait(0.5)

        self.after(100, self.loop)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
