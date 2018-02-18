import datetime
import tkinter.messagebox
from functools import partial
from tkinter import *
from tkinter import ttk

from BillingSoftwareGUI.GUI import userAdd
from BillingSoftwareGUI.GUI.Discount import *
from BillingSoftwareGUI.GUI.dataReadWrite import *
from BillingSoftwareGUI.GUI.Num2Words import *

date_time = datetime.datetime.now()
date_now = date_time.strftime("%Y - %m - %d")
time_now = date_time.strftime("%H : %M : %S")

cart = []
counter = 1
totalPrice = 0


class BillingSoftware:
    def __init__(self, master):

        self.totalPrice = 0
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
        master.option_add('*tearOff', False)
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
        self.ProductLabel.pack(anchor=W)

        self.productTreeView = ttk.Treeview(self.productFrame, height=30, selectmode="extended")
        self.productTreeView.pack(side=LEFT, anchor=NW)

        self.productTreeView["columns"] = ("1", "2", "3")

        self.productTreeView.column("#0", width=50, anchor=W)
        self.productTreeView.column("1", width=250, anchor=W)
        self.productTreeView.column("2", width=200, anchor=W)
        self.productTreeView.column("3", width=200, anchor=W)

        self.productTreeView.heading("#0", text="S.N")
        self.productTreeView.heading("1", text="Name")
        self.productTreeView.heading("2", text="Price")
        self.productTreeView.heading("3", text="Quantity")
        clean_data()
        for i in range(len(products)):
            self.productTreeView.insert("", "end", str(i), text=i)

            self.productTreeView.set(str(i), "1", products[i][0])
            self.productTreeView.set(str(i), "2", products[i][1])
            self.productTreeView.set(str(i), "3", products[i][2])

        self.productTreeView.bind("<Double-1>", self.addToCart)
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
        self.UserTreeView = ttk.Treeview(self.userFrame, height=30, selectmode="none")
        self.UserTreeView.pack(side=LEFT, anchor=NW)

        self.UserTreeView["columns"] = ("1", "2")

        self.UserTreeView.column("#0", width=50, anchor=W)
        self.UserTreeView.column("1", width=300, anchor=W)
        self.UserTreeView.column("2", width=250, anchor=W)

        self.UserTreeView.heading("#0", text="S.N")
        self.UserTreeView.heading("1", text="Name")
        self.UserTreeView.heading("2", text="Price")

        # Labels inside of frame for top frame

        self.totalFrame = Frame(master, height=200, bg="green")
        self.totalFrame.config(relief=SUNKEN, bd=2)
        self.totalFrame.pack(side=TOP, padx=20, pady=20, fill=BOTH)
        self.totalFrame.pack_propagate(False)

        self.priceFrame = Frame(self.totalFrame, height=140, bg="red")
        self.priceFrame.pack(side=TOP, fill=BOTH)
        self.priceFrame.pack_propagate(False)

        self.priceLabelTotal = Label(self.priceFrame, text="Total : Rs.",
                                     font=("Helvetica", 17))
        self.priceLabelTotal.pack()

        self.priceLabelNum = Label(self.priceFrame, text=0,
                                   font=("Helvetica", 15))
        self.priceLabelNum.pack()
        self.priceLabelWords = Label(self.priceFrame, text="",
                                     font=("Helvetica", 15))
        self.priceLabelWords.pack()

        self.priceLabelDis = Label(self.priceFrame, text="",
                                   font=("Helvetica", 15))
        self.priceLabelDis.pack()

        self.bottomFrame = Frame(self.totalFrame, bg="grey")
        self.bottomFrame.pack(side=BOTTOM, fill=X)

        self.applyDisocunt = ttk.Button(self.bottomFrame, text="Apply discount",
                                        command=self.askDiscount, width=15)

        self.applyDisocunt.pack(side=LEFT, anchor=W)

        self.printInvoice = ttk.Button(self.bottomFrame, text="Checkout / PRINT Invoice",
                                       command=self.doNothing, width=30)

        self.printInvoice.pack(side=RIGHT, anchor=E)

    def doNothing(self):
        print("did nothing")

    def updateTreeView(self):
        for i in range(len(products)):
            self.productTreeView.insert("", "end", str(i), text=i)

            self.productTreeView.set(str(i), "1", products[i][0])
            self.productTreeView.set(str(i), "2", products[i][1])
            self.productTreeView.set(str(i), "3", products[i][2])

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

        # self.priceLabelDis['text'] = self.returnFormatedDiscount

    def addToCart(self, event):
        global counter
        item = int(self.productTreeView.identify('item', event.x, event.y))
        if int(products[item][2]) - 1 >= 0:
            cart.append(products[item])
            self.UserTreeView.insert("", "end", str(counter), text=counter)
            self.UserTreeView.set(str(counter), "1", products[item][0])
            self.UserTreeView.set(str(counter), "2", products[item][1])
            self.calculateTotal(int(products[item][1]))

            self.priceLabelNum.config(text=totalPrice)
            # TODO implement discount

            self.priceLabelWords.config(text=num_to_word(totalPrice))
            # print(totalPrice)
            # print("discountamt",self.returnFormatedDiscount())
            counter += 1

            # decreasing the inventory after user adds to cart.

            products[int(item)][2] = int(products[item][2]) - 1



        else:
            print("not enough item")

            # TODO implement pop-up

    def calculateTotal(self, num, ):
        global totalPrice
        totalPrice += num

    def returnFormatedDiscount(self):
        amt = DiscountClass.returnDiscountAmt(totalPrice)

        return amt


def main():
    root = Tk()
    app = BillingSoftware(root)
    root.mainloop()


if __name__ == "__main__": main()
