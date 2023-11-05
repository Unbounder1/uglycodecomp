import pyWinhook 
from threading import Timer
import win32gui
import logging
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import socket


# Initialize the main application window
root = tk.Tk()
root.withdraw()  # Hide the main window (optional)

def show_popup(timer):
    popup = tk.Toplevel()
    popup.title("Popup Title")
    
    # Load and display the image (assuming the image is in the same directory)
    image = Image.open("circle.png").resize((1200,700))  # Replace with your image path
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(popup, text="Go touched grass nerd. Time Remaining: "+str(timer)+" You live in Troy, NY", compound=tk.TOP, image=photo)
    label.photo = photo  # keep a reference!
    label.pack()
    root.mainloop()
    
class blockInput():
    def OnKeyboardEvent(self,event):
        return False

    def OnMouseEvent(self,event):
        return False
    
    def unblock(self):
        logging.info(" -- Unblock!")
        if self.t.is_alive():
            self.t.cancel()
        try: self.hm.UnhookKeyboard()
        except: pass
        try: self.hm.UnhookMouse()
        except: pass

    def block(self, timeout = 10, keyboard = True, mouse = True):
        self.t = Timer(timeout, self.unblock)
        self.t.start()

        logging.info("Loading!")
        if mouse:
            self.hm.MouseAll = self.OnMouseEvent
            self.hm.HookMouse()
        if keyboard:
            self.hm.KeyAll = self.OnKeyboardEvent
            self.hm.HookKeyboard()
        win32gui.PumpWaitingMessages()

    def __init__(self):
        self.hm = pyWinhook.HookManager()

def check():
    logging.basicConfig(level=logging.INFO)

    block = blockInput()
    block.block()

    import time
    t0 = time.time()
    while time.time() - t0 < 6000:
        time.sleep(1)
        show_popup(int(6000 - (time.time() - t0)))
        print(int(time.time() - t0))

    block.unblock()
    logging.info("Done.")