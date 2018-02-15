import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import datetime

date_time = datetime.datetime.now()
date_now = date_time.strftime("%Y - %m - %d")
time_now = date_time.strftime("%H : %M : %S")


def dummyFunction():
    print("This does nothing.")
    print(date_now)
    print(time_now)


def confirmExit():
    global root
    if tkinter.messagebox.askyesno("Exit", "Do you want to exit this application?\n"
                                           "Unsaved files may get deleted."):
        root.destroy()


def askName():
    pass


root = Tk()

menu = Menu(root)
root.config(menu=menu)

# menus and submenus here
subMenu = Menu(root)
menu.add_cascade(label="File", menu=subMenu)  # this adds tabs on the menu
subMenu.add_command(label="New User", command=dummyFunction)
subMenu.add_command(label="Open Recent", command=dummyFunction)
subMenu.add_separator()  # separator
subMenu.add_command(label="Dummy1", command=dummyFunction)
subMenu.add_command(label="Dummy2", command=dummyFunction)
subMenu.add_separator()
subMenu.add_command(label="NDummy3", command=dummyFunction)
subMenu.add_command(label="Dummy4", command=dummyFunction)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=confirmExit)
# next menu
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)  # this adds tabs on menu
editMenu.add_command(label="New User", command=dummyFunction)
editMenu.add_command(label="Open Recent", command=dummyFunction)
editMenu.add_separator()
editMenu.add_command(label="Dummy1", command=dummyFunction)
editMenu.add_command(label="Dummy2", command=dummyFunction)
editMenu.add_separator()

# tool bar

toolBar = Frame(root, bg="grey")
# to show on screen
insertButton = ttk.Button(toolBar, text="Insert....", command=dummyFunction)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = ttk.Button(toolBar, text="Print....", command=dummyFunction)
printButton.pack(side=RIGHT, padx=2, pady=2)

# shows on frame
toolBar.pack(side=TOP, fill=X)

# Name and address  of company
companyName = Label(root, text="Generic Super Market", font="-weight bold")
companyName.pack(side=TOP)
companyAddress = Label(root, text="Generic Chowk, Kathmandu")
companyAddress.pack(side=TOP)

# Date and time
dateTimeFrame = Frame(root)
NowDate = Label(dateTimeFrame, text="Date: " + date_now)
NowDate.pack(side=LEFT, pady=2)
NowTime = Label(dateTimeFrame, text="Time: " + time_now)
NowTime.pack(side=RIGHT, pady=2)
dateTimeFrame.pack(side=TOP, fill=X)

# status bar
# where to add->root
statusBar = Label(root, text="Static text that is going to change",
                  bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

# icon for the window
root.iconbitmap('icon.ico')

# title and size of window
root.title("Billing Software - Sapkota Suson")
root.geometry("750x450")

# this loops the program
root.mainloop()
