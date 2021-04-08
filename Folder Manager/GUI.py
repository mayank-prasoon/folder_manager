from tkinter import *
from tkinter.ttk import *

OptionList = [
    "",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

root = Tk()
root.geometry('600x700')

options = Frame(root)
options.pack(side='top', pady=50)

menu = Frame(root)
menu.pack(side='top')

clicked = StringVar(options)
projects = OptionMenu(options, clicked, *OptionList)
projects.pack(side='left', padx=10)

new = Button(options, text='New Project')
new.pack(side='right')

run = Button(options, text='Run Project')
run.pack(side='right', padx=10)


setting = Button(menu, text='Setting')
setting.pack(side='top')

exit_software = Button(menu, text='Exit', command=root.destroy)
exit_software.pack(side='top')

root.mainloop()
