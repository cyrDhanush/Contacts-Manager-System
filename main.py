import display
import sqlhelper


d=display.Display()
s=sqlhelper.SQLhelper()



while True:

    d.printMainmenu()
    option=int(input('Enter the Option: '))


    if(option==1):
        s.addcontact()
    elif(option==2):
        s.showcontacts()
    elif(option==3):
        s.deletecontact()