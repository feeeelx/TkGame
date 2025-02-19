import tkinter as tk
import os

FolderDir = "C:\\Users\\felix\\Downloads\\d"

def MakeFolders():
    os.makedirs(FolderDir + '\\ok', exist_ok=True)


root = tk.Tk()
button = tk.Button(root, text='ttt', command=MakeFolders)
button.pack()


tk.mainloop()