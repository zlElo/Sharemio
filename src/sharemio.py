from tkinter import * 
import customtkinter
from transmitter import sendfile
from receiver import receive
import pyuac
from settings import settings_window


def admin_for_settings():
    if pyuac.isUserAdmin():
        settings_window()
    else:
        root.destroy()
        print("[log] re-launching as admin")
        pyuac.runAsAdmin() 

root = customtkinter.CTk()

# This is the section of code which creates the main window
root.geometry('300x205')
root.title('Sharemio')
root.minsize(300, 205)
root.maxsize(300, 205)
root.iconbitmap('src/icon.ico')


if pyuac.isUserAdmin():
    settings_window()

    
# This is the section of code which creates a button
customtkinter.CTkButton(root, text='⚙', command=admin_for_settings, width=10).place(x=265, y=3)

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