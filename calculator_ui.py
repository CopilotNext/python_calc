import tkinter as tk

class CalculatorUI:
    def __init__(self, calculator_service):
        self.calculator_service = calculator_service
        self.window = tk.Tk()
        self.window.title('计算器')
        self.window.geometry('300x400')
        self.window.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        # 显示框
        self.display = tk.Entry(self.window, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        # 按钮文本
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # 创建并放置按钮
        r = 1
        c = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.window, text=button, width=5, height=2,
                     command=cmd).grid(row=r, column=c, padx=2, pady=2)
            c += 1
            if c > 3:
                c = 0
                r += 1

        # 添加清除按钮
        tk.Button(self.window, text='C', width=5, height=2,
                 command=self.clear).grid(row=5, column=0, columnspan=4, padx=2, pady=2)

        # 配置网格权重
        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            expression = self.display.get()
            result = self.calculator_service.calculate(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        else:
            self.display.insert(tk.END, key)

    def clear(self):
        self.display.delete(0, tk.END)

    def run(self):
        self.window.mainloop()
