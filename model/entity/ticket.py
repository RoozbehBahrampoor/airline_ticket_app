from tkinter import StringVar, Entry, Checkbutton
from tkinter import ttk

from controller.person_controller import PersonController
from view import *

class ticketView:
    def save_click(self):
        ticket_controller = ticketController()
        status, message = ticket_controller.save(
            self.id.get(),
            self.ticket_code.get(),
            self.origin.get(),
            self.destination.get(),
            self.airline.get(),
            self.start_date_time.get(),
            self.end_date_time.get(),
            self.price.get(),
            self.seat_no.get(),
            self.sold.get()

        )
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)


    def __init__(self):
        win = Tk()
        win.geometry("300x300")

        self.id = IntVar()
        self.ticket_code = StringVar()
        self.origin = StringVar()
        self.destination = IntVar()
        self.airline = StringVar()
        self.start_date_date = StringVar()
        self.end_date_date = StringVar()
        self.price = StringVar()
        self.seat_no = StringVar()
        self.sold = IntVar()

        Entry(win, textvariable=self.id).pack()
        Entry(win, textvariable=self.ticket_code).pack()
        Entry(win, textvariable=self.origin).pack()
        Entry(win, textvariable=self.destination).pack()
        Entry(win, textvariable=self.airline).pack()
        Entry(win, textvariable=self.start_date_date).pack()
        Entry(win, textvariable=self.end_date_date).pack()
        Entry(win, textvariable=self.price).pack()
        Entry(win, textvariable=self.seat_no).pack()
        Entry(win, Checkbutton=self.sold).pack()


        Button(win, text="Save", command=self.save_click).pack()

        win.mainloop()