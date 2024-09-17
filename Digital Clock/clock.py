from tkinter import Tk
from tkinter import Label
import time
import sys


root = Tk()
root.title('My Clock')

def present_time():
    display_time = time.strftime('%I : %M : %S %p')
    digital_clock.config(text=display_time)
    digital_clock.after(200, present_time)

digital_clock = Label(root, font=('Arial', 150), bg='Red', fg='Black')
digital_clock.pack()

present_time()
root.mainloop()