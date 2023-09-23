from tkinter import * 
import customtkinter
from transmitter import sendfile
from receiver import receive


root = customtkinter.CTk()

# This is the section of code which creates the main window
root.geometry('300x205')
root.title('Sharemio')
root.minsize(300, 205)
root.maxsize(300, 205)

frame = customtkinter.CTkFrame(root)
frame.pack(pady=24)

# This is the section of code which creates the a label
customtkinter.CTkLabel(frame, text='Receive').pack(padx=80)


# This is the section of code which creates a button
customtkinter.CTkButton(frame, text='Host receiving server', command=receive).pack(pady=10)


# This is the section of code which creates the a label
customtkinter.CTkLabel(frame, text='Send file').pack()


# This is the section of code which creates a button
customtkinter.CTkButton(frame, text='Select and send', command=sendfile).pack(pady=10)



# This is the section of code which creates the a label
customtkinter.CTkLabel(root, text='v1.4').place(x=8, y=180)


root.mainloop()