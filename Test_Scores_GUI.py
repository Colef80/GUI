import tkinter as tk
import tkinter.messagebox

class TestScoresGUI:
    def __init__(self):
    #creates the main winow widget and assign it to variable 'main_window'
        self.main_window = tk.Tk()

        #set size of window, confirgure main window by pixels (width x height)
        self.main_window.geometry('400x200')
        self.main_window.title('Student Test Average')
        self.main_window.configure(bg='green')

        #tell where it will be placed
        self.top_frame = tk.Frame(self.main_window, bg='green')
        self.score1_frame = tk.Frame(self.top_frame, bg='green')
        self.score2_frame = tk.Frame(self.top_frame, bg='green')
        self.score3_frame = tk.Frame(self.top_frame, bg='green')
        self.mid_frame = tk.Frame(self.main_window, bg='green')
        self.bottom_frame = tk.Frame(self.main_window, bg='green')


        #Labels for top frame
        self.test1 = tk.Label(self.score1_frame, text='Enter the score for test 1: ', bg='green')
        self.test2 = tk.Label(self.score2_frame, text='Enter the score for test 2: ', bg='green')
        self.test3 = tk.Label(self.score3_frame, text='Enter the score for test 3: ', bg='green')

        #Entry for top frame
        self.score1_entry = tk.Entry(self.score1_frame, width=6, bg='green')
        self.score2_entry = tk.Entry(self.score2_frame, width=6, bg='green')
        self.score3_entry = tk.Entry(self.score3_frame, width=6, bg='green')

        self.test1.pack(side='left')
        self.score1_entry.pack(side='left')
        self.test2.pack(side='left')
        self.score2_entry.pack(side='left')
        self.test3.pack(side='left')
        self.score3_entry.pack(side='left')


        #Create the widgets for the mid frame 
        self.average_label = tk.Label(self.mid_frame, text='Average: ', bg='green')

        self.average_var = tk.StringVar()

        self.average = tk.Label(self.mid_frame, textvariable=self.average_var, bg='green')

        self.average_label.pack()
        self.average.pack()


        self.calc_button = tk.Button(self.bottom_frame, text='Average', fg='green', command=self.calc_average)
        self.calc_button.configure(bg='green')
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)


        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack(side='top', anchor='nw')
        self.score1_frame.pack()
        self.score2_frame.pack()
        self.score3_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        tk.mainloop()

    def calc_average(self):
        pass

#create an instance of our class to run it
my_gui = TestScoresGUI()

print("moving on ...")
