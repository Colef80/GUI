import tkinter as tk
import tkinter.messagebox

class PizzaOrderGUI:
    def __init__(self):
        #Main Window
        self.main_window = tk.Tk()
        self.main_window.geometry('590x600')
        self.main_window.title('Pizza Order Form')
        self.main_window.configure(bg='black')

        #Format Frames
        # self.top_frame = tk.Frame(self.main_window, bg='gold')
        # self.name_frame = tk.Frame(self.main_window, bg='black')
        # self.address_frame = tk.Frame(self.main_window, bg='black')
        # self.option_frame = tk.Frame(self.main_window, bg='black')
        # self.bottom_frame = tk.Frame(self.main_window, bg='black')

        #Welcome Message
        self.welcome = tk.Label(self.main_window, bg='green', fg='gold', font=('Cambria', 22, 'bold'), text='Welcome to the Baylor Pizza Bar!')
        self.welcome.grid(row=0)
        self.welcome2 = tk.Label(self.main_window, bg='black', fg='gold', font=('Cambria', 20), text='Fill Out The Order Form Below To Build Your Pizza')
        self.welcome2.grid(row=1)

        #Customer Details
        self.customerheader = tk.Label(self.main_window, bg='black', fg='green', font=('Cambria', 20, 'underline'), text='Customer Details')
        self.customerheader.grid(row=2)
        self.nprompt = tk.Label(self.main_window, bg='black', fg='white', font=('Cambria', 12), text='Enter Your Name: ')
        self.name_entry = tk.Entry(self.main_window, bg='light grey', font=('Cambria', 12), width=18)
        self.nprompt.grid(row=3, column=0)

        check_vars = []

        # Create checkboxes
        for i in range(5):
            self.var = tk.IntVar()
            check_vars.append(self.var)
            tk.Checkbutton(self.main_window, text=f"Option {i+1}", variable=self.var).pack()

        # Button to count checked checkboxes
        Button(self.main_window, text="Count Checked", command=count_checked).pack()

        # self.aprompt = tk.Label(self.main_window, bg='black', fg='white', font=('Cambria', 12), text='Street Address: ')
        # self.address_entry = tk.Entry(self.main_window, bg='light grey', font=('Cambria', 12), width=20)
        # self.aprompt.grid(row=0)
        # self.address_entry.pack(side='left')

        # self.cprompt = tk.Label(self.main_window, bg='black', fg='white', font=('Cambria', 12), text='City: ')
        # self.city_entry = tk.Entry(self.main_window, bg='light grey', font=('Cambria', 12), width=10)
        # self.cprompt.pack(side='left')
        # self.city_entry.pack(side='left')

        # self.sprompt = tk.Label(self.main_window, bg='black', fg='white', font=('Cambria', 12), text='State: ')
        # self.state_entry = tk.Entry(self.main_window, bg='light grey', font=('Cambria', 12), width=2)
        # self.sprompt.pack(side='left')
        # self.state_entry.pack(side='left')

        # self.zprompt = tk.Label(self.main_window, bg='black', fg='white', font=('Cambria', 12), text='ZIP Code: ')
        # self.zip_entry = tk.Entry(self.main_window, bg='light grey', font=('Cambria', 12), width=5)
        # self.zprompt.pack(side='left')
        # self.zip_entry.pack(side='left')


        # #Pizza Options
        # self.pheader = tk.Label(self.main_window, bg='black', fg='Green', font=('Cambria', 20, 'underline'), text='Pizza Order')
        # self.pheader.pack()

        # #Size
        # self.sizeheader = tk.Label(self.main_window, bg='black', fg='Gold', font=('Cambria', 15), text='Pizza Size')
        # self.sizeheader.pack()
        # self.size_var = tk.DoubleVar()

        # self.rbs = tk.Radiobutton(self.main_window, activebackground='gold', selectcolor='black', bg='black', fg='white',
        #                             text='Small ($7.99)',
        #                             variable=self.size_var,
        #                             value=7.99)
                                    
        
        # self.rbm = tk.Radiobutton(self.main_window, activebackground='gold', selectcolor='black', bg='black', fg='white',
        #                             text='Medium ($10.99)',
        #                             variable=self.size_var,
        #                             value=10.99)
                                    
                
        # self.rbl = tk.Radiobutton(self.main_window, activebackground='gold', selectcolor='black', bg='black', fg='white',
        #                             text='Large ($13.99)',
        #                             variable=self.size_var,
        #                             value=13.99)
                                    
        # self.rbs.pack()
        # self.rbm.pack()
        # self.rbl.pack()
        
        # #Toppings
        # self.toppingheader = tk.Label(self.main_window, bg='black', fg='Gold', font=('Cambria', 15), text='\nSelect Toppings')
        # self.toppingheader.pack()
        # self.cb1 = tk.DoubleVar()
        # self.cb2 = tk.DoubleVar()
        # self.cb3 = tk.DoubleVar()


        # self.cbox1 = tk.Checkbutton(self.main_window, activebackground='gold', selectcolor='black', bg='black', fg='white',
        #                             text='Pepperoni ($0.75)',
        #                             variable=self.cb1)
        
        # self.cbox2 = tk.Checkbutton(self.main_window, activebackground='gold', selectcolor='black', bg='black', fg='white',
        #                             text='Olives ($0.75)',
        #                             variable=self.cb2)
        
        # self.cbox3 = tk.Checkbutton(self.main_window, activebackground='gold', selectcolor='black', bg='black', fg='white',
        #                             text='Extra Cheese ($0.75)',
        #                             variable=self.cb3)
        
        # self.cbox1.pack()
        # self.cbox2.pack()
        # self.cbox3.pack()


        # #Sauce Menu
        # # self.sauceheader = tk.Label(self.option_frame, text='\nSelect Your Sauce')
        # # self.sauceheader.pack()

        # # options = [
        # #     'Tomato ($0.50)',
        # #     'Pesto ($1.00)',
        # #     'Alfredo ($1.00)']
        
        # # self.clicked = StringVar()

        # # self.clicked.set('Tomato ($0.50)')

        # # self.drop = OptionMenu(self.option_frame, clicked, *options)
        # # drop.pack()


        # #Delivery/Pickup
        # self.methodheader = tk.Label(self.main_window, bg='black', fg='Green', font=('Cambria', 20, 'underline'), text='Recival Method')
        # self.methodheader.pack()
        # self.method_var = tk.DoubleVar()

        # self.rbd = tk.Radiobutton(self.main_window,
        #                             text='Delivery ($2.25)', activebackground='gold', selectcolor='black', bg='black', fg='white',
        #                             variable=self.method_var,
        #                             value=2.25)
        
        # self.rbp = tk.Radiobutton(self.main_window,
        #                             text='Pickup ($0.00)', activebackground='gold', selectcolor='black', bg='black', fg='white',
        #                             variable=self.method_var,
        #                             value=0)
        
        # self.rbd.pack(side='left')
        # self.rbp.pack(side='right')


        # #Submit
        # self.submit_button = tk.Button(self.main_window, bg='green', activebackground='gold', text='Submit Order', command=self.confirm_message)
        # self.submit_button.pack(pady=10)
    

        # #Pack
        # # self.top_frame.pack()
        # # self.name_frame.pack()
        # # self.address_frame.pack(pady=12)
        # # self.option_frame.pack(pady=10)
        # # self.bottom_frame.pack()



        tk.mainloop()


    #Calc_Total
    def calc_total(self):
        size = self.size_var.get()
        delivery = self.method_var.get()
        total = size + delivery
        return total

    #Confirmation Message
    def confirm_message(self):
        tk.messagebox.showinfo('Response', f'Order Details For {self.name_entry.get()} Address: {self.address_entry.get()} {self.city_entry.get()}, {self.state_entry.get()} {self.zip_entry.get()} Total Cost: {self.calc_total()}')

pizza_order = PizzaOrderGUI()
