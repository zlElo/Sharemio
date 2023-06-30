import socket
import os
import customtkinter


def receive():
    def openserv():
        # device's IP address
        SERVER_HOST = "0.0.0.0"
        SERVER_PORT = 5001
        # receive 4096 bytes each time
        BUFFER_SIZE = 4096
        SEPARATOR = "<SEPARATOR>"

        # create the server socket
        # TCP socket
        s = socket.socket()

        # bind the socket to our local address
        s.bind((SERVER_HOST, SERVER_PORT))

        # enabling our server to accept connections
        # 5 here is the number of unaccepted connections that
        # the system will allow before refusing new connections
        s.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
        status.configure(text='Status: up')
        root.update_idletasks()
        root.update()

        # accept connection if there is any
        client_socket, address = s.accept() 
        # if below code is executed, that means the sender is connected
        print(f"[+] {address} is connected.")

        # receive the file infos
        # receive using client socket, not server socket
        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        # remove absolute path if there is
        filename = os.path.basename(filename)
        # convert to integer
        filesize = int(filesize)
        downloaded = 0

        with open(filename, "wb") as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    # nothing is received
                    # file transmitting is done
                    break
            # write to the file the bytes we just received
                f.write(bytes_read)
                downloaded += len(bytes_read)
                done_ = int(50*downloaded/filesize)
                # update the progress bar
                progress.set(done_/50)
                root.update_idletasks()

        client_socket.close()
        # close the server socket
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
