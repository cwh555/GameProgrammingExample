from Game import Game
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Breakout")
    game = Game(root)
    game.mainloop()
