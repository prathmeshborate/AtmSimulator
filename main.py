import tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

try:
    con = pymysql.connect(host='localhost', user='root', password='root')
    mycursor = con.cursor()
except:
    messagebox.showerror('Error', 'Connection is not established.\nPlease try again later...')


def authenticate():
    if cardNumEntry.get() == '' or atmPinEntry.get() == '':
        messagebox.showerror('Érror', 'All fields are required...')
    else:
        query = 'use atmTransaction'
        mycursor.execute(query)
        query = 'select * from accountHolder where cardNo=%s and cardPin=%s'
        mycursor.execute(query, (cardNumEntry.get(), atmPinEntry.get()))
        row = mycursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Invalid Card Number or Pin!')
        else:
            messagebox.showinfo('Authenticated', 'Entered Account Successfully...')
            checkBalanceButton.config(state=tkinter.NORMAL, bg='firebrick1')
            withdrawButton.config(state=tkinter.NORMAL, bg='firebrick1')
            depositButton.config(state=tkinter.NORMAL, bg='firebrick1')


def showBalance():
    query = 'select availBalance from accountHolder where cardNo=%s'
    mycursor.execute(query, (cardNumEntry.get()))
    row = mycursor.fetchone()[0]
    message = f"Your account balance is:  {row} Rs."
    messagebox.showinfo('Account Balance', message)


