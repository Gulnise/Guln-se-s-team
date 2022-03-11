from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

# Heading
Label(root , text="Python Registration Form",font="arial 15 bold").grid(row=0,column=3)

# Field name
name=Label(root, text="name")
phone=Label(root, text="phone")
email=Label(root, text="email")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
email.grid(row=3,column=2)

# Variable for storing data
namevalue=StringVar
phonevalue=StringVar
emailevalue=StringVar
checkvalue=IntVar

# Creating entry field
nameentry= Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
emailentry=Entry(root, textvariable=emailevalue)

# Packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)

# Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

#Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()