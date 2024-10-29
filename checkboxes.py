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

        self.cb1 = tk.IntVar()
        self.cb2 = tk.IntVar()
        self.cb3 = tk.IntVar()


        self.cbox1 = tk.Checkbutton(self.top_frame,
                                    text='Option 1',
                                    variable=self.cb1)
        
        self.cbox2 = tk.Checkbutton(self.top_frame,
                                    text='Option 2',
                                    variable=self.cb2)
        
        self.cbox3 = tk.Checkbutton(self.top_frame,
                                    text='Option 3',
                                    variable=self.cb3)
        
        self.cbox1.pack()
        self.cbox2.pack()
        self.cbox3.pack()


        self.ok_button = tk.Button(self.bottom_frame, text='Ok', command=self.show_choice)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)


        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()


        tk.mainloop()

    def show_choice(self):
        msg = 'You have selected:\n'

#two states of a checkbox are 0 or 1, 0 is unchecked 1 is checked
        if self.cb1.get() ==1:
            msg += '1\n'
            
        if self.cb2.get() ==1:
            msg += '2\n'

        if self.cb3.get() ==1:
            msg += '3\n'

        tk.messagebox.showinfo('Selection', msg)
        

#create an instance of our class to run it
my_gui = KiloConverterGUI()

#watch for errors to happen, like that^^

#won't run until the window, or GUI, is closed
print("moving on ...")
