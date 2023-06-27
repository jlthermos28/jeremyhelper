# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
 
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
def openNewPre():
    submission_model = tk.StringVar()
    submission_tag = tk.StringVar()
    submission_username=tk.StringVar()
    submission_image=tk.StringVar()
    submission_finalstep=tk.StringVar()
    submission_da=tk.StringVar()
    submission_bios=tk.StringVar()
    submission_software=tk.StringVar()
    submission_thermal=tk.StringVar()
    submission_location=tk.StringVar()
    submission_shelf=tk.StringVar()


    def submitnew():
        subwindow = Toplevel(newWindow)
        subwindow.title("Output")
        subwindow.geometry("600x500")

        #getting all the components of the predeploy
        submissionmodel=submission_model.get()
        submissiontag=submission_tag.get()
        submissionusername=submission_username.get()
        submissionimage=submission_image.get()
        submissionfinalstep=submission_finalstep.get()
        submissionda=submission_da.get()
        submissionbios=submission_bios.get()
        submissionsoftware=submission_software.get()
        submissionthermal=submission_thermal.get()
        submissionlocation=submission_location.get()
        submissionshelf=submission_shelf.get()

        def copy_to_clipboard():
                subwindow.clipboard_clear()  # Optional.
                subwindow.clipboard_append(usableoutput.get("1.0", 'end'))
                #subwindow.update()
                #subwindow.destroy()


      

        
        
        
        outputlabel = submissionmodel + ' Tag ' + submissiontag + ' was reserved in Stock Tracking under ' + submissionusername +'. It is imaged with a '+ submissionimage +' image, it was final stepped as ' + submissionfinalstep +', joined to the domain, desktop and user were added as administrators. Windows updates are up to date. AD description has been changed, DA '+ submissionda +' moved it into the appropriate OU. GPUpdate was run, and Trellix installed successfully. Bios is updated to '+ submissionbios + ' and boot settings were checked. PGP Fix was run. '+ submissionsoftware + ' was installed. Thermal Drivers were updated and Lenovo Intelligent Solution was '+ submissionthermal + ' in services.  Computer is in '+ submissionlocation + ' on '+ submissionshelf + '.'
        
        #outputlabel.pack()

        usableoutput = tk.Text(subwindow, height= 20, width= 400)
        usableoutput.insert(tk.END, outputlabel)
        usableoutput.pack()


        copybutton = Button(subwindow, text="Copy", command= lambda: copy_to_clipboard())
        copybutton.pack()

        #submission_var.set("")

        
     



    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Predeploy")
 
    # sets the geometry of toplevel
    newWindow.geometry("1000x500")

    Label(newWindow, anchor= "w", justify="left", text="Enter the model type (Ex. T16)").grid(sticky = W, row=0, column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter the tag").grid(sticky = W, row=1, column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter the user's full name (Ex. Jane Doe)").grid(sticky = W, row=2, column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter the image type (Ex. Fac/Staff 2022)").grid(sticky = W, row=3, column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter what it was final stepped as (Ex. Staff)").grid(sticky = W, row=4, column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter the DA that moved it to the OU").grid(sticky = W, row=5,column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter the Bios version and date").grid(sticky = W, row=6, column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter the names only of any software installed separated by commas (Ex. Jabber, VSCode, etc.)").grid(sticky = W, row=7,column=0)
    Label(newWindow, anchor= "w", justify="left", text="What is the status of the Lenovo Intelligent Thermal Solution? (enabled, disabled, left alone)").grid(sticky = W, row=8, column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter the Building").grid(sticky = W, row=9,column=0)
    Label(newWindow, anchor= "w", justify="left", text="Enter the Shelf or Cabinet it is in").grid(sticky = W, row=10,column=0)



        

    model = tk.Entry(newWindow, textvariable=submission_model)
    tag = tk.Entry(newWindow, textvariable=submission_tag)
    username = tk.Entry(newWindow, textvariable=submission_username)
    image = tk.Entry(newWindow, textvariable=submission_image)
    finalstep = tk.Entry(newWindow, textvariable=submission_finalstep)
    da = tk.Entry(newWindow, textvariable=submission_da)
    bios = tk.Entry(newWindow, textvariable=submission_bios)
    software = tk.Entry(newWindow, textvariable=submission_software)
    thermal = tk.Entry(newWindow, textvariable=submission_thermal)
    location = tk.Entry(newWindow, textvariable=submission_location)
    shelf = tk.Entry(newWindow, textvariable=submission_shelf)







    testbutton= tk.Button(newWindow, text="submit", command=submitnew)

    model.grid(row=0, column=2)
    tag.grid(row=1, column=2)
    username.grid(row=2, column=2)
    image.grid(row=3, column=2)
    finalstep.grid(row=4, column=2)
    da.grid(row=5, column=2)
    bios.grid(row=6, column=2)
    software.grid(row=7, column=2)
    thermal.grid(row=8, column=2)
    location.grid(row=9, column=2)
    shelf.grid(row=10, column=2)



    testbutton.grid(row=12, column=2)

    


 
 
label = Label(master,
              text ="This is the main window")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btnpre = Button(master,
             text ="Predeploy Template",
             command = openNewPre)
btnpre.pack(pady = 10)







# mainloop, runs infinitely
mainloop()