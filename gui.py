import tkinter as tk
import configparser
import os
import random

from utils import get_available_themes, set_theme
from panels import panel_main, panel_settings

def parse_rgb(rgb_string):
    try:
        r, g, b = [int(c.strip()) for c in rgb_string.split(",")]
        return f"#{r:02x}{g:02x}{b:02x}"
    except:
        return "#000000"

def get_current_theme_name():
    path = os.path.join("data", "settings.ini")
    config = configparser.ConfigParser()
    config.read(path)
    return config.get("App", "theme", fallback="dark")

def load_theme(name="dark"):
    path = os.path.join("data", "themes.ini")
    config = configparser.ConfigParser()
    config.read(path)

    if name not in config:
        print(f"Theme '{name}' not found. Falling back to 'dark'")
        name = "dark"

    return {key: parse_rgb(val) for key, val in config[name].items()}

def launch_gui():
    theme_name = get_current_theme_name()
    theme = load_theme(theme_name)

    root = tk.Tk()
    root.title("Abacus")
    root.geometry("640x480")
    root.configure(bg=theme["col_bg"])

    current_panel = {"widget": None}

    def switch_panel(panel_func):
        if current_panel["widget"] is not None:
            current_panel["widget"].destroy()
        new_panel = panel_func(root, theme, switch_panel)
        new_panel.pack(fill="both", expand=True)
        current_panel["widget"] = new_panel

    switch_panel(panel_main.get_panel)

    root.mainloop()
