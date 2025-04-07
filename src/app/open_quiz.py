import tkinter as tk


class OpenTest(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Відкрити тест')