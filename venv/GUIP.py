import os
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as ScrolledText
from tkinter import filedialog

root = tkinter.Tk()
root.title("Untitled - Notepad")
#root.grid_rowconfigure(0, weight = 1)
#root.grid_columnconfigure(0, weight = 1) #ignore these
root.geometry("600x500") #self explanatory

def newFile():              #Look into it later. Cancel also clears text.
    if len(text.get('1.0', END+ '-1c')) > 0:
        if messagebox.askyesnocancel("Notepad", "Do you want to save changes to Document?"):
            saveFile()
        else:
            text.delete('1.0', END)

    root.title("Untitled - Notepad")

#Adding functions for menubar options

def openFile():
    file = filedialog.askopenfile(mode = "rb", title = "Select a file", filetypes = (("Text Documents", "*.txt"), ("All files", "*.*")))
    root.title(os.path.basename(file.name) + " - Notepad")

    if file != None:
        contents = file.read()
        text.insert("1.0", contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode = "w", filetypes = (("Text Documents", "*.txt"), ("All files", "*.*")))
    if file != None:
        data = text.get("1.0", END)
        file.write(data)
        file.close()

def quitApplication():

    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()
    else:
        pass

def aboutMe():
    messagebox.showinfo("About me", "My name is Arman. I am from Bangladesh. I am an amateur studying Software Development & Entrepreneurship at Mainor."
                                    " This is my first project. I am running it on Python 3.8. I am sure it'll run fine on Python 3.7")



#creating the Menu bar

bar = tkinter.Menu(root)
root.config(menu = bar)

fileMenu = tkinter.Menu(bar, tearoff = 0)
fileMenu.add_command(label = "New", command = newFile)
bar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Open", command = openFile)
fileMenu.add_command(label = "Save", command = saveFile)
fileMenu.add_command(label = "Exit", command = quitApplication)

helpMenu = tkinter.Menu(bar, tearoff = 0)
helpMenu.add_command(label = "About This Application", command = aboutMe)
bar.add_cascade(label = "Help", menu = helpMenu)

text = ScrolledText.ScrolledText(root, width = 1024, height = 768)
text.configure(font = "consolas 11")
text.pack()


root.mainloop()
exit()