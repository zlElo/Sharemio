import socket
import os
import customtkinter
from tkinter import * 
from tkinter import filedialog
import time


def sendfile():
    def go():
        SEPARATOR = "<SEPARATOR>"
        BUFFER_SIZE = 4096
        host = inputfield.get()
        port = 5001
        filename = filedialog.askopenfilename()
        filesize = os.path.getsize(filename)
        uploaded = 0
        s = socket.socket()

        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected.")

        s.send(f"{filename}{SEPARATOR}{filesize}".encode())

        with open(filename, "rb") as f:
            start = time.perf_counter()
            last_update = start
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                s.sendall(bytes_read)
                uploaded += len(bytes_read)
                done = int(50*uploaded/filesize)
                if not bytes_read:
                    break
                progress.set(done/50)

                time_elapsed = time.perf_counter() - last_update
                if time_elapsed >= 3:
                    time_elapsed_total = time.perf_counter() - start
                    calculated_speed = round(uploaded/time_elapsed_total/1000000, 2)
                    speed.configure(text=f"{calculated_speed} MB/s")
                    last_update = time.perf_counter()

                root.update_idletasks()
        s.close()
        print('[+] done')


    root = customtkinter.CTk()

    # This is the section of code which creates the main window
    root.geometry('291x156')
    root.title('Send file')

    inputfield = customtkinter.CTkEntry(root, placeholder_text="IP of host")
    inputfield.place(x=29, y=40)
    customtkinter.CTkButton(root, text='Ok', command=go, width=10).place(x=180, y=40)

    # This is the section of code which creates a progress bar
    progress=customtkinter.CTkProgressBar(root)
    progress.place(x=29, y=103)

    speed = customtkinter.CTkLabel(root, text='')
    speed.place(x=29, y=113)


    root.mainloop()