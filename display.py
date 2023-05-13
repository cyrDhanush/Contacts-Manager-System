class Display:
    def printMainmenu(self):
        print("\n\nWelcome to Contact Manager")
        print("1. Add Contacts")
        print("2. Show Contacts")
        print("3. Delete Contacts\n\n")
    
    def showallcontacts(self, data):
        if(len(data)>0):
            print("Id\tPhoneNo \tName")
            for i in data:
                print(i[0], i[2], i[1], sep='\t')
        else:
            print("No contacts stored")
