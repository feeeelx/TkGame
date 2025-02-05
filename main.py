import customtkinter as ctk



root = ctk.CTk()
root.geometry("400x150")



def ClickOnClicker():
    print('dd')

clicker = ctk.CTkButton(root, text="my button", command=ClickOnClicker)
clicker.pack(padx=20, pady=20)











root.mainloop()