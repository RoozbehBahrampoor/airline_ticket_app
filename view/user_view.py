from controller.user_controller import UserController
from view import *

class UserView:
    def save_click(self):
        user_controller = UserController()
        status, message = user_controller.save(
            self.id.get(),
            self.name.get(),
            self.family.get(),
            self.birth_date.get(),
            self.user_name.get(),
            self.password.get(),
            self.is_locked.get(),
            self.role.get(),
        )
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save Error", message)

    def __init__(self):
        win = Tk()
        win.geometry("300x300")

        self.id = IntVar()
        self.name = StringVar()
        self.family = StringVar()
        self.birth_day = IntVar()
        self.user_name = StringVar()
        self.password = StringVar()
        self.role = StringVar()

        Entry(win, textvariable=self.id).pack()
        Entry(win, textvariable=self.name).pack()
        Entry(win, textvariable=self.family).pack()
        Entry(win, textvariable=self.birth_day).pack()
        Entry(win, textvariable=self.user_name).pack()
        Entry(win, textvariable=self.password).pack()
        Entry(win, textvariable=self.role).pack()

        Button(win, text="Save", command=self.save_click).pack()

        win.mainloop()

