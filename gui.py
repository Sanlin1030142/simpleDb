import tkinter as tk
from tkinter import scrolledtext
import sys
import database

class TextRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, string):
        self.widget.insert(tk.END, string)
        self.widget.see(tk.END)  # 滾動到底部

    def flush(self):
        pass  # 在這個例子中不需要實現



# 初始化GUI視窗
window = tk.Tk()
window.title("Database Operations GUI")

text_area = scrolledtext.ScrolledText(window, width=80, height=20)
text_area.pack()

# 重定向標準輸出到 text_area
sys.stdout = TextRedirector(text_area)

print_tables_button = tk.Button(window, text="Print Tables", command=database.print_tables)
print_tables_button.pack()

window.mainloop()
