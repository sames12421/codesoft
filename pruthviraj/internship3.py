import os

class contact:
    def __init__(self,name,ph_no,email,adrs):
        self.name=name
        self.ph_no=ph_no
        self.email=email
        self.adrs=adrs

l=[]
def add():
    n=input("Enter contact name: ")
    p=int(input("Enter Phone Number: "))
    e=input("Enter the email address: ")
    a=input("Enter Address: ")
    l.append(contact(n,p,e,a))

def view():
    if(len(l)==0):
        print("Contact List is empty")
    else:
        print("--------Contact List--------")
        for i in range(len(l)):
            print("----------------------------")
            print("Contact No:",i+1)
            print("Name:",l[i].name)
            print("Phone Number:",l[i].ph_no)
            print("Email:",l[i].email)
            print("Address",l[i].adrs)
        print("------------End-------------")

def search():
    if(len(l)==0):
        print("Contact List is empty")
    else:
        f=input("Enter the Name of contact: ")
        f1=True
        for i in range(len(l)):
            if(l[i].name==f):
                print("Contact Found...")
                print("----------------------------")
                print("Contact No:",i+1)
                print("Name:",l[i].name)
                print("Phone Number:",l[i].ph_no)
                print("Email:",l[i].email)
                print("Address",l[i].adrs)
                print("----------------------------")
                f1=False
                break
        if(f1):
            print("Contact not found in list")

def delete():
    if(len(l)==0):
        print("Contact List is empty")
    else:
        f=input("Enter the Name of contact: ")
        f1=True
        for i in range(len(l)):
            if(l[i].name==f):
                l.pop(i)
                f1=False
                print("Contact has been deleted")
                break
        if(f1):
            print("Contact not found in list")

def update():
    if(len(l)==0):
        print("Contact List is empty")
    else:
        f=input("Enter the Name of contact: ")
        f1=True
        for i in range(len(l)):
            if(l[i].name==f):
                print("Enter Updated Details for",l[i].name)
                l[i].ph_no=int(input("Enter Phone Number: "))
                l[i].email=input("Enter the email address: ")
                l[i].adrs=input("Enter Address: ")
                print("Contact details have been updated")
                f1=False
                break
        if(f1):
            print("Contact not found in list")

while(True):
    print("\n----------------Menu-----------------\n1) Add Contact\n2) View Contact List\n3) Search Contact\n4) Update Contact\n5) Delete Contact\n6) Exit\n-------------------------------------")
    ch=int(input("Enter your choice: "))
    match ch:
        case 1:
            add()
        case 2:
            view()
        case 3:
            search()
        case 4:
            update()
        case 5:
            delete()
        case 6:
            break
        case _:
            print("Invalid Chocie")