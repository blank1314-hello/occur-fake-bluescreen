#occur bluescreen
import tkinter as tk

def show_blue_screen():
    root = tk.Tk()
    root.title("블루스크린")
    
    root.attributes('-fullscreen', True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    root.configure(bg="blue")
    
    label = tk.Label(root, text="A problem has been detected and Windows has been shut down to prevent damage.\n\n"
                               "If this is the first time you've seen this Stop error screen,\n"
                               "restart your computer. If this screen appears again, follow these steps:\n\n"
                               "Check for viruses on your computer. Remove any newly installed hard drives\n"
                               "or hard drive controllers. Check your hard drive to make sure it is properly configured\n"
                               "and terminated.\n\n"
                               "Technical information:\n\n*** STOP: 0x0000007B (0xF78D2524, 0xC0000034, 0x00000000, 0x00000000)",
                    fg="white", font=("Courier", 16), bg="blue", justify="left")
    label.pack(padx=20, pady=20)
    
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    
    root.attributes('-topmost', True)
    
    root.after(5000, lambda: bring_to_front(root))
    
    root.mainloop()

def bring_to_front(root):
    root.attributes('-topmost', True)
    
    root.after(5000, lambda: bring_to_front(root))

show_blue_screen()
