from tkinter import * 
import customtkinter
from transmitter import sendfile
from receiver import receive


root = customtkinter.CTk()

# This is the section of code which creates the main window
root.geometry('432x135')
root.title('Sharemio')


# This is the section of code which creates the a label
customtkinter.CTkLabel(root, text='Receive').place(x=29, y=30)


# This is the section of code which creates a button
customtkinter.CTkButton(root, text='Host receiving server', command=receive).place(x=29, y=66)


# This is the section of code which creates the a label
customtkinter.CTkLabel(root, text='Send file').place(x=261, y=30)


# This is the section of code which creates a button
customtkinter.CTkButton(root, text='Select and send', command=sendfile).place(x=262, y=66)


root.mainloop()