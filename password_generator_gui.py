from tkinter import *
import pyperclip
import random

gui = Tk()

gui.geometry("370x300")   
gui.configure(bg="#7E87FF")

passstr  = StringVar()
passkey  = StringVar()
charchanged = StringVar()
passlen  = IntVar()
selected = StringVar()
gentype  = IntVar()

# setting the length of the password to zero initially
passlen.set(0)
charchanged.set(0)
passkey.set('')

# function to generate the password
def generate():
    choice = selected.get()

    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    pass2 = ['1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    # declaring the empty string
    password = ""
    
    if choice == "string":
        password_key = list(passkey.get())
        c = 0
        while c <= int(charchanged.get()):
            k = random.randrange(len(passkey.get()))
            password_key[k] = random.choice(pass2)
            password = "".join(password_key)
            c = c+1
    else:
    # storing the keys in a list which will be used to generate 
    # the password 

        # loop to generate the random password of the length entered           
        # by the user
        for x in range(passlen.get()):
            password = password + random.choice(pass1)
    
        # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

def chose1():
    l1.grid(row=3,columnspan=2)
    e1.grid(row=4,columnspan=2)

    l2.grid_forget() 
    e2.grid_forget() 
    l3.grid_forget() 
    e3.grid_forget() 
def chose2():
    l1.grid_forget()
    e1.grid_forget()

    l2.grid(row=3,columnspan=2) 
    e2.grid(row=4,columnspan=2) 
    l3.grid(row=5,columnspan=2) 
    e3.grid(row=6,columnspan=2) 


# Creating a text label widget
Label(gui, text="Password Generator Application", font="calibri 20 bold", justify=CENTER).grid(row=0,columnspan=2)

Radiobutton(gui, text='Generate random password', value='random', variable=selected, command=chose1, tristatevalue=0, bg="#7E87FF").grid(row=1,columnspan=2)
Radiobutton(gui, text='Generate password from string', value='string', variable=selected, command=chose2, tristatevalue=0, bg="#7E87FF").grid(row=2,columnspan=2)

l1 = Label(gui, text="Enter password length")
e1 = Entry(gui, textvariable=passlen)


l2 = Label(gui, text="How many characters should  be changed")
e2 = Entry(gui, textvariable=charchanged)

l3 = Label(gui, text="Enter string on which password will be created")
e3 = Entry(gui, textvariable=passkey)

# button to call the generate function
Button(gui, text="Generate Password", command=generate, justify=RIGHT).grid(row=10, column=0, sticky="ew")

# entry widget to show the generated password
Label(gui, textvariable=passstr).grid(row=9,columnspan=2)

# button to call the copytoclipboard function
Button(gui, text="Copy to clipboard", command=copytoclipboard, justify=LEFT).grid(row=10, column=1, sticky="ew")

for widget in gui.winfo_children():
        # check whether widget is instance of Label
        if isinstance(widget, Label):
            widget.config(bg="#7E87FF")

# mainloop() is an infinite loop used to run the application when 
# it's in ready state 
gui.mainloop()