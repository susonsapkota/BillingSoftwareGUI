from functools import partial
from  tkinter import *
from tkinter import ttk


discPercent = 0
updatedPrice = 0
discAmt = 0
class DiscountClass:
    def __init__(self, master):
        master.geometry("305x165")
        master.resizable(False, False)
        master.title("Apply discount amount")
        master.iconbitmap('add.ico')

        self.companyFrame = ttk.Frame(master)
        self.companyFrame.pack()

        self.companyName = ttk.Label(self.companyFrame, text="Generic Super Market",
                                     font="-weight bold")
        self.companyAddress = ttk.Label(self.companyFrame, text="Generic Chowk, Kathmandu")
        self.companyName.pack(side=TOP, padx=2, pady=2)
        self.companyAddress.pack(side=TOP, padx=2, pady=2)

        self.addDesc = ttk.Label(master,
                                 text="Enter the percent of Discount to apply: [ in % ]")
        self.addDesc.pack()

        self.descAmt = ttk.Entry(master, width=15)
        self.descAmt.pack()

        passingArgs = partial(self.updateDiscount, master)
        self.applyButton = ttk.Button(master, text="Apply",
                                      command=passingArgs)
        self.applyButton.pack(padx=5, pady=10, ipadx=5, ipady=4)

        self.infoText = ttk.Label(master, text="Please Input the valid discount percentage.")

    def doNothing(self):
        print("clickedfgsd")

    def returnDiscountAmt(self, totalprice):
        amt = (int(discPercent) / 100) - int(totalprice)
        return amt



    def updateDiscount(self, master):
        global discAmt
        global discPercent
        global updatedPrice
        try:
            if int(self.descAmt.get()) >= 0:
                discPercent = int(self.descAmt.get())
                master.destroy()

        except ValueError:
            self.infoText.pack(side=BOTTOM, fill=X, padx=3, pady=3)
