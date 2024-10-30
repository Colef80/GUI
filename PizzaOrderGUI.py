import tkinter as tk
import tkinter.messagebox
import re

class PizzaOrderGUI:
    def __init__(self):
        #Main Window
        self.main_window = tk.Tk()
        self.main_window.geometry('625x950')
        self.main_window.title('Pizza Order Form')
        self.main_window.configure(bg='black')

        #Format Frames
        self.top_frame = tk.Frame(self.main_window, bg='gold')
        self.name_frame = tk.Frame(self.main_window, bg='black')
        self.address1_frame = tk.Frame(self.main_window, bg='black')
        self.address2_frame = tk.Frame(self.main_window, bg='black')
        self.option_frame = tk.Frame(self.main_window, bg='black')
        self.topping_frame = tk.Frame(self.main_window, bg='black')
        self.sauce_frame = tk.Frame(self.main_window, bg='black')
        self.lower_frame = tk.Frame(self.main_window, bg='black')
        self.button_frame = tk.Frame(self.main_window, bg='black')

        #Welcome Message
        self.welcome = tk.Label(self.top_frame, bg='green', fg='gold', font=('Cambria', 26, 'bold'), text='Welcome to the Baylor Pizza Bar!')
        self.welcome.pack()
        self.welcome2 = tk.Label(self.top_frame, bg='black', fg='gold', font=('Cambria', 22), text='Fill Out This Order Form To Build Your Own Pizza!')
        self.welcome2.pack()

        #Customer Details
        self.customerheader = tk.Label(self.name_frame, bg='black', fg='green', font=('Cambria', 20, 'bold', 'underline'), text='Customer Details')
        self.customerheader.pack()
        self.nprompt = tk.Label(self.name_frame, bg='black', fg='white', font=('Cambria', 12), text='Enter Your Name: ')
        self.name_entry = tk.Entry(self.name_frame, bg='light grey', font=('Cambria', 12), width=18)
        self.nprompt.pack(side='left')
        self.name_entry.pack(side='left')

        self.aprompt = tk.Label(self.address1_frame, bg='black', fg='white', font=('Cambria', 12), text='Street Address: ')
        self.address_entry = tk.Entry(self.address1_frame, bg='light grey', font=('Cambria', 12), width=20)
        self.aprompt.pack(side='left')
        self.address_entry.pack(side='left')

        self.cprompt = tk.Label(self.address2_frame, bg='black', fg='white', font=('Cambria', 12), text='City: ')
        self.city_entry = tk.Entry(self.address2_frame, bg='light grey', font=('Cambria', 12), width=10)
        self.cprompt.pack(side='left')
        self.city_entry.pack(side='left')

        self.sprompt = tk.Label(self.address2_frame, bg='black', fg='white', font=('Cambria', 12), text=' State(Abbreviation): ')
        self.state_entry = tk.Entry(self.address2_frame, bg='light grey', font=('Cambria', 12), width=2)
        self.sprompt.pack(side='left')
        self.state_entry.pack(side='left')

        self.zprompt = tk.Label(self.address2_frame, bg='black', fg='white', font=('Cambria', 12), text=' ZIP Code: ')
        self.zip_entry = tk.Entry(self.address2_frame, bg='light grey', font=('Cambria', 12), width=5)
        self.zprompt.pack(side='left')
        self.zip_entry.pack(side='left')


        #Pizza Options
        self.pheader = tk.Label(self.option_frame, bg='black', fg='Green', font=('Cambria', 20, 'bold', 'underline'), text='Pizza Order')
        self.pheader.pack()

        #Size
        self.sizeheader = tk.Label(self.option_frame, bg='black', fg='Gold', font=('Cambria', 15, ), text='Pizza Size:')
        self.sizeheader.pack()
        self.size_var = tk.DoubleVar()

        self.rbs = tk.Radiobutton(self.option_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Small ($7.99)',
                                    variable=self.size_var,
                                    value=7.99)
                                    
        
        self.rbm = tk.Radiobutton(self.option_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Medium ($10.99)',
                                    variable=self.size_var,
                                    value=10.99)
                                    
                
        self.rbl = tk.Radiobutton(self.option_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Large ($13.99)',
                                    variable=self.size_var,
                                    value=13.99)
                                    
        self.rbs.pack()
        self.rbm.pack()
        self.rbl.pack()
        
        #Toppings
        self.toppingheader = tk.Label(self.topping_frame, bg='black', fg='Gold', font=('Cambria', 15), text='Select Toppings:')
        self.toppingheader.pack()
        self.cb1 = tk.DoubleVar()
        self.cb2 = tk.DoubleVar()
        self.cb3 = tk.DoubleVar()
        self.cb4 = tk.DoubleVar()
        self.cb5 = tk.DoubleVar()
        self.cb6 = tk.DoubleVar()
        self.cb7 = tk.DoubleVar()
        self.cb8 = tk.DoubleVar()
        self.cb9 = tk.DoubleVar()

        self.topping_var = [self.cb1, self.cb2, self.cb3, self.cb4, self.cb5, self.cb6, self.cb7, self.cb8, self.cb9]



        self.cbox1 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Pepperoni ($1.50)',
                                    variable=self.cb1)
        
        self.cbox2 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Sausage ($1.50)',
                                    variable=self.cb2)
        
        self.cbox3 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Bacon ($1.50)',
                                    variable=self.cb3)
        self.cbox4 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Chicken ($1.50)',
                                    variable=self.cb4)
        
        self.cbox5 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Olives ($1.50)',
                                    variable=self.cb5)
        
        self.cbox6 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Peppers ($1.50)',
                                    variable=self.cb6)
        self.cbox7 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Anchovies ($1.50)',
                                    variable=self.cb7)
        
        self.cbox8 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Pineapple ($1.50)',
                                    variable=self.cb8)
        
        self.cbox9 = tk.Checkbutton(self.topping_frame, activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    text='Extra Cheese ($1.50)',
                                    variable=self.cb9)
        
        self.cbox1.pack()
        self.cbox2.pack()
        self.cbox3.pack()
        self.cbox4.pack()
        self.cbox5.pack()
        self.cbox6.pack()
        self.cbox7.pack()
        self.cbox8.pack()
        self.cbox9.pack()


        #Sauce Menu
        self.methodheader = tk.Label(self.sauce_frame, bg='black', fg='Gold', font=('Cambria', 15), text='Choose Your Sauce:')
        self.methodheader.pack()

        self.sauces = ["Tomato ($0.00)", "Marinara ($0.00)", "White ($1.00)", "Red (Spicy) ($1.00)", "Alfredo ($1.00)", "Pesto ($2.00)"]
        self.clicked = tk.StringVar()
        self.clicked.set(self.sauces[0])

        self.sauce_menu = tk.OptionMenu(self.sauce_frame, self.clicked, *self.sauces)
        self.sauce_menu.config(width=14, bg='black', activebackground='gold', fg='white', font=('Cambria', 12))
        self.sauce_menu.pack()

        #Delivery/Pickup
        self.methodheader = tk.Label(self.lower_frame, bg='black', fg='Gold', font=('Cambria', 15), text='Recival Method:')
        self.methodheader.pack()
        self.method_var = tk.DoubleVar()

        self.rbd = tk.Radiobutton(self.lower_frame,
                                    text='Delivery ($2.25)', activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    variable=self.method_var,
                                    value=2.25)
        
        self.rbp = tk.Radiobutton(self.lower_frame,
                                    text='Pickup ($0.00)', activebackground='gold', selectcolor='black', bg='black', fg='white', font=('Cambria', 12),
                                    variable=self.method_var,
                                    value=0)
        
        self.rbd.pack(side='left')
        self.rbp.pack(side='right')


        #Submit
        self.submit_button = tk.Button(self.button_frame, bg='green', fg='white', activebackground='gold', font=('Cambria', 14, "bold"), text='Submit Order', command=self.confirm_message)
        self.submit_button.pack()
    

        #Pack
        self.top_frame.pack()
        self.name_frame.pack(pady=8)
        self.address1_frame.pack()
        self.address2_frame.pack(pady=8)
        self.option_frame.pack()
        self.topping_frame.pack(pady=10)
        self.sauce_frame.pack()
        self.lower_frame.pack(pady=16)
        self.button_frame.pack(pady=10)


        tk.mainloop()

    #Count Toppings
    def count_toppings(self):
        count = 0
        for i in self.topping_var:
            if i.get() == 1:
                count += 1
        return count
    
    def sauce_cost(self, sauces):
        for i in range(len(self.sauces)):
            if self.sauces[i] == self.clicked.get():
                sauce = str(self.clicked.get())
        cost = [int(x) for x in sauce if x.isdigit()]
        sauce_cost = float(cost[0])
        return sauce_cost

    #Calculate Total
    def calc_total(self):
        size = self.size_var.get()
        toppings = self.count_toppings() * 1.50
        delivery = self.method_var.get()
        saucecost = self.sauce_cost(self.sauces)
        total = (size + toppings + saucecost + delivery)*1.0825
        return total

    #Confirmation Message
    def confirm_message(self):
        tk.messagebox.showinfo('Order Confirmation', f'Order Details For {self.name_entry.get()}\n \nAddress: {self.address_entry.get()} \n{self.city_entry.get()}, {self.state_entry.get()} {self.zip_entry.get()}\n \nTotal Cost: ${self.calc_total():.2f}')
        tk.messagebox.showinfo(f'Thank You For Your Business {self.name_entry.get()}!', f'We Look Forward To Serving You Again Soon!', command=self.main_window.destroy())

pizza_order = PizzaOrderGUI()

print('Enjoy Your Pizza!')