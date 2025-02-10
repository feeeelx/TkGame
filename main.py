import customtkinter as ctk
hawktuah = 1

root = ctk.CTk()
root.geometry("400x150")


def ClickOnClicker():
    global hawktuah
    global tt
    hawktuah = hawktuah + 1
    print(hawktuah)
    tt.pack_forget()
    tt = ctk.CTkLabel(root, text=hawktuah)
    tt.pack()
3
clicker = ctk.CTkButton(root, text="my button", command=ClickOnClicker)
clicker.pack(padx=20, pady=20)

tt = ctk.CTkLabel(root, text=hawktuah)
tt.pack()


root.update()
root.mainloop()