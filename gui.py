import tkinter as tk
import configparser
import os

def parse_rgb(rgb_string):
    """Convert 'R,G,B' string to a tkinter-friendly color."""
    try:
        r, g, b = [int(c.strip()) for c in rgb_string.split(",")]
        return f"#{r:02x}{g:02x}{b:02x}"
    except:
        return "#000000"

def load_theme(name="dark"):
    """Load a theme section from themes.ini"""
    path = os.path.join("data", "themes.ini")
    config = configparser.ConfigParser()
    config.read(path)
    
    if name not in config:
        print(f"Theme '{name}' not found.")
        return {}

    return {key: parse_rgb(val) for key, val in config[name].items()}

def launch_gui(theme_name="dark"):
    theme = load_theme(theme_name)
    if not theme:
        return

    root = tk.Tk()
    root.title("Abacus Theme Viewer")
    root.geometry("360x300")
    root.configure(bg=theme["col_bg"])

    # Labels using foregrounds
    tk.Label(root, text="Foreground 0", fg=theme["col_f0"], bg=theme["col_bg"]).pack(pady=5)
    tk.Label(root, text="Foreground 1", fg=theme["col_f1"], bg=theme["col_bg"]).pack(pady=5)
    tk.Label(root, text="Foreground 2", fg=theme["col_f2"], bg=theme["col_bg"]).pack(pady=5)

    canvas = tk.Canvas(root, width=300, height=100, bg=theme["col_bg"], highlightthickness=0)
    canvas.pack(pady=10)

    # Border line
    canvas.create_line(10, 10, 290, 10, fill=theme["col_bc"], width=2)
    # Market Up
    canvas.create_line(10, 40, 290, 40, fill=theme["col_mu"], width=2)
    # Market Down
    canvas.create_line(10, 70, 290, 70, fill=theme["col_md"], width=2)

    root.mainloop()
