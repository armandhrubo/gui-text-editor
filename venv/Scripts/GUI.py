import tkinter

def clickMe():
    button.configure(text ='Hello ' + name.get())

    win = tkinter.Tk()
    win.title('MY GUI')
    win.geometry('250x100')
    win.resizable(0, 0)
