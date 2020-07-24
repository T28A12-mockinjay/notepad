from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

if __name__ == '__main__':
    root = Tk()
    root.geometry("900x600")
    root.wm_iconbitmap("1.ico")
    root.title("Untitled")
ta = Text(root, font="lucida 10")
ta.pack(fill=BOTH, expand=TRUE)
file = None

def newf():
    global file
    root.title("Untitled - Notepad")
    file = None
    ta.delete(1.0, END)

def openf():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", ".txt")])
    if file == "":
        file = None
    else:

        root.title(os.path.basename(file) + " - Notepad")
        print(file)
        ta.delete(1.0, END)
        f = open(file,"r")
        ta.insert(1.0, f.read())
        f.close()

def savef():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(ta.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(ta.get(1.0, END))
        f.close()



def quitApp():
    root.destroy()
def cut():
    ta.event_generate("<<Cut>>")
def copy():
    ta.event_generate("<<Copy>>")
def paste():
    ta.event_generate("<<Paste>>")
def about():
    showinfo("About", "This is the simplest editor for you.NOTEPAD")


# Menubar
mb = Menu(root)
filem = Menu(mb, tearoff=0)
filem.add_command(label="New", command=newf)
filem.add_command(label="Open", command=openf)
filem.add_command(label="Save", command=savef)
filem.add_separator()
filem.add_command(label="Exit", command=quitApp)
mb.add_cascade(label="File", menu=filem)

editm = Menu(mb, tearoff=0)
editm.add_command(label="Cut", command=cut)
editm.add_command(label="Copy", command=copy)
editm.add_command(label="Paste", command=paste)
mb.add_cascade(label="Edit", menu=editm)

helpm = Menu(mb, tearoff=0)
helpm.add_command(label="About", command=about)
mb.add_cascade(label="Help", menu=helpm)
root.config(menu=mb)


sb = Scrollbar(ta)
sb.pack(side=RIGHT, fill=Y)
sb.config(command=ta.yview)
ta.config(yscrollcommand=sb.set)


root.mainloop()



