import tkinter as tk

class MyGUI:
    def __init__(self):
    #creates the main winow widget and assign it to variable 'main_window'
        self.main_window = tk.Tk()
    #create labels, require 2 parameters, where it should be located and what text it should contain
    #no matter what you do, if you don't use the pack method, it won't show up. 
    #sets location, defaults to top

        #set size of window, confirgure main window by pixels (width x height)
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.label1 = tk.Label(self.main_window,text='Hello World!')

        self.label2 = tk.Label(self.main_window,text='This is my GUI program')

        self.label1.pack(side='left')
        self.label2.pack(side='right')

        tk.mainloop()

#create an instance of our class to run it
my_gui = MyGUI()

#won't run until the window, or GUI, is closed
print("moving on ...")
