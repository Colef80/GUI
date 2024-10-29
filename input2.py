import tkinter as tk
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
    #creates the main winow widget and assign it to variable 'main_window'
        self.main_window = tk.Tk()
    #create labels, require 2 parameters, where it should be located and what text it should contain
    #no matter what you do, if you don't use the pack method, it won't show up. 
    #sets location, defaults to top

        #set size of window, confirgure main window by pixels (width x height)
        self.main_window.geometry('300x100')
        self.main_window.title('Input 2 Demo')

        #tell where it will be placed
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)


        #Labels for top frame
        self.prompt = tk.Label(self.top_frame, text='Enter a distance in Kilometers: ')
        self.kilo_entry = tk.Entry(self.top_frame, width=10)

        self.prompt.pack(side='left')
        self.kilo_entry.pack(side='left')


        #Create the widgets for the mid frame 
        self.desc_label = tk.Label(self.mid_frame, text='Converted to miles: ')

        self.miles_var = tk.StringVar()

        self.miles_label = tk.Label(self.mid_frame, textvariable=self.miles_var)

        self.desc_label.pack()
        self.miles_label.pack()


        self.calc_button = tk.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)


        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        tk.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(kilo * 0.6214,2)
        self.miles_var.set(miles)

#create an instance of our class to run it
my_gui = KiloConverterGUI()

#watch for errors to happen, like that^^

#won't run until the window, or GUI, is closed
print("moving on ...")
