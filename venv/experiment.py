import os
import tkinter
from tkinter import *
from tkinter import messagebox

class Notepad:

    root = tkinter.Tk()
    #root.wm_iconbitmap("Notepad.ico")
    root.title("Untitled - Notepad")
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)

    #def __init__(self, **kwargs):

    def newFile(self):
        self.root.title("Untitled")
        self.file = None

    def saveFile(self):

        if self.file == None:
            self.file = asksavefilename(fileName = "Untitled.txt",
                                        defaultextension = ".txt",
                                        fileTypes = [("All Files", ".txt")])

    def aboutMe(self):
        messagebox.showinfo("Notepad", "Nope")




