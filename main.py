import tkinter as tk
import os
import random

FolderDir = "C:\\Users\\felix\\Downloads\\d"
stringvar = "test"
testlist = ['a', 'b', 'c', 'd']

def MakeFolders():
    wordintestlist = testlist[random.randrange(0,3)]
    os.makedirs(FolderDir + '\\ok', exist_ok=True)
    os.makedirs(FolderDir + '\\ok' + wordintestlist, exist_ok=True)


root = tk.Tk()
button = tk.Button(root, text='Make Folders', command=MakeFolders)
button.pack()


tk.mainloop()