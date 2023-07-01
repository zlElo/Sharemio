import socket
import os
import customtkinter


def receive():
    def openserv():
        SERVER_HOST = "0.0.0.0"
        SERVER_PORT = 5001
        BUFFER_SIZE = 4096
        SEPARATOR = "<SEPARATOR>"

        s = socket.socket()

        
        s.bind((SERVER_HOST, SERVER_PORT))
        s.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
        status.configure(text='Status: up')
        root.update_idletasks()
        root.update()

        client_socket, address = s.accept() 
    
        print(f"[+] {address} is connected.")

    
        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
       
        filename = os.path.basename(filename)
       
        filesize = int(filesize)
        downloaded = 0

        with open(filename, "wb") as f:
            while True:
                
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    break
                f.write(bytes_read)
                downloaded += len(bytes_read)
                done_ = int(50*downloaded/filesize)
                # update the progress bar
                progress.set(done_/50)
                root.update_idletasks()

        client_socket.close()
        s.close()
        print('[+] done')

        

    root = customtkinter.CTk()

    # This is the section of code which creates the main window
    root.geometry('291x156')
    root.title('Host for receive')

    customtkinter.CTkButton(root, text='Open server', command=openserv).place(x=29, y=40)
    status = customtkinter.CTkLabel(root, text='Status: down')
    status.place(x=190, y=40)

    # This is the section of code which creates a progress bar
    progress=customtkinter.CTkProgressBar(root)
    progress.place(x=29, y=103)


    root.mainloop()
