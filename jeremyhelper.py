# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
 
# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("1200x500")

master.title("WELCOME TO THE JEREMY HELPER!")

Label(master, text ="WARNING, CLOSING THIS WINDOW WILL RESULT IN CLOSING ALL SUBSEQUENT WINDOWS THAT YOU OPENED USING THE BUTTONS BELOW", foreground= "white", background="red", font= 100, relief= "ridge").pack()



Message(master, text = "WELCOME TO THE JEREMY HELPER! THIS PROGRAM IS DESIGNED TO GIVE YOU A SHORTCUT FOR EVERYTHING RELATED TO CSR'S BECAUSE YOU'RE LAZY!", foreground= "white", 
        font=90, width=1000, justify="center", background= "blue").pack(pady = 10)
 
 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Test Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window", foreground= "blue").pack()
 
 
label = Label(master,
              text ="This is the main window")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btnpre = Button(master,
             text ="Test button #1",
             command = openNewWindow)
btnpre.pack(pady = 10)





btnpostdep = Button(master, text="Test button #2", command = openNewWindow)


btnpostdep.pack()
# mainloop, runs infinitely
mainloop()