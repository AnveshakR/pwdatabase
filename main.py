import sqlite3
import string

db = sqlite3.connect('pwprotect.db')


def home():
    print("Welcome to Password Database!")
    print()
    print("1. Make a new entry")
    print("2. Search in existing entries")
    print("3. Update an existing entry")
    ch = int(input("Enter your choice: "))
    print()
    if ch == 1:
        insert()
    if ch == 2:
        search()
    if ch == 3:
        update()


def insert():
    while True:
        print()
        sitename = input("Enter the name of the site: ").lower()
        username = input("Enter your username for the site: ")
        password = ""
        ch = input("Do you want to use our generated password?(y/n): ")
        if ch == "y":
            password = pwgenerator()
            print("Your generated password is ", password)
        elif ch == "n":
            password = input("Enter your password for the site: ")

        entities = (sitename, username, password)
        cursor = db.cursor()
        cursor.execute('INSERT INTO INFO(SITENAME,USERNAME,PASSWORD) VALUES (?,?,?)', entities)
        db.commit()
        ch = input("Do you want to make another entry?(y/n): ")
        if ch == 'n':
            ch = input("Do you want to return to home screen?(y/n): ")
            print()
            if ch == 'y':
                home()

            elif ch == 'n':
                print("Thank you for using Password Database")
                return

        elif ch == 'y':
            continue

        else:
            print("Invalid input")
            home()


def search():
    while True:
        site = input('Enter the name of the site: ').lower()
        csr = db.cursor()
        csr.execute('SELECT USERNAME, PASSWORD FROM INFO WHERE SITENAME == ?', (site,))
        rows = csr.fetchall()
        for row in rows:
            print("Username, Password: ", row)

        ch = input("Do you want to search again?(y/n): ")
        if ch == 'n':
            ch = input("Do you want to return to home screen?(y/n): ")
            print()
            if ch == 'y':
                home()
                break

            elif ch == 'n':
                print("Thank you for using Password Database")
                return

        elif ch == 'y':
            continue

        else:
            print("Invalid input")
            home()
            break


def update():
    while True:
        site = input('Enter the name of the site: ').lower()
        ch = int(input("1 = Change Username, 2 = Change Password: "))
        csr = db.cursor()
        if ch == 1:
            user = input("Enter new username: ")
            csr.execute('UPDATE INFO SET USERNAME = ? WHERE SITENAME = ?', (user, site))
            db.commit()
            print("Your new username is ", user)

        elif ch == 2:
            passw = ""
            c = input("Do you want to use our generated password?(y/n): ")
            if c == "y":
                passw = pwgenerator()
            elif c == "n":
                passw = input("Enter new password: ")
            csr.execute('UPDATE INFO SET PASSWORD = ? WHERE SITENAME = ?', (passw, site))
            db.commit()
            print("Your new password is ", passw)

        else:
            print("Invalid input")
            home()

        ch = input("Do you want to update again?(y/n): ")

        if ch == 'n':
            ch = input("Do you want to return to home screen?(y/n): ")
            print()
            if ch == 'y':
                home()
                break

            elif ch == 'n':
                print("Thank you for using Password Database")
                return

        elif ch == 'y':
            continue

        else:
            print("Invalid input")
            home()
            break


def pwgenerator():
    import random
    pw = ""
    lower = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z" ]
    upper = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z" ]
    digits = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    special = [ "@", "%", "+", '/', "!", "#", "$", "^", "?", ":", ",", ".", "_", "-" ]
    i = 0
    while i <= 15:
        n = random.randint(0, 4)
        if n == 1:
            pw = pw + random.choice(lower)
        elif n == 2:
            pw = pw + random.choice(upper)
        elif n == 3:
            pw = pw + random.choice(digits)
        elif n == 4:
            pw = pw + random.choice(special)
        i += 1
    return pw


home()
