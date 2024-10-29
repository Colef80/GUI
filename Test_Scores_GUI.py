import tkinter as tk
import tkinter.messagebox

class TestScoresGUI:
    def __init__(self):
    #creates the main winow widget and assign it to variable 'main_window'
        self.main_window = tk.Tk()

        #set size of window, confirgure main window by pixels (width x height)
        self.main_window.geometry('600x300')
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
        self.test1 = tk.Label(self.score1_frame, text='Enter the score for test 1:', bg='green', fg='yellow', font=('Comic Sans MS', 20))
        self.test2 = tk.Label(self.score2_frame, text='Enter the score for test 2:', bg='green', fg='yellow', font=('Comic Sans MS', 20))
        self.test3 = tk.Label(self.score3_frame, text='Enter the score for test 3:', bg='green', fg='yellow', font=('Comic Sans MS', 20))

        #Entry for top frame
        self.score1_entry = tk.Entry(self.score1_frame, width=5, bg='green', fg='yellow', font=('Comic Sans MS', 20))
        self.score2_entry = tk.Entry(self.score2_frame, width=5, bg='green', fg='yellow', font=('Comic Sans MS', 20))
        self.score3_entry = tk.Entry(self.score3_frame, width=5, bg='green', fg='yellow', font=('Comic Sans MS', 20))

        self.test1.pack(side='left')
        self.score1_entry.pack(side='left')
        self.test2.pack(side='left')
        self.score2_entry.pack(side='left')
        self.test3.pack(side='left')
        self.score3_entry.pack(side='left')


        #Create the widgets for the mid frame 
        self.average_label = tk.Label(self.mid_frame, text='Average:', bg='green', fg='yellow', font=('Comic Sans MS', 20))

        self.average_var = tk.StringVar()

        self.average = tk.Label(self.mid_frame, textvariable=self.average_var, bg='green', fg='yellow', font=('Comic Sans MS', 20))

        self.average_label.pack(side='left')
        self.average.pack(side='left')


        self.calc_button = tk.Button(self.bottom_frame, text='Average', bg='green', fg='yellow', font=('Comic Sans MS', 20), command=self.calc_average)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', bg='green', fg='yellow', font=('Comic Sans MS', 20), command=self.main_window.destroy)


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
        total = int(self.score1_entry.get()) + int(self.score2_entry.get()) + int(self.score3_entry.get())
        average = round(total / 3,2)
        self.average_var.set(average)

#create an instance of our class to run it
my_gui = TestScoresGUI()

print("moving on ...")
