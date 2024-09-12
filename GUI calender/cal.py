#importing the libraries
from tkinter import *
import calendar

def Calender_see():
    window = Tk()
    window.config(background='light pink')
    window.title('Complete year calender')
    window.geometry('650x780')
    get_year = int(year_entry.get())
    window_content = calendar.calendar(get_year)
    year_cal = Label(window, text=window_content, font=('Arial', 12, 'bold'))
    year_cal.grid(row=5, column=1)
    window.mainloop()

if __name__  == '__main__':
    root = Tk()
    root.config(background="Yellow")
    root.title('GUI Calender')
    root.geometry('300x190')

    name = Label(root, text='Calender', bg='light pink', font=('arial', 20, 'bold'))
    name.grid(row=1, column=1)

    year = Label(root, text='Enter the Year', bg='light blue', font=('arial', 15, 'bold'))
    year.grid(row=2, column=1)

    year_entry = Entry(root, font=('arial', 15, 'bold'))
    year_entry.grid(row=3, column=1)

    show_button = Button(root, text='Show Calender', fg='red', bg='black', font=('arial', 15, 'bold'), command=Calender_see)
    show_button.grid(row=4, column=1)


    root.mainloop()
