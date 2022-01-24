from tkinter import *
from datetime import *
from tkinter import messagebox
import re
import UserInfo_0813 as userinfo
import Chat1

#Assigning tkinter to an object called base
base = Tk()
#creating a class for chatbot GUI

class ChatBotGUI(object):

    counter = 1.0
    UserText="{}[{}]: "

    def __init__(self, base):
        #Creating an UI with below dimensions
        base.title("Khaleesi")
        base.geometry('400x500')
        base.resizable (0,0)
        #to place the application at center base.eval('tk::PlaceWindow. center')
        base.bind('<Return>',self.FetchData)
        self.maininput = getuserinfo.user_input
        self.maininput = getuserinfo.user_input
        self.base_menu = Menu(base, tearoff=0)
        self.sub_menu = Menu(base, tearoff=0)
        # added implementation for clearing session
        self.sub_menu.add_command(label='New Session', command=lambda: self.clearSession())
        self.sub_menu.add_command(label='Quit', command=lambda: self.quitSession())
        self.sub_menu_help = Menu(base, tearoff=0)
        # self.sub_menu.add_command (label='Attach Document') #added implementation for quit button
        # added sub menu for help option
        self.sub_menu_help.add_command(label='Contacts', command=lambda: self.contactDetails())
        self.base_menu.add_cascade(label='File', menu=self.sub_menu)
        self.base_menu.add_cascade(label='Help', menu=self.sub_menu_help)
        base.config(menu=self.base_menu)
        self.chatpane = Text(base, bd=1, bg='light green', state='disabled', width=47,height=22, \
                        wrap = 'word',spacing3= '1', highlightbackground = 'black', \
                        highlightthickness = 1)
        self.chatpane.place(x=5, y=5, height=350, width=370)
        self.messagebox = Text(base, bd = 1, bg='bisque', wrap='word', highlightbackground='black', \
                          font = ('Calibri', 11), highlightthickness = 1)

        self.messagebox.place(x=5, y=370, height=100, width=290)
        self.messagebox.focus()
        self.sendbutton = Button(base, text='Send', bd=1, bg='IndianRed1', activebackground='white', \
                          font = ('arial', 12, 'bold'), foreground = 'black', relief = 'raised', \
                          highlightbackground = 'black', highlightthickness = 1,\
                          command = lambda: self.FetchData())
        self.sendbutton.place(x = 320, y=390, height=50, width=75)
        self.windowscroll = Scrollbar(base, command=self.chatpane.yview())
        self.windowscroll.place(x = 388, y=5, height=350, width=20)
        self.messagescroll = Scrollbar(base, command = self.messagebox.yview())
        self.messagescroll.place(x=295, y=370, height=100, width=20)
        self.messagebox.config(yscrollcommand=self.messagescroll.set)
        self.messagescroll.config(command=self.messagebox.yview)
        self.chatpane.config(yscrollcommand=self.windowscroll.set)
        self.windowscroll.config(command=self.chatpane.yview)
        self.chatpane.config(state="normal")
        self.chatpane.tag_configure('FromTo3', foreground="Blue", font=(
            'arial', 9, "bold"),justify="center")
        self.chatpane.insert(1.0, "WikiBot: Welcome!! Happy to assist You!!\n\n",'FromTo3')
        self.chatpane.config(state="disabled")

    def CountGenerator(self):
        self.counter += 1
        yield self.counter

    def DisplayData(self):
        self.chatpane.tag_configure("right_Justify", justify='right', font=('Calibri', 11))
        self.date = datetime.now().strftime("%I:%M")
        self.chatpane.config(state="normal")
        result = bool(re.search('^[\s+?]',self.i_p))

        '''added timestamp and Logic not to send empty value'''

        if result == True:
            self.chatpane.config(state='disabled')

        else:

            self.chatpane.tag_configure("FromTo", foreground="red", font=('arial', 9, 'bold'), justify="right")
            self.chatpane.insert(END, self.UserText.format(self.maininput, self.date), "From To")
            self.chatpane.tag_add("F romTo", 1.0, END)
            self.chatpane.pack(fill=BOTH)
            self.chatpane.config(state="disabled")
            self.chatpane.config(state="normal")
            self.chatpane.insert(END, self.i_p + "\n", "right_Justify")
        # self.chatpane.insert (END, "", "left_Justify")
            self.chatpane.see("end")
            self.chatpane.config(state="disabled")
            self.ResponseProcessing(Chat1.input_process(self.i_p))

    def ResponseProcessing(self, response="xxxxxxxxxxx"):
    # index = self.Count Generator()
        self.date = datetime.now().strftime("%I: XM")
        self.chatpane.tag_configure("Left_Justify", justify='Left', font=('Calibri', 11))
        self.chatpane.config(state="normal")
        self.chatpane.tag_configure("FromTo1", foreground="red", font=('arial', 9, 'bold'), justify='Left')
        self.chatpane.insert(END, self.UserText.format("WikiBot", self.date), "FromTo1")
        self.chatpane.config(state="disabled")
        self.chatpane.config(state="normal")
        self.chatpane.insert(END, response + "\n\n", "Left_Justify")
    # self.chatpane.tag_add("left_Justify", END)
    # self.chatpane.pack()
        self.chatpane.see("end")
        self.chatpane.config(spacing3='1', state="disabled")

    def FetchData(self, event=None):
        self.i_p = self.messagebox.get(1.0, END)
        self.DisplayData()
        self.messagebox.delete(1.0, END)
        return self.i_p

    '''Added method to clear the screen and restart based on user's response'''

    def clearSession(self):

        user_input = messagebox.askquestion("MessageBox", "Are you sure?")
        if user_input == 'yes':
            self.chatpane.config(state="normal.")
            self.chatpane.delete(1.0, END)
            self.chatpane.tag_configure("From Toz", foreground="Blue", font=('arial', 9, "bold"), justify="center")
            self.chatpane.insert(1.0, "WikiBot: Welcome!! Happy to assist You!!\n\n",'FromTo2')
            self.chatpane.config(state="disabled")
        else:
            pass

    def quitSession(self):
        user_input = messagebox.askquestion("MessageBox", "Do you really want to Quit?")
        if user_input == 'yes':
            base.destroy()
        else:
            pass

    '''Method to display the contact details '''

    def contactDetails(self):
        messagebox.showinfo('Contacts', "Dharanisankarmuthusamy@fiserv.com\n\nbrunogodwinvisvas.anbu@fiserv.com\n\n" \
                                    "ashokkumar.parthiban@fiserv.com\n\ngopakumar.ks@fiserv.com")

    def inputList(self):

        with open('inputList.txt', 'a') as f:
            f.write('\n'+ self.maininput +' '+ datetime.now().strftime ("%Y_% m_%d-%I:%M:%S"))
            f.close()

getuserinfo = userinfo.userInput

chatBot = ChatBotGUI(base)
base.focus_force()
base.mainloop()
chatBot.inputList()