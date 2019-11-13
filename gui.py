from tkinter import messagebox
import tkinter
import main

win1 = tkinter.Tk()
win1.geometry("500x200")
win1.title("Password Database")
l1 = tkinter.Label(win1, text="Welcome to Password Database!").grid(row=0, column=0)
l2 = tkinter.Label(win1, text="").grid(row=1, column=0)
entry = tkinter.Label(win1, text="1. Make a new entry")
entry.grid(row=2, column=0)
search = tkinter.Label(win1, text="2. Search for an existing entry")
search.grid(row=3, column=0)
update = tkinter.Label(win1, text="3. Update an existing entry")
update.grid(row=4, column=0)
choice = tkinter.Entry(win1, width=10)
choice.grid(row=5, column=0)


def entrygui():
    wini = tkinter.Tk()
    wini.geometry("500x200")
    wini.title("New Entry")
    entryl1 = tkinter.Label(wini, text="Enter name of the site: ")
    entryl2 = tkinter.Label(wini, text="Enter your username for the site: ")
    entryl3 = tkinter.Label(wini, text="Enter the password the site: ")
    entrye1 = tkinter.Entry(wini, width=20)
    entrye2 = tkinter.Entry(wini, width=20)
    entrye3 = tkinter.Entry(wini, width=20)
    entryl1.grid(row=0, column=0)
    entryl2.grid(row=1, column=0)
    entryl3.grid(row=2, column=0)
    entrye1.grid(row=0, column=1)
    entrye2.grid(row=1, column=1)
    entrye3.grid(row=2, column=1)

    def insertbt():
        site = str(entrye1.get()).lower()
        user = str(entrye2.get())
        passw = str(entrye3.get())
        main.insert(site, user, passw)
        messagebox.showinfo("Success!", "Entry added!")
        wini.destroy()

    insert = tkinter.Button(wini, text="Insert", command=insertbt)
    insert.grid(row=3, column=0)

    wini.mainloop()


def searchgui():
    wins = tkinter.Tk()
    wins.geometry("500x200")
    wins.title("Search")
    searchl1 = tkinter.Label(wins, text="Enter the name of the site: ")
    searchl1.grid(row=0, column=0)
    searche1 = tkinter.Entry(wins, width=20)
    searche1.grid(row=0, column=1)

    def searchbt():
        site = str(searche1.get()).lower()
        user, passw = main.search(site)
        messagebox.showinfo("Success!", "Username is "+user+"\nPassword is "+passw)
        wins.destroy()

    searchbtn = tkinter.Button(wins, text="Search", command=searchbt)
    searchbtn.grid(row=1, column=0)

    wins.mainloop()


def updategui():
    winu = tkinter.Tk()
    winu.geometry("500x200")
    winu.title("Update")
    caution = tkinter.Label(winu, text="Please select the option if you are updating the corresponding value")
    caution.grid(row=0, column=0)
    sitel = tkinter.Label(winu, text="Enter site name: ")
    sitee = tkinter.Entry(winu, width=20)
    userv = tkinter.IntVar(winu)
    userr = tkinter.Checkbutton(winu, text="New Username: ", variable=userv)
    passv = tkinter.IntVar(winu)
    passr = tkinter.Checkbutton(winu, text="New Password: ", variable=passv)
    usere = tkinter.Entry(winu, width=20)
    passe = tkinter.Entry(winu, width=20)
    sitel.grid(row=1, column=0)
    sitee.grid(row=1, column=1)
    userr.grid(row=2, column=0)
    usere.grid(row=2, column=1)
    passr.grid(row=3, column=0)
    passe.grid(row=3, column=1)

    def updatebt():
        userval = int(userv.get())
        passval = int(passv.get())
        site = str(sitee.get()).lower()
        if userval == 1 and passval == 0:
            user = str(usere.get())
            passw = None
            main.update(site, user, passw)
            messagebox.showinfo("Success", "Username updated")
            winu.destroy()
        elif userval == 0 and passval == 1:
            user = None
            passw = passe.get()
            main.update(site, user, passw)
            messagebox.showinfo("Success", "Password updated")
            winu.destroy()
        elif userval == 1 and passval == 1:
            user = str(usere.get())
            passw = str(passe.get())
            main.update(site, user, passw)
            messagebox.showinfo("Success", "Username and password updated")
            winu.destroy()
        elif userval == 0 and passval == 0:
            messagebox.showinfo("Error", "Please check a box")

    updatebtn = tkinter.Button(winu, text="Update", command=updatebt)
    updatebtn.grid(row=4, column=0)

    winu.mainloop()


def choicefn():
    ch = int(choice.get())
    if ch == 1:
        entrygui()
    elif ch == 2:
        searchgui()
    elif ch == 3:
        updategui()
    else:
        messagebox.showinfo("ERROR", "Please enter a valid choice")


submit = tkinter.Button(win1, text="Submit", command=choicefn).grid(row=5, column=1)
win1.mainloop()
