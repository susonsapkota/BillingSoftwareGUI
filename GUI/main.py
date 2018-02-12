from tkinter import *
import tkinter.messagebox


def dummyFunction():
    print("This does nothing.")


def confirmExit():
    global root
    if tkinter.messagebox.askyesno("Exit", "Do you want to exit this application?\n"
                                           "Unsaved files may get deleted."):
        root.destroy()


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
insertButton = Button(toolBar, text="Insert....", command=dummyFunction)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolBar, text="Print....", command=dummyFunction)
printButton.pack(side=RIGHT, padx=2, pady=2)

# shows on frame
toolBar.pack(side=TOP, fill=X)

# status bar


# where to add->root
statusBar = Label(root, text="Static text that is going to change",
                  bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

# icon for the window
root.iconbitmap('icon.ico')

# title and size of window
root.title("Billing Software - Sapkota Suson")
root.geometry("500x400")

# this loops the program
root.mainloop()
