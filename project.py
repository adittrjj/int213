import os
from tkinter import *

gui = Tk()
var=IntVar()
def getvals():
    print("Submitting form")

    print(f"{namevalue.get(), registervalue.get(), sectionvalue.get()} ")

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), registervalue.get(), sectionvalue.get()}\n ")

gui.geometry("720x400")
#Heading
Label(gui, text="Welcome To Python QUIZ ", font="comicsansms 25 bold", pady=35, width=25, fg="blue").grid(row=0, column=3)

#Text for our form
name = Label(gui, text="Name")
register = Label(gui, text="Registeration No.")
section = Label(gui, text="Section")
level=Label(gui,text="Level")

#Pack text for our form
name.grid(row=1, column=2)
register.grid(row=2, column=2)
section.grid(row=3, column=2)
level.grid(row=4,column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
registervalue = StringVar()
sectionvalue = StringVar()


#Entries for our form
nameentry = Entry(gui, textvariable=namevalue)
registerentry = Entry(gui, textvariable=registervalue)
sectionentry = Entry(gui, textvariable=sectionvalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
registerentry.grid(row=2, column=3)
sectionentry.grid(row=3, column=3)
Radiobutton(gui,text="Easy",padx= 20, variable= var, value=1).grid(row=4,column=3)
Radiobutton(gui,text="Med.",padx= 20, variable= var, value=2).grid(row=5,column=3)
Radiobutton(gui,text="Hard",padx= 20, variable= var, value=3).grid(row=6,column=3)
Button(text="SUBMIT", command=getvals,width=10,bg="blue", fg="white").grid(row=7, column=3)

#To start the Test
def run():
	os.system('main.py')
#Button & packing it and assigning it a command
Button(text="START TEST", command=run,width=10, bg="red", fg="white", font=("ariel", 10, " bold")).grid(row=9, column=3)

# set the title of the Window
gui.title("Submit Form")

# Start the GUI
gui.mainloop()
# END OF THE PROGRAM
