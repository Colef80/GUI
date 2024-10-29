import tkinter as tk
import tkinter.messagebox
import tkinter.ttk

class PizzaOrderGUI:
    def __init__(self):
        #Main Window
        self.main_window = tk.Tk()
        self.main_window.geometry('700x600')
        self.main_window.title('Pizza Order Form')


        #Format Frames
        self.top_frame = tk.Frame(self.main_window)
        self.name_frame = tk.Frame(self.main_window)
        self.address_frame = tk.Frame(self.main_window)
        self.option_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #Welcome Message
        self.welcome = tk.Label(self.top_frame, text='Welcome to Baylor Pizza Bar!\n')
        self.welcome.pack()

        #Customer Details
        self.customerheader = tk.Label(self.name_frame, text='Customer Details')
        self.customerheader.pack()
        self.nprompt = tk.Label(self.name_frame, text='Enter Your Name: ')
        self.name_entry = tk.Entry(self.name_frame, width=10)
        self.nprompt.pack(side='left')
        self.name_entry.pack(side='left')

        self.aprompt = tk.Label(self.address_frame, text='Street Address: ')
        self.address_entry = tk.Entry(self.address_frame, width=10)
        self.aprompt.pack(side='left')
        self.address_entry.pack(side='left')

        self.cprompt = tk.Label(self.address_frame, text='City: ')
        self.city_entry = tk.Entry(self.address_frame, width=10)
        self.cprompt.pack(side='left')
        self.city_entry.pack(side='left')

        self.sprompt = tk.Label(self.address_frame, text='State: ')
        self.state_entry = tk.Entry(self.address_frame, width=10)
        self.sprompt.pack(side='left')
        self.state_entry.pack(side='left')

        self.zprompt = tk.Label(self.address_frame, text='ZIP Code: ')
        self.zip_entry = tk.Entry(self.address_frame, width=10)
        self.zprompt.pack(side='left')
        self.zip_entry.pack(side='left')


        #Pizza Options
        self.pheader = tk.Label(self.option_frame, text='\nPizza Order')
        self.pheader.pack()

        #Size
        self.sizeheader = tk.Label(self.option_frame, text='Pizza Size')
        self.sizeheader.pack()
        self.size_var = tk.IntVar()

        self.rbs = tk.Radiobutton(self.option_frame,
                                    text='Small ($7.99)',
                                    variable=self.size_var,
                                    value=7.99)
                                    
        
        self.rbm = tk.Radiobutton(self.option_frame,
                                    text='Medium ($10.99)',
                                    variable=self.size_var,
                                    value=10.99)
                                    
                
        self.rbl = tk.Radiobutton(self.option_frame,
                                    text='Large ($13.99)',
                                    variable=self.size_var,
                                    value=13.99)
                                    
        self.rbs.pack()
        self.rbm.pack()
        self.rbl.pack()
        
        #Toppings
        self.toppingheader = tk.Label(self.option_frame, text='\nSelect Toppings')
        self.toppingheader.pack()
        self.cb1 = tk.IntVar()
        self.cb2 = tk.IntVar()
        self.cb3 = tk.IntVar()


        self.cbox1 = tk.Checkbutton(self.option_frame,
                                    text='Pepperoni ($0.75)',
                                    variable=self.cb1)
        
        self.cbox2 = tk.Checkbutton(self.option_frame,
                                    text='Olives ($0.75)',
                                    variable=self.cb2)
        
        self.cbox3 = tk.Checkbutton(self.option_frame,
                                    text='Extra Cheese ($0.75)',
                                    variable=self.cb3)
        
        self.cbox1.pack()
        self.cbox2.pack()
        self.cbox3.pack()


        #Sauce Menu
        # self.sauceheader = tk.Label(self.option_frame, text='\nSelect Your Sauce')
        # self.sauceheader.pack()

        # options = [
        #     'Tomato ($0.50)',
        #     'Pesto ($1.00)',
        #     'Alfredo ($1.00)']
        
        # self.clicked = StringVar()

        # self.clicked.set('Tomato ($0.50)')

        # self.drop = OptionMenu(self.option_frame, clicked, *options)
        # drop.pack()


        #Delivery/Pickup
        self.methodheader = tk.Label(self.option_frame, text='\nHow Do You Want Your Pizza Today?')
        self.methodheader.pack()
        self.method_var = tk.IntVar()

        self.rbd = tk.Radiobutton(self.option_frame,
                                    text='Delivery ($2.25)',
                                    variable=self.method_var,
                                    value=2.25)
        
        self.rbp = tk.Radiobutton(self.option_frame,
                                    text='Pickup ($0.00)',
                                    variable=self.method_var,
                                    value=1)
        
        self.rbd.pack(side='left')
        self.rbp.pack(side='right')


        #Submit
        self.submit_button = tk.Button(self.bottom_frame, text='Submit Order', command=self.confirm_message)

    

        #Pack
        self.top_frame.pack()
        self.name_frame.pack()
        self.address_frame.pack()
        self.option_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.submit_button.pack()



        tk.mainloop()


    #Calc_Total
    # def calc_total(self):
    #     size = self.size_var.get()
    #     delivery = self.method_var.get()
    #     total = size + delivery
    #     return float(total)

    #Confirmation Message
    def confirm_message(self):
        tk.messagebox.showinfo('Response', f'Order Details For {self.name_entry.get()} \nAddress: {self.address_entry.get()}\n {self.city_entry.get()}, {self.state_entry.get()} {self.zip_entry.get()} \nTotal Cost: {self.calc_total()}')

pizza_order = PizzaOrderGUI()
