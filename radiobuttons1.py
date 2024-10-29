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
        self.bottom_frame = tk.Frame(self.main_window)

        self.radio_var = tk.IntVar()

        self.radio_var.set(2)
        #if you set before you run the rest of the options, it can set a default value


        self.rb1 = tk.Radiobutton(self.top_frame,
                                    text='Option 1',
                                    variable=self.radio_var,
                                    value=1)
        
        self.rb2 = tk.Radiobutton(self.top_frame,
                                    text='Option 2',
                                    variable=self.radio_var,
                                    value=2)
        
        self.rb3 = tk.Radiobutton(self.top_frame,
                                    text='Option 3',
                                    variable=self.radio_var,
                                    value=3)
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()


        self.ok_button = tk.Button(self.bottom_frame, text='Ok', command=self.show_choice)
        self.reset_button = tk.Button(self.bottom_frame, text='Reset', command=self.reset_choice)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)


        self.ok_button.pack(side='left')
        self.reset_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()


        tk.mainloop()

    def show_choice(self):
        tk.messagebox.showinfo('Selection', 'You have selected option ' + 
                                                str(self.radio_var.get()))
        
    def reset_choice(self):
        self.radio_var.set(1)

#create an instance of our class to run it
my_gui = KiloConverterGUI()

#watch for errors to happen, like that^^

#won't run until the window, or GUI, is closed
print("moving on ...")
