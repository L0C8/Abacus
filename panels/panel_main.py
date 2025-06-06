import tkinter as tk
from panels import panel_settings

def get_panel(parent, theme, switch_panel):
    frame = tk.Frame(parent, bg=theme["col_bg"])

    tk.Label(
        frame,
        text="Main Panel",
        fg=theme["col_f0"],
        bg=theme["col_bg"],
        font=("Arial", 16, "bold")
    ).pack(padx=20, pady=20)

    tk.Button(
        frame,
        text="Go to Settings",
        command=lambda: switch_panel(panel_settings.get_panel),
        fg=theme["col_f0"],
        bg=theme["col_b1"],
        activeforeground=theme["col_f1"],
        activebackground=theme["col_b3"],
        relief=tk.FLAT,
        bd=0,
        font=("Arial", 11)
    ).pack(pady=10)

    return frame
