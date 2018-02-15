import datetime
from  tkinter import *
from tkinter import ttk

date_time = datetime.datetime.now()
date_now = date_time.strftime("%Y - %m - %d")
time_now = date_time.strftime("%H : %M : %S")

users = [["id", "name", "gender", "dateCreated"]]  # formatting of database.


class UserClass:
    def addUserFunction(self):
        if len(self.userName.get()) >= 3 and len(self.userGender.get()) >= 4:
            print(self.userName.get())
            users.append([str(len(users)), self.userName.get(), self.userGender.get(), str(date_now)])
            self.userName.delete(0, END)
            self.writeToTxt()
        else:
            self.infoText.pack(side=BOTTOM, fill=X, padx=3, pady=3)

    def writeToTxt(self):
        f = open("usersDatabase.txt", "w")
        for i in range(len(users)):
            for j in range(len(users[i])):
                if j < 3:
                    f.write(users[i][j] + ",")  # for determining where to put comma
                else:
                    f.write(users[i][j])
            f.write("\n")

    def __init__(self, master):
        master.geometry("400x200")
        master.resizable(False, False)
        master.title("Add new user")
        master.iconbitmap('add.ico')

        self.companyFrame = ttk.Frame(master)
        self.companyFrame.pack()

        self.companyName = ttk.Label(self.companyFrame, text="Generic Super Market",
                                     font="-weight bold")
        self.companyAddress = ttk.Label(self.companyFrame, text="Generic Chowk, Kathmandu")
        self.companyName.pack(side=TOP, padx=2, pady=2)
        self.companyAddress.pack(side=TOP, padx=2, pady=2)

        self.addUser = ttk.Label(master, text="Full Name: ")
        self.addUser.pack()

        self.userName = ttk.Entry(master, width=45)
        self.userName.pack()

        self.userGender = StringVar()
        self.genderFrame = ttk.Frame(master)
        self.genderFrame.pack(padx=2, pady=2)
        self.maleGender = ttk.Radiobutton(self.genderFrame, text="Male",
                                          variable=self.userGender, value="Male")
        self.femaleGender = ttk.Radiobutton(self.genderFrame, text="Female",
                                            variable=self.userGender, value="Female")
        self.maleGender.pack(side=LEFT)
        self.femaleGender.pack(side=LEFT)

        self.submitButton = ttk.Button(master, text="Add New User",
                                       command=self.addUserFunction)
        self.submitButton.pack(padx=5, pady=10, ipadx=5, ipady=4)

        self.infoText = ttk.Label(master, text="Please Input your full name and select your gender.")

# root = Tk()
# app = UserClass(root)
# root.mainloop()
