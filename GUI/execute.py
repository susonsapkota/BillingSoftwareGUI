import datetime
import tkinter.messagebox
from functools import partial
from tkinter import *
from tkinter import ttk

from BillingSoftwareGUI.GUI import userAdd
from BillingSoftwareGUI.GUI.Discount import DiscountClass

date_time = datetime.datetime.now()
date_now = date_time.strftime("%Y - %m - %d")
time_now = date_time.strftime("%H : %M : %S")


class BillingSoftware:
    def __init__(self, master):

        # for window scaling and full screen

        # master.overrideredirect(True)
        # master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # master.focus_set()  # <-- move focus to this widget
        # master.bind("<Escape>", lambda e: e.widget.quit())

        # maximized window
        master.state('zoomed')
        master.resizable(False, False)

        # icon for the window
        master.iconbitmap('icon.ico')

        # title and size of window
        master.title("Billing Software - Sapkota Suson")

        # heading of company
        self.companyFrame = ttk.Frame(master)
        self.companyFrame.pack()

        self.companyName = ttk.Label(self.companyFrame, text="Generic Super Market",
                                     font=("Times New Roman", 25, "bold"))
        self.companyAddress = ttk.Label(self.companyFrame, text="Generic Chowk, Kathmandu",
                                        font=("Times New Roman", 15, "bold"))
        self.companyName.pack(side=TOP, padx=2, pady=2)
        self.companyAddress.pack(side=TOP, padx=2, pady=2)

        menu = Menu(master)
        master.config(menu=menu)

        # menus and submenus here
        subMenu = Menu(master)
        menu.add_cascade(label="File", menu=subMenu)  # this adds tabs on the menu
        subMenu.add_command(label="New User", command=self.AddNewUsers)
        subMenu.add_command(label="Open User List", command=self.doNothing)
        subMenu.add_separator()  # separator
        subMenu.add_command(label="Dummy1", command=self.doNothing)
        subMenu.add_command(label="Dummy2", command=self.doNothing)
        subMenu.add_separator()
        subMenu.add_command(label="NDummy3", command=self.doNothing)
        subMenu.add_command(label="Dummy4", command=self.doNothing)
        subMenu.add_separator()
        # passing parameters in a single button method

        paramAsArgument = partial(self.confirmExit, master)
        subMenu.add_command(label="Exit", command=paramAsArgument)
        # next menu
        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)  # this adds tabs on menu
        editMenu.add_command(label="New User", command=self.doNothing)
        editMenu.add_command(label="Open Recent", command=self.doNothing)
        editMenu.add_separator()
        editMenu.add_command(label="Dummy1", command=self.doNothing)
        editMenu.add_command(label="Dummy2", command=self.doNothing)
        editMenu.add_separator()

        # Frame for displaying all the products to the user

        self.productFrame = Frame(master, width=700, bg="blue")
        self.productFrame.config(relief=SUNKEN, bd=2)
        self.productFrame.pack(side=LEFT, fill=Y, padx=20, pady=20)
        self.productFrame.pack_propagate(False)

        # Frame for displaying top bar inside Product Frame which includes s.n,name,price

        self.topFrame = Frame(self.productFrame, bg="yellow")
        self.topFrame.config(relief=SUNKEN, bd=1)
        self.topFrame.pack(side=TOP, fill=X)

        self.ProductLabel = ttk.Label(self.topFrame, text="Inventory - Items available will appear here")
        self.ProductLabel.pack()

        # Labels inside of topFrame

        self.SNBar = Label(self.topFrame, text="S.N",
                           bd=1, width=10, font=(None, 10))
        self.SNBar.pack(side=LEFT, padx=25, pady=5, anchor=NW)

        self.productBar = Label(self.topFrame, text="Product Name",
                                bd=1, width=15, font=(None, 10))
        self.productBar.pack(side=LEFT, padx=30, pady=5, anchor=NW)

        self.PriceBar = Label(self.topFrame, text="Price of Product",
                              bd=1, width=15, font=(None, 10))
        self.PriceBar.pack(side=LEFT, padx=30, pady=5, anchor=NW)

        self.QuantityBar = Label(self.topFrame, text="Quantity Available",
                                 bd=1, width=15, font=(None, 10))
        self.QuantityBar.pack(side=LEFT, padx=30, pady=5, anchor=NW)

        # for adding items that the user selects

        self.userFrame = Frame(master, height=400, bg="grey")
        self.userFrame.config(relief=SUNKEN, bd=2)
        self.userFrame.pack(side=TOP, padx=20, pady=20, fill=X)
        self.userFrame.pack_propagate(False)

        # frames for top bar at user Frames

        self.topFrameUser = Frame(self.userFrame, bg="orange")
        self.topFrameUser.pack(side=TOP, anchor=NW)
        self.userFrame.pack_propagate(False)

        self.UserLabel = ttk.Label(self.topFrameUser, text="Cart - Added items will appear here")
        self.UserLabel.pack()

        # catagories in users frame cart
        self.SNBar1 = Label(self.topFrameUser, text="S.N",
                            bd=1, width=10, font=(None, 10))
        self.SNBar1.pack(side=LEFT, padx=10, pady=5, anchor=NW)

        self.productBar1 = Label(self.topFrameUser, text="Product Name",
                                 bd=1, width=23, font=(None, 10))
        self.productBar1.pack(side=LEFT, padx=10, pady=5, anchor=NW)

        self.PriceBar1 = Label(self.topFrameUser, text="Price",
                               bd=1, width=15, font=(None, 10))
        self.PriceBar1.pack(side=LEFT, padx=10, pady=5, anchor=NW)

        self.totalBar = Label(self.topFrameUser, text="Total",
                              bd=1, width=15, font=(None, 10))
        self.totalBar.pack(side=LEFT, padx=10, pady=5, anchor=NW)

        # Labels inside of frame for top frame

        self.totalFrame = Frame(master, height=200, bg="green")
        self.totalFrame.config(relief=SUNKEN, bd=2)
        self.totalFrame.pack(side=TOP, padx=20, pady=20, fill=BOTH)
        self.totalFrame.pack_propagate(False)

    def doNothing(self):
        print("did nothing")

    def AddNewUsers(self):
        rootSecond = Tk()
        master = userAdd.UserClass(rootSecond)
        rootSecond.mainloop()

    def confirmExit(self, master):
        if tkinter.messagebox.askyesno("Exit", "Do you want to exit this application?\n"
                                               "Unsaved files may get deleted."):
            master.destroy()



    def askDiscount(self):
        rootThird = Tk()
        app = DiscountClass(rootThird)
        rootThird.mainloop()


def main():
    root = Tk()
    app = BillingSoftware(root)
    root.mainloop()


if __name__ == "__main__": main()
