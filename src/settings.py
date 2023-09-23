import customtkinter
import json
from tkinter import filedialog


def setup_path(selected_path, path_label, status):

    with open('src\settings.json', 'r+') as f:
        data = json.load(f) 
        data['out_path'] = selected_path
        f.seek(0) 
        json.dump(data, f, indent=4) 

    path_label.configure(text=f'actual path: {selected_path}')
    status.configure(text='✅')
        


def settings_window():
    root = customtkinter.CTk()
    root.title('⚙-Settings')
    root.geometry('300x200')
    root.iconbitmap('src/icon.ico')

    with open('src\settings.json', 'r') as f:
        data = json.load(f) # load the JSON data spom the file
        path_to_save = data['out_path']

    frame = customtkinter.CTkFrame(root)
    frame.pack(pady=25)

    customtkinter.CTkLabel(frame, text='Default ouput path:').pack(padx=70, pady=10)

    customtkinter.CTkButton(frame, text='select', width=10, command=lambda: setup_path(filedialog.askdirectory(), path_label, status)).pack()

    path_label = customtkinter.CTkLabel(frame, text=f'actual path: {path_to_save}')
    path_label.pack(pady=20)

    status = customtkinter.CTkLabel(root, text='')
    status.place(x=3, y=175)

    root.mainloop()

settings_window()