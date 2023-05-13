import sqlite3
import display

d=display.Display()

class SQLhelper:
    conn=sqlite3.connect('contacts.db')
    cur=conn.cursor()
    def __init__(self):
        # creating table in database
        try: 
            cmd='''CREATE TABLE phno(id INTEGER PRIMARY KEY, name STRING , phonenumber INTEGER UNIQUE);'''
            self.conn.execute(cmd)
        except:
            pass

    def addcontact(self):
        phoneno=int(input("Enter Phone Number: "))
        name=input("Enter name: ")
        cmd='''INSERT INTO phno(id, name, phonenumber) VALUES (NULL,'{}','{}')'''.format(name, phoneno)
        try:
            self.cur.execute(cmd)
            self.conn.commit()
            print('Successfully Saved')
        except:
            print('Sorry ERROR occured')
    
    def showcontacts(self):
        da=self.conn.execute('''SELECT * FROM phno''')
        data=da.fetchall()
        d.showallcontacts(data)

    def deletecontact(self):
        self.showcontacts()
        delid=int(input("Enter ID to delete contact: "))
        try:
            self.cur.execute('''DELETE FROM phno WHERE id={}'''.format(delid))
            self.conn.commit()
        except:
            print("Invalid ID")

        
