import tkinter as tk

gamelist = ['1', '2']


gamechoice = str(input("'Pile ou face (1)', 'Secret button (2)'"))


def CoinGame():
    CoinGameWindow = tk.Tk()






    CoinGameWindow.mainloop()


while True:
    if gamechoice in gamelist:
        if gamechoice == '1':
            CoinGame()
        if gamechoice == '2':
            print('2')