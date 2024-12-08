import tkinter as tk
from gui.settings import SettingsWindow
from gui.logger import LoggerWindow

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PumpFun Bot")
        self.root.geometry("800x600")
        self._setup_ui()

    def _setup_ui(self):
        tk.Button(self.root, text="Settings", command=self.open_settings).pack(pady=10)
        tk.Button(self.root, text="Logs", command=self.open_logs).pack(pady=10)
        tk.Button(self.root, text="Start Bot", command=self.start_bot).pack(pady=10)

    def open_settings(self):
        SettingsWindow()

    def open_logs(self):
        LoggerWindow()

    def start_bot(self):
        print("Bot started")

    def run(self):
        self.root.mainloop()
