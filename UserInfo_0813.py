"""
Created on Tue Aug 10 13:34:16 2021

@author: Gopa Kumar

"""

from tkinter import *
import sys
from tkinter import messagebox


class UserPrompt(object):

    user_name= ""

    def __init__(self):

        self.base= Tk()
        self.base.protocol ("W_DELETE WINDOW", self.Exit)
        self.base.title("User Info")
        self.base.geometry('488x289')
        self.base.bind('<Return>',self.wholeFunc)
        self.base.resizable(0,0)
        self.usernamelabel= Label(self.base, text="User Name:", font=('arial', 9, 'bold'))
        self.usernamelabel.place(x=80, y=40)
        self.messagebox1 = Entry(self.base, textvariable=self.user_name, bd=1, bg='Light grey',\
                                highlightbackground= 'red', highlightthickness = 1,highlightcolor='red')
        self.messagebox1.place(x=160, y=40, height=22, width=180)
        self.messagebox1.focus()
        self.submitbutton = Button(self.base, text= 'Submit', bd=1, bg='grey', activebackground = 'white',\
                                   font=('arial', 9, 'bold'), foreground= 'black', relief= 'raised',\
                                   highlightbackground='red', highlightthickness = 1,\
                                    command = lambda: self.wholeFunc())
        self.submitbutton.place(x=160, y=80, height=20, width= 60)
        self.base.focus_force()
        self.base.mainloop()

    def getInput(self):
        self.user_input = self.messagebox1.get()
    # print(self.user_input)
    # self.DisplayData()
    # self.messagebox.delete (1.0, END)
        return self.user_input

    def closeWindow(self):
        if self.user_input == '':
            messagebox.showinfo("Info", "Username Cannot be empty!")
        else: self.base.destroy()

    def Exit(self):
        self.base.destroy()
        sys.exit()

    def wholeFunc(self, event=None):
        self.getInput()
        self.closeWindow()

userInput = UserPrompt()