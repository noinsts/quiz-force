import tkinter as tk
from app.open_quiz import OpenTest
from app.create_quiz import CreateTest


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('QuizForce')

        tk.Label(text='QuizForce', font=20).pack(pady=10)

        buttons = {
            "Відкрити тест" : OpenTest,
            "Створити тест" : CreateTest
        }

        for text, cmd in buttons.items():
            tk.Button(self, text=text, command = lambda cls=cmd: cls(self)).pack(fill='x')


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()