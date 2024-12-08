import tkinter as tk
from tkinter import messagebox

class SettingsWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Settings")
        self.window.geometry("400x300")
        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.window, text="API Key:").pack(pady=10)
        tk.Entry(self.window).pack(pady=10)
        tk.Button(self.window, text="Save", command=self.save_settings).pack(pady=10)

    def save_settings(self):
        messagebox.showinfo("Settings", "Settings saved!")
