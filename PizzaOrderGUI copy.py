import tkinter as tk
import tkinter.messagebox
import tkinter.ttk

class PizzaOrderGUI:
    def __init__(self):
        #Main Window
        self.main_window = tk.Tk()
        self.main_window.title('Pizza Order Form')


        #Welcome Message
        self.welcome = tk.Label(self.main_window, text='Welcome to Baylor Pizza Bar!\n')
        self.welcome.grid(row = 0, column = 0)



        tk.mainloop()

        #Confirmation Message
    def confirm_message(self):
        tk.messagebox.showinfo('Response', f'Name: {self.name_entry.get()} Address: {self.address_entry.get()} Total Cost: ')

pizza_order = PizzaOrderGUI()