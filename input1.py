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
        self.main_window.title('Input Demo')

        #tell where it will be placed
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #prompt
        self.prompt = tk.Label(self.top_frame, text='Enter a distance in Kilometers: ')

        self.kilo_entry = tk.Entry(self.top_frame, width=10)

        self.prompt.pack()
        self.kilo_entry.pack()


        self.calc_button = tk.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')


        tk.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(kilo * 0.6214,2)
        tk.messagebox.showinfo('Result', str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles')

#create an instance of our class to run it
my_gui = KiloConverterGUI()

#won't run until the window, or GUI, is closed
print("moving on ...")
