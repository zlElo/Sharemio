import customtkinter

def progress_done():
    window = customtkinter.CTk()
    window.title('done!')

    customtkinter.CTkLabel(window, text='The progress is done!', text_color='green').pack(pady=10, padx=10)

    window.mainloop()