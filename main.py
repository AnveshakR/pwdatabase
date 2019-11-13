import sqlite3
import os
from cryptography.fernet import Fernet

path = r"C:\Users\anves\PycharmProjects\pwdatabase\pwprotect.db"


def dbcreate():
    db = sqlite3.connect('pwprotect.db')
    csr = db.cursor()
    csr.execute("CREATE TABLE INFO(SITENAME TEXT, USERNAME TEXT, PASSWORD TEXT, PWKEY TEXT)")


if not os.path.exists(path):
    dbcreate()

db = sqlite3.connect('pwprotect.db')


def insert(sitename, username, password):

    enk, key = encrypt(password)
    entities = (sitename, username, enk, key)
    cursor = db.cursor()
    cursor.execute('INSERT INTO INFO(SITENAME,USERNAME,PASSWORD,PWKEY) VALUES (?,?,?,?)', entities)
    db.commit()

    return


def search(site):
    csr = db.cursor()
    csr.execute('SELECT USERNAME, PASSWORD, PWKEY FROM INFO WHERE SITENAME == ?', (site,))
    row = csr.fetchone()
    if row is not None:
        username = row[0]
        enk = row[1]
        key = row[2]
    else:
        # print("Data not found")
        # home()
        return "not found", "not found"
    password = decrypt(enk, key)

    return username, password


def update(site, user, passw):
    csr = db.cursor()
    if passw is None:
        # user = input("Enter new username: ")
        csr.execute('UPDATE INFO SET USERNAME = ? WHERE SITENAME = ?', (user, site))
        db.commit()

    elif user is None:

        enk, key = encrypt(passw)

        csr.execute('UPDATE INFO SET PASSWORD = ? WHERE SITENAME = ?', (enk, site))
        csr.execute('UPDATE INFO SET PWKEY = ? WHERE SITENAME = ?', (key, site))
        db.commit()

    else:
        enk, key = encrypt(passw)
        csr.execute('UPDATE INFO SET USERNAME = ? WHERE SITENAME = ?', (user, site))
        csr.execute('UPDATE INFO SET PASSWORD = ? WHERE SITENAME = ?', (enk, site))
        csr.execute('UPDATE INFO SET PWKEY = ? WHERE SITENAME = ?', (key, site))
        db.commit()


def pwgenerator():
    import random
    pw = ""
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special = ["@", "%", "+", '/', "!", "#", "$", "^", "?", ":", ",", ".", "_", "-"]
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
    print(pw)
    return pw


def encrypt(pw):
    key = Fernet.generate_key()
    f = Fernet(key)
    b = bytes(pw, 'utf-8')
    encoded = f.encrypt(b)
    return encoded, key


def decrypt(enk, key):
    f = Fernet(key)
    decoded = f.decrypt(enk)
    pw = str(decoded.decode('utf-8'))
    return pw
