import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
    #creates the main winow widget and assign it to variable 'main_window'
        self.main_window = tk.Tk()
    #create labels, require 2 parameters, where it should be located and what text it should contain
    #no matter what you do, if you don't use the pack method, it won't show up. 
    #sets location, defaults to top

        #set size of window, confirgure main window by pixels (width x height)
        self.main_window.geometry('500x200')
        self.main_window.title('Frame Demo')

        #tell where it will be placed
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)

        #labels for top frame
        self.label1 = tk.Label(self.top_frame, text='John')
        self.label2 = tk.Label(self.top_frame, text='James')
        self.label3 = tk.Label(self.top_frame, text='Jack')


        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')

        #labels for bottom frame
        self.label4 = tk.Label(self.bottom_frame, text='Jill')
        self.label5 = tk.Label(self.bottom_frame, text='Janie')
        self.label6 = tk.Label(self.bottom_frame, text='Jennifer')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.my_button = tk.Button(self.button_frame, text='Click Me!', command=self.do_something)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()
        self.my_button.pack(side='left')
        self.quit_button.pack(side='left')


        tk.mainloop()

    def do_something(self):
        tk.messagebox.showinfo('Response', 'Thanks for clicking the button!')

#create an instance of our class to run it
my_gui = MyGUI()

#won't run until the window, or GUI, is closed
print("moving on ...")