def withdraw():
    window = Toplevel()
    window.geometry('420x120+200+80')
    card_entry.resizable(0, 0)
    window.title('Withdraw Cash')

    def operation():
        if cardNumEntry.get() == '':
            messagebox.showerror('Érror', 'All fields are required...')
        else:
            query = 'select availBalance from accountHolder where cardNo=%s'
            mycursor.execute(query, (cardNumEntry.get()))
            row = mycursor.fetchone()[0]
            amount = int(amountEntry.get())
            if amount > row:
                messagebox.showwarning('Insufficient Balance', 'Your Account has insufficient balance to withdraw')
            else:
                avail_balance = (row - amount)
                query = 'UPDATE accountHolder SET availBalance=%s WHERE cardNo=%s'
                mycursor.execute(query, (avail_balance, cardNumEntry.get()))
                showBalance()
                con.commit()
                window.destroy()

    bgPic = ImageTk.PhotoImage(file='transaction.jpeg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.place(x=0, y=0)

    withdrawLabel = Label(window, text='Enter Amount to Withdraw', font=('arial', 13, 'bold'),
                    bg='LightPink1', fg='firebrick1')
    withdrawLabel.place(x=13, y=10)

    amountEntry = Entry(window, width=28, font=('Times New Roman', 11)
                        , bd=0, fg='firebrick1')
    amountEntry.place(x=19, y=40)

    withdrawMoneyButton = Button(window, text='Withdraw Money', font=('Open Sans', 13, 'bold'),
                                fg='white', bg='firebrick1', activeforeground='white'
                                , activebackground='firebrick1', cursor='hand2', bd=0, width=21, command=operation)
    withdrawMoneyButton.place(x=13, y=70)

    window.mainloop()


def deposit():
    window = Toplevel()
    window.geometry('420x120+200+80')
    card_entry.resizable(0, 0)
    window.title('Withdraw Cash')

    def operationmin():
        if cardNumEntry.get() == '':
            messagebox.showerror('Érror', 'All fields are required...')
        else:
            try:
                query = 'select availBalance from accountHolder where cardNo=%s'
                mycursor.execute(query, (cardNumEntry.get()))
                row = mycursor.fetchone()[0]
                amount = int(damountEntry.get())
                availd_balance = (row + amount)
                query = 'UPDATE accountHolder SET availBalance=%s WHERE cardNo=%s'
                mycursor.execute(query, (availd_balance, cardNumEntry.get()))
                showBalance()
                con.commit()
                window.destroy()
            except:
                messagebox.showwarning('Limit Exceeded', 'You cant deposit money above Rs. 1000000000')

    bgPic = ImageTk.PhotoImage(file='transaction.jpeg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.place(x=0, y=0)

    depositLabel = Label(window, text='Enter Amount to Deposit', font=('arial', 13, 'bold'),
                          bg='LightPink1', fg='firebrick1')
    depositLabel.place(x=13, y=10)

    damountEntry = Entry(window, width=28, font=('Times New Roman', 11)
                        , bd=0, fg='firebrick1')
    damountEntry.place(x=19, y=40)

    depositMoneyButton = Button(window, text='Deposit Money', font=('Open Sans', 13, 'bold'),
                                 fg='white', bg='firebrick1', activeforeground='white'
                                 , activebackground='firebrick1', cursor='hand2', bd=0, width=21, command=operationmin)
    depositMoneyButton.place(x=13, y=70)

    window.mainloop()


def hide():
    openEye.config(file='closeye.png')
    atmPinEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openEye.config(file='openeye.png')
    atmPinEntry.config(show='')
    eyeButton.config(command=hide)


card_entry = Tk()
card_entry.geometry("740x471+200+200")
card_entry.resizable(0, 0)
card_entry.title("Atm Simulator")
bgImage = ImageTk.PhotoImage(file='atm.jpg')

bgLabel = Label(card_entry, image=bgImage)
bgLabel.place(x=0, y=0)

Heading = Label(card_entry, text='Atm Simulator', font=('Times New Roman', 23, 'bold'),
                bg='LightPink1', fg='firebrick1')
Heading.pack()

# Card Number Label and Entry Field
CardNumLabel = Label(card_entry, text='Enter Your Card Number', font=('Times New Roman', 12, 'bold')
                     , bg='LightPink1', fg='firebrick1')
CardNumLabel.place(x=50, y=100)

cardNumEntry = Entry(card_entry, width=28, font=('Times New Roman', 12)
                     , bd=0, fg='firebrick1')
cardNumEntry.place(x=50, y=130)

# Atm Pin Label and Entry Field
atmPinLabel = Label(card_entry, text='Enter Your Atm Pin', font=('Times New Roman', 12, 'bold')
                    , bg='LightPink1', fg='firebrick1')
atmPinLabel.place(x=50, y=180)

atmPinEntry = Entry(card_entry, width=28, font=('Times New Roman', 12)
                    , bd=0, fg='firebrick1', show='*')
atmPinEntry.place(x=50, y=210)

# Eye Button
openEye = PhotoImage(file='closeye.png')
eyeButton = Button(card_entry, image=openEye, bd=0, bg='white', activebackground='white'
                   , cursor='hand2', command=show)
eyeButton.place(x=250, y=207)

# Enter Account Button
enterAccountButton = Button(card_entry, text='Enter into account', font=('Open Sans', 16, 'bold'),
                            fg='white', bg='firebrick1', activeforeground='white'
                            , activebackground='firebrick1', cursor='hand2', bd=0,
                            command=authenticate)
enterAccountButton.place(x=60, y=280)

# Buttons
checkBalanceButton = Button(card_entry, text='Check Balance', font=('Open Sans', 16, 'bold'),
                            fg='white', bg='white', activeforeground='white'
                            , activebackground='firebrick1', cursor='hand2', bd=0, width=15, command=showBalance,
                            state=tkinter.DISABLED)
checkBalanceButton.place(x=20, y=420)

withdrawButton = Button(card_entry, text='Withdraw Cash', font=('Open Sans', 16, 'bold'),
                        fg='white', bg='white', activeforeground='white'
                        , activebackground='firebrick1', cursor='hand2', bd=0, width=15, state=tkinter.DISABLED, command=withdraw)
withdrawButton.place(x=270, y=420)

depositButton = Button(card_entry, text='Deposit Cash', font=('Open Sans', 16, 'bold'),
                       fg='white', bg='white', activeforeground='white'
                       , activebackground='firebrick1', cursor='hand2', bd=0, width=15, state=tkinter.DISABLED, command=deposit)
depositButton.place(x=520, y=420)

card_entry.mainloop()