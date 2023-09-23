import errno
import socket
import os
import customtkinter
from ip import get_local_ip
import time
import threading
from info_window import progress_done
import json

def connection_timeouted():
    root = customtkinter.CTk()
    root.title('timeout')
    
    customtkinter.CTkLabel(root, text='The connection is timeouted! Try again...').pack(pady=10, padx=10)

    root.mainloop()

def receive():
    def openserv():
        with open('src\settings.json', 'r') as f:
            data = json.load(f) # load the JSON data spom the file
            path_to_save = data['out_path']
            
        SERVER_HOST = "0.0.0.0"
        SERVER_PORT = 5001
        BUFFER_SIZE = 2048 * 2048
        SEPARATOR = "<SEPARATOR>"

        s = socket.socket()
        s.setblocking(False)
        
        s.bind((SERVER_HOST, SERVER_PORT))
        s.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
        status.configure(text='Status: up')
        root.update_idletasks()
        root.update()
        
        # set timelimit of 60 seconds to connect
        s.settimeout(60)

        try:
            client_socket, address = s.accept() 
        except socket.timeout:
            print("[-] Connection timed out")
            s.close()
            status.configure(text='Status: timeouted')
            connection_timeouted()
            return

        print(f"[+] {address} is connected.")

        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)

        filename = os.path.basename(filename)

        filesize = int(filesize)
        downloaded = 0

        with open(f'{path_to_save}/{filename}', "wb") as f:
            start = time.perf_counter()
            last_update = start
            
            while downloaded < filesize:
                try:
                    bytes_read = client_socket.recv(BUFFER_SIZE)
                except socket.error as e:
                    if e.errno == errno.EWOULDBLOCK:
                        continue
                    else:
                        raise
                if not bytes_read:    
                    break
                f.write(bytes_read)
                downloaded += len(bytes_read)
                done_ = int(50*downloaded/filesize)
                # update the progress bar
                progress.set(done_/50)

                time_elapsed = time.perf_counter() - last_update
                if time_elapsed >= 1:
                    time_elapsed_total = time.perf_counter() - start
                    calculated_speed = round(downloaded/time_elapsed_total/1000000, 2)
                    speed.configure(text=f"{calculated_speed} MB/s")
                    last_update = time.perf_counter()

                root.update_idletasks()

        client_socket.close()
        s.close()
        print('[+] done')
        progress_done()


    def btn_function():
        openserver_thread = threading.Thread(target=openserv)
        openserver_thread.start()
        

    root = customtkinter.CTk()

    # This is the section of code which creates the main window
    root.geometry('291x156')
    root.title('Host for receive')
    root.minsize(291, 156)
    root.maxsize(291, 156)
    root.iconbitmap('src/icon.ico')

    frame = customtkinter.CTkFrame(root)
    frame.pack(pady=10)

    customtkinter.CTkButton(frame, text='Open server', command=btn_function).pack(pady=10)
    status = customtkinter.CTkLabel(frame, text='Status: down')
    status.pack()
 
    customtkinter.CTkLabel(root, text=f'Your local IP: {get_local_ip()}').pack()

    # This is the section of code which creates a progress bar
    progress=customtkinter.CTkProgressBar(frame)
    progress.pack(padx=30)

    speed = customtkinter.CTkLabel(frame, text='0 mb/s')
    speed.pack()


    root.mainloop()