import tkinter as tk
from tkinter import messagebox


class CreateTest(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Створити тест')

        buttons = {
            "Вкажіть назву тесту" : tk.Entry(self),
            "Вкажіть кількість запитань" : tk.Entry(self)
        }

        for text, entry in buttons.items():
            tk.Label(self, text=text).pack(pady=10)
            entry.pack()

        self.entries = buttons

        tk.Button(self, text='Продовжити', command=self.create_table, bg='green', fg='white').pack(pady=10)


    def create_table(self):
        self.name = self.entries['Вкажіть назву тесту'].get()
        self.count = self.entries['Вкажіть кількість запитань'].get()

        if not self.name or not self.count:
            messagebox.showerror(title='Помилка', message='Ви не заповнили всі поля')
            return

        try:
            self.count = int(self.count)

            if self.count <= 0:
                messagebox.showerror(title='Помилка', message='Кількість запитань повинна бути більше 0')
                return
        except ValueError:
            messagebox.showerror(title='Помилка', message='Кількість запитань не є числом')
            return

        self.withdraw()
        QuestionForm(self)


class QuestionForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Створення тесту')

        self.name = parent.name
        self.count = parent.count

        for i in range(self.count):
            forms = {
                "Введіть запитання" : tk.Entry(self),
                "Введіть відповідь" : tk.Entry(self)
            }

            for text, entry in forms.items():
                tk.Label(self, text=text).pack(pady=10)
                entry.pack()

        tk.Button(self, text='Підтвердити', bg='green', fg='white').pack(pady=10)